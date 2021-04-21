import numpy as np
import random


print('MY TEST PYTHON CODE....')
for i in range(5):
    print(i)
print('\n\n')
val = []
for i in range(10):
    x = random.randint(1, 20)
    print(x)
    val.append(x)
    
vl = []
for i in range(len(val)):
    j = i + 1
    if j > len(val):
        break
    else :
        if val[i] < val[j]:
            vl[i].append(val[i])
            vl[j].append(val[j])
        else : 
            vl[i].append(val[j])
            vl[j].append(val[i])
    
    
print(val)
print(vl)