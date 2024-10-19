#task 4.1
''' i = 0
a = [0, 1, 0, 12, 3]
while i < len(a):
    if a[i] == 0:
        a.append(a.pop(i))
        i +=1
    else:
        i += 1
print(a)'''
from random import random

# task 4.2
import random
'''b = [0, 1, 7, 2, 4, 8]
sum_b = sum(b[i] for i in range(0, len(b),2))
print(sum_b)
res = sum_b * b[-1]
print(res)'''
#task 4.3
sp = [random.randint(1, 10) for _ in range(random.randint(3, 10))]
print(sp)
new_sp = [sp[0], sp[2] , sp[-2]]
print(new_sp)
sp_sort=sorted(sp)
print(sp_sort)
