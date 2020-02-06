summa = 0
n = 0

while True:
    luku = input('Anna luku, tyhjä lopettaa: ')
    if luku == '':
        break
    summa += float(luku)
    n += 1

print(f'Lukuja {n} kappaletta')
print(f'Summa: {summa:.2f}')
print(f'Keskiarvo: {(summa / n):.2f}')