#1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11


print("Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.")
print("Введите вещественное число через точку: ")
number =  float(input())
str1=str(number)
sum=0
for element in str1:
    if element.isdigit():
        sum += int(element)
print("Сумма цифр равна: " ,sum)