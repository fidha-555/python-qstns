# Question: Check if all elements are unique.

# inp : [4,8,2,9,2,9]
# out : False

# inp : [3,4,1,8]
# out : True

x1 = [4,8,2,9,2,9]
x2 = [3,4,1,8]

for x in (x1,x2):
 u=[]
 unique=True
 for i in x:
    if i in u:
       unique = False
       break
    u.append(i)
 print(unique)
