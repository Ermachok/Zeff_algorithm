

def write_all_ch(sht_num,ch_num,data):
    with open('D:\Ioffe\slowADC\calculations\sht%d\%d_all_ch%d.txt' % (sht_num, sht_num, ch_num) ,'w') as file:
        for i in range(len(data[0])):
            line = '%.3f\t' % (i *2E-3)
            for j in range(len(data)):
                line += '%.4f\t' % data[j][i]
            file.write(line +'\n')  # работа с txt файлами, старая версия
