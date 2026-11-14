# Даны 2 числа А и В (А < В). Вывести в порядке убывания все целые числа расположенные между А и В
# (включая сами числа А и В), а также количество N этих чисел)

A = input("Введите число А ")
B = input("Введите число B ")

while type(A) != int or type(B) != int:
    try:
        A = int(A)
    except ValueError:
        print("Неправильно ввели число А")
        A = input("Введите число А ")

    try:
        B = int(B)
    except ValueError:
        print("Неправильно ввели число B")
        B = input("Введите число B ")

    if A >= B:
        print("Число B должно быть больше А!")
        break

    break

k = 0
while B >= A:
    print(B)
    B -= 1
    k += 1

print(f"\nКол-во чисел: {k}")