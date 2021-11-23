import get_Data
import writing
import processing
import zeff_func

sht_num = 40975

times_ADC = get_Data.get_from_json_ADCdata_ch(sht_num, 1)[0]
for ch_num in range(1, 6):

    all_ch = get_Data.get_from_json_ADCdata_ch(sht_num, ch_num)[1]

    processing.signal_to_zerolvl(all_ch)
    processing.averaging(all_ch, 200)

    writing.write_ADCdata_txt(sht_num, all_ch, times_ADC,ch_num)

print('ok')