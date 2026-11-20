#Дано целое число. С помощью операция деления нацело и взятия остатка от деления определить, есть ли в записи числа N
#нечетные числа. Если есть то вывести true, если нет то false

while True:
    try:
        X = int(input("Введите ваше число "))

    except ValueError:
        print("Нужно вводить ццелые числа")
        exit()

    break

while X > 0:
    Y = X % 10
    if Y % 2 != 0:
        print("True")
        break
    X = X // 10

if X == 0:
    print("False")