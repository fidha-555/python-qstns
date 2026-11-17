# Today's Question: Find two numbers that have the smallest absolute difference.
# inp: [4,9,6,1]
# out: [4,6]
num = [4,1,6,9]
num.sort()

min = num[-1] - num[0]

for i in range(len(num)):
    for j in range(i+1,len(num)):
        if min > num[j] - num[i]:
            x = num[i]
            y = num[j]
            min = num[j] - num[i]

print(x,y)



