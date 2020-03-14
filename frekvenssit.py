def main():
    base = 'abcdefghijklmnopqrstuwvxyzåäö'
    small_chars = list(base)
    
    content = ''
    with open('luku1.txt', 'r', encoding="utf-8") as f:
        content = f.read()
        f.close()

    content = content.lower()
    
    counts = {letter: 0 for letter in small_chars}
    
    for key in counts.keys():
        counts[key] = content.count(key)
    
    kirjaimia = sum(counts.values())
    print(f'Kirjaimia yhteensä: {kirjaimia}')

    # https://docs.python.org/3/howto/sorting.html
    # creates list of tuples
    counts = sorted(counts.items(), key = lambda x : x[1], reverse = True)
    
    for count in counts:
        print(f'{count[0]} : {100 * count[1] / kirjaimia:.2f} %')


if __name__ == "__main__":
    main()