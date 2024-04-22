import numpy as np

for i in np.arange(1,16,1):
    
    if i % 15 ==0:
        print('fizzbuzz')
    elif i % 5 ==0:
        print('buzz')

    elif i % 3 ==0:
        print('fizz')
    else:
        print(i)
