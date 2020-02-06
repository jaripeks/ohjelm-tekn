def tulostaTahtia(maara):
    """ tulostaa maara tahtia ja rivinvaihdon """
    print(maara * '*')

def tulostaNelio(sivu):
    """ tulostaa tahtinelion """
    for _ in range (0, sivu):
        tulostaTahtia(sivu)

def tulostaSuorakulmio(leveys, korkeus):
    """ tulostaa tahtisuorakulmion """
    for _ in range (0, korkeus):
        tulostaTahtia(leveys)

def tulostaKolmio(korkeus):
    """ tulostaa suorakulmaisen kolmion """
    for row in range (1, korkeus + 1):
        tulostaTahtia(row)

def lukusarjanSumma(n):
    """ palauttaa summan 1 + 2 + ... + (n - 1) + n """
    return sum(range(1, n + 1))

def kertoma(n):
    """ palatauttaa kertoman 1 * 2 * ... * (n - 1) * n """
    from functools import reduce
    # reduce(function, iterable, initializer (or inital value))
    return reduce(lambda x,y:x*y, range(1, n + 1), 1)

def main():
    print('Tähdet:')
    tulostaTahtia(5)
    print('Neliö:')
    tulostaNelio(4)
    print('Suorakulmio:')
    tulostaSuorakulmio(5, 3)
    print('Kolmio:')
    tulostaKolmio(6)
    print('Lukusarjan summa n=100:', lukusarjanSumma(100))
    print('Kertoma n=20', kertoma(20))

if __name__ == "__main__":
    main()