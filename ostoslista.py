def jarjestaJaTulosta(lista):
    print(f'Listalla {len(lista)} riviä:')
    lista.sort()
    for l in lista:
        print(l)

def main():
    lista = []
    while True:
        syote = input('Lisää listalle: ')
        if syote == '':
            break
        lista.append(syote)
        jarjestaJaTulosta(lista)


if __name__ == "__main__":
    main()