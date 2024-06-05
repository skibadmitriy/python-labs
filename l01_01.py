s1 = "aaaxbbbxcccy"
s2 = ""

for a in s1:
    if a == "x":
        s2 += "y"
    else:
        s2 += a

print(s1)
print(s2)

'''
aaaxbbbxcccy
aaaybbbycccy
'''
