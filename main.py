import get_Data
import json
import writing

with open('config.json', 'r') as config_file:
    config = json.load(config_file)

sht_num = 40733

temperature_TS = get_Data.get_from_json_TSdata(sht_num)[0] # возвращает массив массивов. каждый массив - температура с одного прибора в разные моменты времени
concentration_TS = get_Data.get_from_json_TSdata(sht_num)[1] # сейм щит но с концентрацией
times_TS = get_Data.get_from_json_TSdata(sht_num)[2] # времена в расчете
writing.write_TS_data(sht_num,temperature_TS,concentration_TS,times_TS)

ADC_times = get_Data.get_from_json_ADCdata_ch1(sht_num)[0]
ADC_signals = get_Data.get_from_json_ADCdata_ch1(sht_num)[1]
writing.write_ADCdata(sht_num, ADC_signals, ADC_times)

dif_time = []
ds_dw = []

for i in range(1,11):
    ds_dw.append(config['chord_%d' %i]['solid_angle'] * config['chord_%d' %i]['square'] )

writing.write_dS_dW(sht_num,ds_dw)

answer = []
for time in range(len(times_TS)):
    for i in range(len(ADC_times)):
        if abs(times_TS[time] - ADC_times[i]) < 0.001:
            all_z_eff = []
            for poly_num in range(1,10):
                #dif_time.append(ADC_times[i])
                signal = ADC_signals[poly_num][i]
                z_eff = 0
                for peace_num in range(len(config['chord_%d' %poly_num]['peaces'])-1):
                    z_eff += config['chord_%d' %poly_num]['peaces'][peace_num] * concentration_TS[peace_num][time]**2 \
                             * temperature_TS[peace_num][time]**(1/2)
                z_eff = z_eff * 2
                z_eff += config['chord_%d' %poly_num]['peaces'][-1] * concentration_TS[-1][time]**2 \
                             * temperature_TS[-1][time]**(1/2)
                z_eff = signal / (z_eff * ds_dw[poly_num])
                all_z_eff.append(z_eff)
            all_z_eff.append(z_eff)
    answer.append(all_z_eff)

for z in answer[10]:
    print(z)
print('hui')