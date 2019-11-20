data1=[[1,2,3,-4,5],
       [6,7,9,0,10],
       [1,3,5,7,9],
       [2,4,-6,8,10]]

for r in data1:
    sum = 0
    for c in r :
        if c < 0 :
            print('got an outlier:%d' % c)
            continue  # compare ..set none use
            break  # compare ..set none use
        else:  # compare ..set none use
            sum += c
    else:
        print('summation=%d' % sum)

