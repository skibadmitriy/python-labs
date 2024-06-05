a = [ 3, 15, 20, 11, 6, 10 ]
p = 1

for c in a:
    if (c % 3) == 0:
        p *= c
    elif (c % 5) == 0:
        p *= c

print(a)
print(p)

'''
[3, 15, 20, 11, 6, 10]
54000
'''
