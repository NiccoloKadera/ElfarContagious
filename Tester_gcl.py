def getContagiousLevel(timeContagiuous, weekBeingContagious):
    x, x_max = 0.1, 1
    x_ts = [x]
    t_max = timeContagiuous
    c, d = 0.5, 0.4

    t = weekBeingContagious
    
    x = x + c * (1 - x / x_max) 
    x = x * ( 1 - t / t_max )

    if weekBeingContagious <= timeContagiuous:

        return x
        
    else:
        return 0



for i in range(0, 10):
    print(getContagiousLevel(5, i))

import os
print(os.path.splitext('ExportCSV_23_PresentBool.csv')[0])