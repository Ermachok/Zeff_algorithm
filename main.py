import get_Data
import json
import writing

sht_num = 777

temperature_TS = get_Data.get_from_json_TSdata(sht_num)[0] # возвращает массив массивов. каждый массив - температура с одного прибора в разные моменты времени
concentration_TS = get_Data.get_from_json_TSdata(sht_num)[1] # сейм щит но с концентрацией
times_TS = get_Data.get_from_json_TSdata(sht_num)[2] # времена в расчете

writing.write_TS_data(sht_num,temperature_TS,concentration_TS,times_TS)

ADC_times = get_Data.get_from_json_ADCdata_ch1(sht_num)[0]
ADC_signals = get_Data.get_from_json_ADCdata_ch1(sht_num)[1]

writing.write_ADCdata(sht_num, ADC_signals, ADC_times)

dif_time = []

for t in times_TS:
    for i in range(len(ADC_times)):
        if abs(t - ADC_times[i]) < 0.001:
            dif_time.append(ADC_times[i])


print('hui')