
# работа с txt файлами, старая версия
def write_all_ch(sht_num,ch_num,data):
    with open('D:\Ioffe\slowADC\calculations\sht%d\%d_all_ch%d.txt' % (sht_num, sht_num, ch_num) ,'w') as file:
        for i in range(len(data[0])):
            line = '%.3f\t' % (i *2E-3)
            for j in range(len(data)):
                line += '%.4f\t' % data[j][i]
            file.write(line +'\n')

def write_TS_data(sht_num,temperature,concentration,times):
    number_of_poly = 10
    with open('D:\Ioffe\slowADC\calculations\sht%d\%d_TS_all_data.txt' % (sht_num,sht_num) ,'w') as file:
        line = 'time,'
        for i in range(number_of_poly):
            line+='poly%d_T, poly%d_n, ' %(int(i+1), int(i+1))
        file.write(line + '\n')
        for j in range(len(times)):
            line = '%.3f,' % (times[j])
            for i in range(len(temperature)):
                line += '%.3e, %.3e, ' %(temperature[i][j], concentration[i][j])
            file.write(line+'\n')
# запись данных TS, вытащенных МНОЙ(вероятно хуева) из json Жильцова

def write_ADCdata(sht_num, adc_data,times):
    number_of_poly = 10
    with open('D:\Ioffe\slowADC\calculations\sht%d\%d_ADC_ch1_data.txt' % (sht_num,sht_num), 'w') as file:
        line = 'time,'
        for i in range(number_of_poly):
            line += 'poly%d, ' % (i+1)
        file.write(line + '\n')

        for j in range(len(times)):
            line = '%.3f,' % (times[j])
            for i in range(len(adc_data)):
                line += '%.3e, ' % adc_data[i][j]
            file.write(line + '\n')

def write_process_ADCdata(sht_num, adc_data,times):
    number_of_poly = 10
    with open('D:\Ioffe\slowADC\calculations\sht%d\%d_process_ADC_ch1_data.txt' % (sht_num,sht_num), 'w') as file:
        line = 'time,'
        for i in range(number_of_poly):
            line += 'poly%d, ' % (i+1)
        file.write(line + '\n')

        for j in range(len(times)):
            line = '%.3f,' % (times[j])
            for i in range(len(adc_data)):
                line += '%.3e, ' % adc_data[i][j]
            file.write(line + '\n')

def write_ADCdata_txt(sht_num, adc_data,times,ch_num):
    number_of_poly = len(adc_data)
    with open('D:\Ioffe\slowADC\calculations\sht%d\%d_process_ADC_ch%d_data.txt' % (sht_num,sht_num,ch_num), 'w') as file:
        line = 'time,'
        for i in range(number_of_poly):
            line += 'poly%d, ' % (i+1)
        file.write(line + '\n')

        for j in range(len(times)):
            line = '%.3f,' % (times[j])
            for i in range(len(adc_data)):
                line += '%.3e, ' % adc_data[i][j]
            file.write(line + '\n')

def write_dS_dW(sht_num,ds_dw):
    with open('D:\Ioffe\slowADC\calculations\sht%d\ds_dw.txt' % (sht_num), 'w') as file:
        file.write('poly number, dS*dOmega \n' )

        for i in range(len(ds_dw)):
            line = '%d, %.4e' %(i+1,ds_dw[i])
            file.write(line + '\n')

def write_z_eff(sht_num,z_eff,times):
    with open('D:\Ioffe\slowADC\calculations\sht%d\%d_z_eff.txt' % (sht_num,sht_num), 'w') as file:
        line = 'poly_num, '
        for t in times:
            line += '%.3f,' % t
        file.write(line +'\n')

        for j in range(len(z_eff[0])):
            line = '%d, ' % int(j+1)
            for i in range(len(z_eff)):
                line += '%.3e, ' % z_eff[i][j]
            file.write(line + '\n')

def write_signals(sht_num,z_eff,times):
    with open('D:\Ioffe\slowADC\calculations\sht%d\%d_signals.txt' % (sht_num,sht_num), 'w') as file:
        line = 'poly_num, '
        for t in times:
            line += '%.3f,' % t
        file.write(line +'\n')

        for j in range(len(z_eff[0])):
            line = '%d, ' % int(j+1)
            for i in range(len(times)):
                line += '%.3e, ' % z_eff[i][j]
            file.write(line + '\n')