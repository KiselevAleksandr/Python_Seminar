print ("Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.")
a = int(input("Введите число дня недели: "))
if a == 6 or a == 7:
    print ("Выходной день")
elif a > 0 and a < 6:
    print ("Будний день")
else:
    print ("Введенное число не является днем недели")