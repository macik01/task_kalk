#task 4.1
i = 0
a = [0, 1, 0, 12, 3]
while i < len(a):
    if a[i] == 0:
        a.append(a.pop(i))
        i +=1
    else:
        i += 1
print(a)