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
# task 4.2
b = [0, 1, 7, 2, 4, 8]
sum_b = sum(b[i] for i in range(0, len(b),2))
print(sum_b)
res = sum_b * b[-1]
print(res)