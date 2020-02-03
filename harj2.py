input_time = int(input('Anna aika sekuntteina: '))
secs = input_time % 60
mins = (input_time // 60) % 60
hrs = (input_time // (60 * 60)) % 24
days = input_time // (60 * 60 * 24)
print(f'{days} paivaa, {hrs} tuntia, {mins} minuuttia, {secs} sekunttia')