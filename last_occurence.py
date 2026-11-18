# Find the last occurrence of a character and return its index.
# inp : sentence = "hello world", k = "l"
# out : 9
s = input("Enter the Sentence:")
k = input("Enter the element:")
a =[]
for i in range(len(s)):
    if k in s[i]:
        a=i
print(a)
