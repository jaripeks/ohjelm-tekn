def takaperin(lista):
    """ näin mä tän kai tekisin """
    kopio = lista.copy()
    kopio.reverse()

    """ tai näin
    kopio = list(lista)
    kopio.reverse()
    """

    """ Kai tän näinkin vois tehdä
    kopio = []
    for luku in lista[::-1]:
      kopio.append(luku)
    print(kopio)
    """

    return kopio

def main():
    lista = [1, 10, 100, 1000]
    print(takaperin(lista))
    print(lista)

if __name__ == "__main__":
    main()