x = [1,4,4,7,7,7,2,2]
count = {}
for i in x:
    if i in count:
        count[i] = count[i] +1
    else:
        count[i] = 1
a =[]
for i in x:
    if count[i] % 2 == 0:
        a.append(i)
print(a)


