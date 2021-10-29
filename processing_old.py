import get_Data
import writing
import processing

sht_num = 40421

all_ch = get_Data.get_txt_slowADC_ch(sht_num,1)[0]
time = get_Data.get_txt_slowADC_ch(sht_num,1)[1]

processing.signal_to_zerolvl(all_ch)
processing.averaging(all_ch,200)

writing.write_ADCdata_txt(sht_num,all_ch,time)

print('ok')