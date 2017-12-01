a = 1
b = 1

print(a)
print(b)

# Print next 20 numbers of fibonacci seq
for i in range(18):
    c = a+b
    print(c)
    a = b
    b = c

