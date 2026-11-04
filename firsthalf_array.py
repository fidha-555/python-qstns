length = int(input("Enter length:"))
num = []
for i in range(length):
    n=int(input("Enter elements:"))
    num.append(n)

if len(num)%2 != 0:
    mid = (len(num)+1)//2

else:
    mid = len(num)//2

half_arr = num[:mid]
print(half_arr)








# a = input("Enter your list:")
# mid = (len(a)+1)//2
# new_arr = a[:mid]
# print(new_arr)
#     mid = (len(a)+1)//2
# else:
#     mid = len(a)//2
# new_arr = a[:mid]
# print(new_arr)










# arr = [6,7,2,9,1]
# mid = (len(arr)+1)//2
# new_arr = [arr[:mid]]
# print(new_arr)
