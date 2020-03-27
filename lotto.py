import random


def getRandom(lista):
    """ poistaa ja palauttaa satunnaisen luvun parametrina saadulta listalta """
    luku = lista.pop(random.randint(0, len(lista) - 1))
    return(luku)


def lottoarvonta():
    """
    palauttaa tuplen (list(numerot), list(lisanumerot))
    arpoo molemmat listat samasta numeropoolista [1, 41[
    jokainen arvottu luku uniikki integer
    """
    luvut = list(range(1, 41))
    numerot = []
    while len(numerot) < 7:
        numerot.append(getRandom(luvut))

    lisat = []
    while len(lisat) < 3:
        lisat.append(getRandom(luvut))

    numerot.sort()
    lisat.sort()

    return (numerot, lisat)


def pelaa():
    """ palauttaa listan, johon arvottu 7 lukua väliltä [1, 41[ jokainen arvottu luku uniikki integer """
    luvut = list(range(1, 41))
    numerot = []
    while len(numerot) < 7:
        numerot.append(getRandom(luvut))
    numerot.sort()
    return numerot

def tarkista(arvonta, rivi):
    """
    tarkistaa kuinka monta samaa lukua on param rivi ja param arvonta[0] sekä param rivi ja param arvonta[1]
    tulostaa tuloksen
    """
    # pelatut täytyy olla set, jotta voi kutsua metodia intersection
    pelatut = set(rivi)
    # samat on tuple (samat_pelatut, samat_lisanumerot) koska why not
    samat = (pelatut.intersection(set(arvonta[0])), pelatut.intersection(set(arvonta[1])))
    print(f"{len(samat[0])} oikein {list(samat[0])} ja {len(samat[1])} lisänumeroa {list(samat[1])}")

def main():
    """ kopioitu suoraan tehtävänannosta """
    arvonta = lottoarvonta()
    print('Oikea rivi:', end=' ')
    print(*arvonta[0], sep=', ')
    print('Lisänumerot:', end=' ')
    print(*arvonta[1], sep=', ')

    rivi = pelaa()
    print('Rivi:', end=' ')
    print(*rivi, sep = ', ')

    tarkista(arvonta, rivi)

if __name__ == "__main__":
    main()
