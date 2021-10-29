import get_Data
import json

import processing
import writing

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

with open('sht_number.txt','r') as shot_file:
    sht_num = int(shot_file.read())

temperature_TS = get_Data.get_from_json_TSdata(sht_num)[0] # возвращает массив массивов. каждый массив - температура с одного прибора в разные моменты времени
concentration_TS = get_Data.get_from_json_TSdata(sht_num)[1] # сейм щит но с концентрацией
times_TS = get_Data.get_from_json_TSdata(sht_num)[2] # времена в расчете
writing.write_TS_data(sht_num,temperature_TS,concentration_TS,times_TS)

ADC_times = get_Data.get_from_json_ADCdata_ch1(sht_num)[0]
ADC_signals = get_Data.get_from_json_ADCdata_ch1(sht_num)[1]

writing.write_ADCdata(sht_num, ADC_signals, ADC_times)

processing.signal_to_zerolvl(ADC_signals)
average_ADC = processing.averaging(ADC_signals, 200)
writing.write_process_ADCdata(sht_num, average_ADC, ADC_times)

dif_time = []
ds_dw = []

for i in range(1,11):
    ds_dw.append(config['chord_%d' %i]['solid_angle'] * config['chord_%d' %i]['square'] )

writing.write_dS_dW(sht_num,ds_dw)

answer_zeff = []
signal_in_use = []
all_signals = []
all_z_eff = []
z_eff = 0
#number_of_poly = 9
number_of_chord = 10

for time in range(len(times_TS)):
    for i in range(len(ADC_times)):
        if abs(times_TS[time] - ADC_times[i]) < 0.001:
            all_z_eff = []
            signal_in_use = []
            for chord_num in range(0, number_of_chord):
                #dif_time.append(ADC_times[i])

                z_eff = 0
                for peace_num in range(len(config['chord_%d' %(chord_num + 1)]['peaces']) - 1):
                    print('time %f,chord  %d,peace %f,conc %e,temp %f' % (ADC_times[i],
                                                                          (chord_num + 1), config['chord_%d' % (chord_num + 1)]['peaces'][peace_num],
                                                                          concentration_TS[peace_num][time],
                                                                          temperature_TS[peace_num][time]))
                    z_eff += config['chord_%d' % (chord_num + 1)]['peaces'][peace_num] * concentration_TS[peace_num][time] ** 2 \
                             * temperature_TS[peace_num][time] ** (1/2)

                z_eff = z_eff * 2
                print('time %f,chord  %d,peace %f,conc %e,temp %f' % (ADC_times[i],
                                                                     (chord_num + 1),
                                                                     config['chord_%d' % (chord_num + 1)]['peaces'][-1],
                                                                     concentration_TS[peace_num+1][time],
                                                                     temperature_TS[peace_num+1][time]))

                z_eff += config['chord_%d' % (chord_num + 1)]['peaces'][-1] * concentration_TS[peace_num + 1][time] ** 2 \
                         * temperature_TS[peace_num+1][-1] ** (1/2)

                signal = average_ADC[chord_num][i]
                signal_in_use.append(signal)
                z_eff = signal / (z_eff * ds_dw[chord_num]) * 1e39

                all_z_eff.append(z_eff)
            #all_z_eff.append(z_eff)
    all_signals.append(signal_in_use)
    answer_zeff.append(all_z_eff)

print(len(answer_zeff))
print(len(times_TS))
print(len(all_signals))
writing.write_z_eff(sht_num,answer_zeff,times_TS)
writing.write_signals(sht_num,all_signals,times_TS)
print('end')