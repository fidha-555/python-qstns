num = [10,7,4,8,9,4,7,7,10,1,7,1]
count = {}
tot = 0
for i in num:
    if i not in count:
        count[i] = 1
    else:
        count[i] = count[i]+1
print(count)
for i in count:
    if count[i] > 1:
        tot +=1
print(tot)