#Задача 5
#""" Напишите программу, которая принимает на вход координаты двух точек 
#и находит расстояние между ними в 2D пространстве. 
#Пример: - A (3,6); B (2,1) -> 5,09 - A (7,-5); B (1,-1) -> 7,21 """


print("Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.")
xa = int(input("Введите координату х точки а: "))
ya = int(input("Введите координату y точки а: "))
xb = int(input("Введите координату х точки b: "))
yb = int(input("Введите координату y точки b: "))
res = round((((xa - xb)**2 + (ya - yb)**2)**0.5), 2)
print(f"Расстояние между точками {res}")