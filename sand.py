import json

def get_json_TSdata(sht_num):

    with open('D:\Ioffe\slowADC\calculations\sht%d\%d.json' %(sht_num, sht_num), 'r') as file:
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

    for t in temperature_TS:
        print(t)

