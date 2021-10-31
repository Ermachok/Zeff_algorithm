import get_Data
import writing
import processing
import zeff

sht_num = 40421

temperature_TS = get_Data.get_from_json_TSdata(sht_num)[0] # возвращает массив массивов. каждый массив - температура с одного прибора в разные моменты времени
concentration_TS = get_Data.get_from_json_TSdata(sht_num)[1] # сейм щит но с концентрацией
times_TS = get_Data.get_from_json_TSdata(sht_num)[2] # времена в расчете
writing.write_TS_data(sht_num,temperature_TS,concentration_TS,times_TS)

all_ch = get_Data.get_txt_slowADC_ch(sht_num, 1)[0]
times_ADC = get_Data.get_txt_slowADC_ch(sht_num, 1)[1]

processing.signal_to_zerolvl(all_ch)
processing.averaging(all_ch, 200)

writing.write_ADCdata_txt(sht_num, all_ch, times_ADC)

zeff.z_eff_calculation(times_TS,concentration_TS,temperature_TS,times_ADC,all_ch)

print('ok')