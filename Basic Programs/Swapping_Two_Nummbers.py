a = 4
b = 2
print("Before swapping: a =", a, "b =", b)

# logic  1
# a, b = b, a

# logic 2
# temp = a
# a = b
# b = temp

# logic 3
# a = a + b
# b = a - b
# a = a - b

# logic 4
a = a^b
b = a^b
a = a^b

print("After swapping: a =", a, "b =", b)