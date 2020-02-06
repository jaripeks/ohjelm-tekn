paino = float(input('Anna paino kiloina: '))
pituus = float(input('Anna pituus senttimetreinä: '))
painoIndeksi = paino / ((pituus / 100) ** 2)
tulostus = f'Painoindeksi {painoIndeksi:.1f} on '

if painoIndeksi < 18.5:
    tulostus += 'ihannetta pienempi'
elif painoIndeksi < 25:
    tulostus += 'ihannepaino'
elif painoIndeksi < 30:
    tulostus += 'lievä ylipaino'
elif painoIndeksi < 35:
    tulostus += 'merkittävä lihavuus'
elif painoIndeksi < 40:
    tulostus += 'vaikea lihavuus'
else:
    tulostus += 'sairaalloinen lihavuus'

print(tulostus)