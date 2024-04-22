import numpy as np

for i in np.arange(1,16,1):
    
    if i % 3 ==0:
        print('fizz')
    else:
        print(i)

    if i % 5 ==0:
        print('buzz')

    if i % 15 ==0:
        print('fizzbuzz')
