a = [5,8,3,9,2,10]
smallest = a[0]
largest = a[0]

for num in a:
    if num > largest:
        largest = num
        
    if num < smallest:
        smallest = num
        
diff = largest - smallest
print (diff)