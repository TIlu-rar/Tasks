x = int(input("Жасыңызды енгізіңіз: "))
while True:
    if x < 18:
        print("Сіз кәмелеттік жасқа толмағансыз")
    elif 18 < x < 65:
        print("Сіз ересексіз")
    elif x > 65:
        print("Сіз зейнеткерсіз")
    break
