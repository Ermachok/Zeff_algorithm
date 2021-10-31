import json

def z_eff_calculation(TS_times,TS_conc,TS_temp,ADC_times,ADC_signal):

    print('length of TS data concentration: %d, should be equal to or greater than length of ADC_signal list' % len(TS_conc))
    print('length of TS data temperature: %d, should be equal to or greater than length of ADC_signal list' % len(TS_temp))
    print('number of time points in TS data: %d' % len(TS_times))
    print('number of chords with slow ADC signals %d ' %len(ADC_signal))
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    ds_dw = []
    for i in range(0, len(config)):
        ds_dw.append(config['chord_%d' % (i+1)]['solid_angle'] * config['chord_%d' % (i+1)]['square'])


    ts_time = TS_times[0]
    for adc_time in ADC_times:
        if (ts_time - adc_time) < 0.001:
            adc_index = ADC_times.index(adc_time)

            for chord_num in range(0,len(ADC_signal)):

                adc_signal = ADC_signal[chord_num][adc_index]
                geom_factor = ds_dw[chord_num]


                for peace_num in range(len(config['chord_%d' %(chord_num+1)]['peaces']) - 1):
                    summ =