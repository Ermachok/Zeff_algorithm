import json

def get_txt_slowADC_ch(sht_num, ch_num): # возвращает список с выбранным каналом каждого полихроматора c slow adc from txt
    all_ch = []
    for ip in range(3):
        data = []
        with open('D:\Ioffe\slowADC\calculations\sht%d\\192.168.10.5%d.txt' % (sht_num, ip), 'r') as file:
            for line in file:
                data.append([float(x) for x in line.split()])
        for poly_num in range(3):
            ch1 = []
            for i in range(len(data)):
                ch1.append(data[i][1+ch_num + poly_num * 5])

            all_ch.append(ch1)
    return all_ch

def get_csv_TSdata(sht_num):  # csv
    radius = []
    time = []
    concentration_TS = []

    with open('D:\Ioffe\slowADC\calculations\sht%d\%d_n(R).csv' % (sht_num, sht_num), 'r') as file:
        lines = file.readlines()
        for i in range(2, len(lines)):
            temp = lines[i].split(',')
            radius.append(float(temp[0]))
            conc = []
            for j in range(1, int(len(temp) / 2)):
                try:
                    conc.append(float(temp[j * 2 - 1]))
                except ValueError:
                    conc.append(0)
            concentration_TS.append(conc)

    with open('D:\Ioffe\slowADC\calculations\sht%d\%d_n(t).csv' % (sht_num, sht_num), 'r') as file:
        lines = file.readlines()
        for i in range(2, len(lines)):
            temp = lines[i].split(',')
            time.append(float(temp[0]))
        print(len(time))

def get_json_TSdata(sht_num):
    with open('D:\Ioffe\slowADC\calculations\sht%d\%d.json' % (sht_num, sht_num), 'r') as file:
        TS_data_file = json.load(file)

    times = []
    index_TS = []
    temperature_TS = []
    concentration_TS = []

    for i in range(1, len(TS_data_file['events'])):
        if 'timestamp' in TS_data_file['events'][i] \
                and TS_data_file['events'][i]['error'] is None \
                and TS_data_file['events'][i]['T_e'][0]['error'] is None \
                and TS_data_file['events'][i]['T_e'][9]['error'] is None:
            index_TS.append(i)
            times.append(TS_data_file['events'][i]['timestamp'])

    for j in range(len(TS_data_file['events'][1]['T_e'])):
        temp_temp = []
        temp_conc = []
        for i in index_TS:
            temp_temp.append(TS_data_file['events'][i]['T_e'][j]['T'])
            temp_conc.append(TS_data_file['events'][i]['T_e'][j]['n'])
        temperature_TS.append(temp_temp)
        concentration_TS.append(temp_conc)

    return temperature_TS,concentration_TS
