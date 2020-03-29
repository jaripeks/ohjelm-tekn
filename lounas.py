from urllib.request import urlopen
import json

def main():
    data = ''
    with urlopen('https://www.fazerfoodco.fi/modules/json/json/Index?costNumber=0083&language=fi') as response:
        for line in response:
            data = data + line.decode('utf-8')
    data = json.loads(data)
    print(data['MenusForDays'])

if __name__ == "__main__":
    main()