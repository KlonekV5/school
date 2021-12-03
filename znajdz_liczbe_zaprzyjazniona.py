a = int(input('Podaj pierwsza liczbe zaprszyjazniona: '))
z = 0

for i in range (1,a):
    if a % i == 0:
        z = z + i

x = 0

for i in range (1,z):
    if z % i == 0:
            x = x + i
if x == a:
    print('Liczby sa zaprzyjaznione, druga liczba wynosi', z)
    exit()

print('liczba nie ma liczby zaprzyjaznionej')
