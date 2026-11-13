# Today's question: Check if a given list contains only numbers.

# Inp: ["7", "0", "python", "6", "sql"]
# out: False

# Inp: ["7", "5", "2", "8"]
# out: True                                                           

l = ["7","0","6"]
try:
    for i in l:
      int(i)
    print(True)
except:
    print(False)
       