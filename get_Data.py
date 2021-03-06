import json

def get_txt_slowADC_ch(sht_num, ch_num): # возвращает список с выбранным каналом каждого полихроматора c slow adc from txt
    all_ch = []
    times = []

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

    for j in range(len(data)):
        times.append(data[j][0] * 0.002)

    return all_ch,times

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

def get_from_json_TSdata(sht_num):
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
                and TS_data_file['events'][i]['T_e'][1]['error'] is None \
                and TS_data_file['events'][i]['T_e'][2]['error'] is None \
                and TS_data_file['events'][i]['T_e'][3]['error'] is None \
                and TS_data_file['events'][i]['T_e'][5]['error'] is None \
                and TS_data_file['events'][i]['T_e'][4]['error'] is None \
                and TS_data_file['events'][i]['T_e'][9]['error'] is None \
                and TS_data_file['events'][i]['T_e'][6]['error'] is None \
                and TS_data_file['events'][i]['T_e'][7]['error'] is None :
            index_TS.append(i)
            times.append(float(TS_data_file['events'][i]['timestamp']))

    for j in range(len(TS_data_file['events'][1]['T_e'])):
        temp_temp = []
        temp_conc = []
        print()
        for ind in index_TS:
            temp_temp.append(TS_data_file['events'][ind]['T_e'][j]['T'])
            temp_conc.append(TS_data_file['events'][ind]['T_e'][j]['n'])
        temperature_TS.append(temp_temp)
        concentration_TS.append(temp_conc)

    return temperature_TS,concentration_TS,times

def get_from_json_ADCdata_ch(sht_num,ch_num):

    ADC_num = 4
    adc_time = []
    poly_ch = []
    with open('D:\Ioffe\slowADC\calculations\sht%d\\192.168.10.50.json' % (sht_num), 'r') as file:

        ADC_data_file = json.load(file)
        for i in range(1, len(ADC_data_file)):
            adc_time.append(ADC_data_file[i]['time'])

        #for ip in range(4):
        for ip in range(ADC_num):
            try:
                with open('D:\Ioffe\slowADC\calculations\sht%d\\192.168.10.5%d.json' % (sht_num, ip), 'r') as file:
                    ADC_data_file = json.load(file)
                    for j in range(3):
                        ch = []
                        for i in range(1, len(ADC_data_file)):
                            ch.append(float(ADC_data_file[i]['ch'][j*5 + ch_num]))
                        poly_ch.append(ch)
            except FileNotFoundError:
                print('ti lox')
                for j in range(3):
                    ch = []
                    for i in range(1, len(ADC_data_file)):
                        ch.append(1e-4)
                    poly_ch.append(ch)
    return adc_time, poly_ch




