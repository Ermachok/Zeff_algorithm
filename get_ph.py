import json

sht_num = 41526
poly_num = 6 #7 if counts from 1
#laser_shot = 15
ch_num = 0
ph_el = []
time = []

with open('C:/Users/FTI Ioffe/Downloads/Telegram Desktop/%d.json' %(sht_num), 'r') as file:
    data_file = json.load(file)
    for laser_shot in range(30, len(data_file['data'])):
        temp = []
        time.append(data_file['data'][laser_shot]['timestamp'])
        #print('time %f \n' %data_file['data'][laser_shot]['timestamp'])
        for ch_num in range(5):
            temp.append(data_file['data'][laser_shot]['poly']['%d' %poly_num]['ch'][ch_num]['ph_el'])
            #print(data_file['data'][laser_shot]['poly']['%d' %poly_num]['ch'][ch_num]['ph_el'])
        ph_el.append(temp)

with open('D:/Ioffe/slowADC/calculations/sht%d/ph_el_%d_poly.csv' % (sht_num,poly_num+1), 'w') as res_file:
    line = 'time, '
    for i in range(5):
        line += 'ch_%d, ' %(i+1)
    res_file.write(line + '\n')

    for j in range(len(time)):
        line = '%f, ' % (time[j] * 1E-3)
        for i in range(len(ph_el[j])):
            line += '%.3e, ' % ph_el[j][i]
        res_file.write(line + '\n')


print(ph_el[0])
print(len(time), len(ph_el))