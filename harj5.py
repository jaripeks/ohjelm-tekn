import sys

def main():
    if len(sys.argv) != 4 or sys.argv[1] not in ['--upper', '--lower']:
        print('usage: python harj5.py --upper|--lower <file-to-read> <file-to-write>')
        sys.exit(1)
    
    # does not work if either file does not exist (needs try-statements)
    with open(sys.argv[2]) as fileToRead:
        # writes, does not append
        with open(sys.argv[3], 'w') as fileToWrite:
            for line in fileToRead:
                # we have already checked that sys.argv[1] is in ['--upper', '--lower']
                if sys.argv[1] == '--upper':
                    fileToWrite.write(line.upper())
                else:
                    fileToWrite.write(line.lower())

if __name__ == "__main__":
    main()