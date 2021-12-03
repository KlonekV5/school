a = int(input('Podaj pierwsza liczbe: '))
b = int(input('Podaj druga liczbe: '))
c = a * b

while b != 0:
    r = a % b
    a = b
    b = r

x = c / a

print(f'NWW wynosi: {x}')
