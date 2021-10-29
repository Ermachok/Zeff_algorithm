
def signal_to_zerolvl(adc_signal):

    for poly_num in range(len(adc_signal)):
        temp = sum(adc_signal[poly_num][:500]) / 500
        for i in range(len(adc_signal[poly_num])):
            #print(temp)
            adc_signal[poly_num][i] = adc_signal[poly_num][i] - temp

def averaging(adc_signal,window):
    all_poly = []

    if window % 2 == 0:
        window += 1

    hw = (window-1)/2

    for poly_num in range(len(adc_signal)):
        n = len(adc_signal[0])
        answer = []
        answer.append(adc_signal[poly_num][0])

        for i in range(1, n):
            init_sum = 0
            if i <= hw:
                start = 1
                end = 2 * i - 1
                w_size = end
            elif i + hw > n:
                start = i - n + i
                end = n
                w_size = end - start
            else:
                start = i - hw
                end = i + hw
                w_size = window

            #print(i)
            #print(int(start),int(end))

            for j in range(int(start),int(end)):
                init_sum = init_sum + adc_signal[poly_num][j]

            result = init_sum/w_size
            answer.append(result)
        all_poly.append(answer)

    return all_poly