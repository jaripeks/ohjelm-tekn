import math

kateetti_1 = float(input('Anna kateetti 1: '))
kateetti_2 = float(input('Anna kateetti 2: '))
print(f'Kolmion pinta-ala: {(kateetti_1 * kateetti_2 / 2):.2f}')
print(f'Hypotenuusan pituus: {math.sqrt(kateetti_1 ** 2 + kateetti_2 ** 2):.2f}')