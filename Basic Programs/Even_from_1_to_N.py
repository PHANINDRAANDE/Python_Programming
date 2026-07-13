# method 1

n = int(input("Enter a number: "))
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)

# method 2
for i in range(2, n+1, 2):
    print(i)