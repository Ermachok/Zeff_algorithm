import get_Data
import writing
import processing

sht_num = 41567
#770,771,772,774,778,787,791

times_ADC = get_Data.get_from_json_ADCdata_ch(sht_num, 1)[0]
for ch_num in range(1,3):

    all_ch = get_Data.get_from_json_ADCdata_ch(sht_num, ch_num)[1]

    processing.signal_to_zerolvl(all_ch)
    processing.averaging(all_ch, 400)

    writing.write_ADCdata_txt(sht_num, all_ch, times_ADC,ch_num)

print('sht num = %d ok' %sht_num)