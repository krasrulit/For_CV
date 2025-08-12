# Решите в целых числах уравнение: (a * x + b) ** 0.5 = c 
# a, b, c – данные целые числа: найдите все решения или сообщите, что решений в целых числах нет.

a, b, c = int(input()), int(input()), int(input())

if c < 0:
    print("NO SOLUTION")

else:

    if a == 0:

        if b == c**2:
            print("MANY SOLUTIONS")
        else:
            print("NO SOLUTION")


    elif b == 0 and a == 0:

        if c == 0:
            print("MANY SOLUTIONS")
        else:
            print("NO SOLUTION")

    elif c == 0 and a == 0:

        if b == 0:
            print("MANY SOLUTIONS")
        else:
            print("NO SOLUTION")

    else:

        if (c**2 - b) % a != 0:
            print("NO SOLUTION")
        else:
            print((c**2 - b) // a)
