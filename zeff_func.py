import json

def z_eff_calculation(TS_times,TS_conc,TS_temp,ADC_times,ADC_signal):

    print('length of TS data concentration: %d, should be equal to or greater than length of ADC_signal list' % len(TS_conc))
    print('length of TS data temperature: %d, should be equal to TS temperature list' % len(TS_temp))
    print('number of time points in TS data: %d' % len(TS_times))
    print('number of chords with slow ADC signals %d ' % len(ADC_signal))
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    ds_dw = []
    for i in range(0, len(config)):
        ds_dw.append(config['chord_%d' % (i+1)]['solid_angle'] * config['chord_%d' % (i+1)]['square'])

    answer = []
    t = []
    for index_time in range(0, len(TS_times)):
        ts_time = TS_times[index_time]
        for adc_time in ADC_times:
            if abs(adc_time - ts_time) < 0.00101:
                t.append(adc_time)
                adc_index = ADC_times.index(adc_time)
                all_chords = []

                #for chord_num in range(0,len(ADC_signal)):
                for chord_num in range(0,len(TS_conc)):

                    adc_signal = ADC_signal[chord_num][adc_index]
                    geom_factor = ds_dw[chord_num]
                    summ = 0

                    for peace_num in range(len(config['chord_%d' %(chord_num+1)]['peaces']) - 1):
                        approx_conc = ( TS_conc[peace_num][index_time] + TS_conc[peace_num + 1][index_time] ) / 2
                        approx_temp = ( TS_temp[peace_num][index_time] + TS_temp[peace_num + 1][index_time] ) / 2
                        summ += config['chord_%d' %(chord_num+1)]['peaces'][peace_num] * approx_conc **2 * approx_temp**(0.5)

                    summ = summ * 2
                    summ += config['chord_%d' %(chord_num+1)]['peaces'][-1] * TS_conc[peace_num+1][index_time] **2 \
                            * TS_temp[peace_num + 1][index_time]**(0.5)
                    summ = summ * geom_factor

                    z_eff = adc_signal / summ * 1e39
                    all_chords.append(z_eff)
                answer.append(all_chords)

    return answer,t