while True:
    x = int(input("Бірінші сан: "))
    y = int(input("Екінші сан: "))
    z = input("Таңба: ")

    if z == '+':
        print(x + y)
    elif z == '-':
        print(x - y)
    elif z == '*':
        print(x * y)
    elif z == '/':
        if y == 0:
            print("Сан 0 ге бөлінбейді")
        print(x / y)