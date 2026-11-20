a = list(map(int, input("Enter elements:").split()))

b = list(map(int, input("Enter the elements:").split()))
for  i in b:
    a.append(i)

print(a)
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i]> a[j]:
            temp = a[i]
            a[i]=a[j]
            a[j] = temp
print(a)

