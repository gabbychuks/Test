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
    
print(val)

vl = np.sort(val)

print(vl)


