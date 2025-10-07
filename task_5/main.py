import math
x = float(input("Введите координату x точки: "))
y = float(input("Введите координату y точки: "))
r = float(input("Введите радиус круга: "))
if r <= 0:
    print("Радиус должен быть положительным")
dist=math.sqrt(x**2 + y**2)
if dist <= r:
    print("Точка находится внутри круга")
else:
    print("Точка находится вне круга")
