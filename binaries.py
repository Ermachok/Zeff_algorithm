import converter
import json
import os
import sys

result = []
adc_range = 5
ch_count = 16

sht_num = 777
ch_map = [0, 8, 1, 9, 2, 10, 3, 11, 5, 13, 4, 12, 7, 15, 6, 14]

ADC_ip = ['192.168.10.50',
          '192.168.10.51',
          '192.168.10.52',
          '192.168.10.53']

if not os.path.isdir('D:\Ioffe\slowADC\calculations\sht%i' % sht_num):
     os.mkdir('D:\Ioffe\slowADC\calculations\sht%i' % sht_num)
     print('Folder D:\Ioffe\slowADC\calculations\sht%i created' %sht_num)
else:
    print('Folder already exist')
    sys.exit()

for ip in ADC_ip:
    final_result = []
    config = {}

    with open('D:\Ioffe\slowADC\measurements\sht%i\%s.slow' % (sht_num, ip), 'rb') as file:
    #with open('D:\Ioffe\slowADC\measurements\date11.10.2021\sht%i\%s.slow' % (sht_num, ip), 'rb') as file:
        config['ip'] = ip
        config['sht_num'] = sht_num
        config['ADC range'] = '%.2f V '%adc_range

        m = file.read()
        final_result.append(config)
        for j in range(int(len(m)/(ch_count*2))):  #количество отсчетов, т.е. количество байтов делю на 16 каналов по 2 байта каждый

            dict = {}
            chan = [0 for i in range(ch_count)]

            for ch in range(16):

                temp = m[ch * 2 + j * (ch_count*2) ] + m[ch * 2 + 1 + j * (ch_count*2)] * 256

                if temp / 32767 >= 1:
                    res = ''
                    temp = bin(temp)[2:]

                    for i in range(len(temp)):
                        if int(temp[i]) == 1:
                            res += '0'
                        else:
                            res += '1'
                    temp = float(converter.convert_base(res, 10, 2))

                    temp = - (temp + 1)
                    result.append(temp)
                    dict['time'] = float('{:.3f}'.format(j * 2E-3))
                    chan[ch_map[ch]] = float('{:.4f}' .format(temp * adc_range / 32767))

                else:
                    result.append(temp)
                    dict['time'] = float('{:.3f}'.format(j * 2E-3))
                    chan[ch_map[ch]] = float('{:.4f}' .format(temp * adc_range / 32767))
                dict['ch'] = chan
            final_result.append(dict)

    with open('D:\Ioffe\slowADC\calculations\sht%i\%s.json' % (sht_num, ip), 'w') as w_file:
        json.dump(final_result, w_file)

print('ok')