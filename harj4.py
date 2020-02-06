import random

def getAsento(merkki):
    """ palauttaa asennon parametrina annetun luvun perusteella: 1=Kivi, 2=Paperi, 3=Sakset """
    if merkki == 1:
        return 'Kivi'
    elif merkki == 2:
        return 'Paperi'
    elif merkki == 3:
        return 'Sakset'
    return ''

def getVoittaja(valittu, arvottu):
    """ tulostaa voittajan annettujen lukujen mukaan """
    if valittu == arvottu:
        print('Tasapeli')
    elif valittu == 1:
        if arvottu == 2:
            print('Paperi voittaa kiven, hävisit')
        else:
            print('Kivi voittaa sakset, voitit')
    elif valittu == 2:
        if arvottu == 1:
            print('Paperi voittaa kiven, voitit')
        else:
            print('Sakset voittaa paperin, hävisit')
    else:
        if arvottu == 1:
            print('Kivi voittaa sakset, hävisit')
        else:
            print('Sakset voittaa paperin, voitit')


def pelaa(valittu):
    """ arpoo tietokoneen asennon, tulostaa pelatun - arvotun asennon, ilmoittaa kumpi voitti """
    arvottu = random.randint(1,3)
    print(f'{getAsento(valittu)} - {getAsento(arvottu)}')
    getVoittaja(valittu, arvottu)


def main():
    while True:
        syote = input('Kivi (1), paperi (2) vai sakset (3)? Tyhjä vastaus lopettaa:')
        if syote == '':
            break
        
        luku = int(syote)
        if luku < 1 or luku > 3:
            print('Yritä uudelleen! Syötä 1, 2 tai 3')
            continue
        
        pelaa(luku)
    print('Kiitos')

if __name__ == "__main__":
    main()