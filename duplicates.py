l = [2,3,4,5,6,3,7,4]
x = []
y= []

for i in l:
    if i not in x:
        x.append(i)
    else:
        y.append(i)


print(y)