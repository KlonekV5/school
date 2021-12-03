x = input('podaj pesel: ')
mult = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
e = 0
cyfry = list(x)

if len(x) != 11:
    print('Niepoprawny numer pesel')
    quit()

suma = sum([int(n) * i for i, n in zip(mult, cyfry)])

if suma % 10 != 0:
    print('Niepoprawny numer pesel')
    quit()

d = int(''.join(cyfry[4:6]))
m = int(''.join(cyfry[2:4]))

if m > 20:
    m = m - 20
    e = 1

r = str(19 + e) + ''.join(cyfry[0:2])

if int(cyfry[9]) % 2 == 0:
    p = 'kobieta'
else:
    p = 'mezczyzna'

print('Poprawny numer pesel')
print(f"Twoja data urodzenia to: {d}.{m}.{r}")
print(f'Twoja plec to: {p}')
