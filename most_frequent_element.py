num = [10,7,4,8,9,4,7,7,10,1,7,1]
count= {}
for i in num:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1
print(count)
max_count = 0
max_freq =0
for i in count:

    if count[i] > max_count:
        max_count = count[i]
        max_freq = i
print(max_freq)