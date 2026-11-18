l = int(input("Enter the length:"))
x = {}
for i in range(l):
    a = input("Enter Key:")
    b = input("Enter Value:")
    x.update({a:b})
print(x)

