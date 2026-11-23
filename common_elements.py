# Ques : Find common elements between three arrays.
# inp : first = [8,3,7,1] , second = [9,2,7,8], third = [9,7,8,2]
# out: [8,7]
first = [8,3,7,1]
second = [9,2,7,8]
third = [9,7,8,2]
res = []
for x in first:
    if x in second and x in third:
        res.append(x)
print(res)