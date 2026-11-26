l =[1,2,3,4,5,6]
k=3
i = len(l)-k
j= len(l)-1
while i<j:
    
    temp = l[i]
    l[i] = l[j]
    l[j] = temp

    i+=1
    j-=1

print(l)