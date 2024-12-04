San = int(input("Нешеге дейін: "))
x = 0
y = 1
z = 1
n = 0
while True:
    n = n + 1
    print(z)
    if n == San:
        break
    z = x + y
    y = z
    x = z - x


