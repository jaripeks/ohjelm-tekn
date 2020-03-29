import sys

def main():
    if len(sys.argv) != 4 or sys.argv[1] not in ['--upper', '--lower']:
        print('usage: python teht4_2.py --upper|--lower <file-to-read> <file-to-write>')
        sys.exit(1)
    
    try:
        with open(sys.argv[2]) as fileToRead:
            # writes, does not append
            with open(sys.argv[3], 'w') as fileToWrite:
                for line in fileToRead:
                    # we have already checked that sys.argv[1] is in ['--upper', '--lower']
                    if sys.argv[1] == '--upper':
                        fileToWrite.write(line.upper())
                    else:
                        fileToWrite.write(line.lower())
    except Exception as error:
        print('Conversion failed:')
        print(f'{type(error)} - {error}')

if __name__ == "__main__":
    main()