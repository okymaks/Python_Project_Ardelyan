while True:
    try:
        A = int(input("Введите число: "))
        if A % 2 == 1:
            print("Число A нечетное")
        else:
            print("Число A или нуль или четное")

    except ValueError:
        print("Нужно вводить числа")
