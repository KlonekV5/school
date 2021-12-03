import math

a = int(input('podaj a dla: ax^2 + bx + c '))
b = int(input('podaj b dla: ax^2 + bx + c '))
c = int(input('podaj c dla: ax^2 + bx + c '))
d = (b ** 2) - (4 * a * c)

print(f'delta wynosi: {d}')

if d < 0:
    print('brak miejsc zerowych')
elif d == 0:
    x = (-b)/(2*a)
    print(f'jedno miejsce zerowe: {x}')
else:
    x = (-b + math.sqrt(d)) / (2 * a)
    y = (-b - math.sqrt(d)) / (2 * a)
    print(f'dwa miejsca zerowe: {x}, {y} ')


