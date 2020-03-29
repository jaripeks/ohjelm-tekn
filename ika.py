from datetime import datetime as dt

def main():
    try:
        syntymapaiva = dt.strptime(input('Anna syntymäpäivä muodossa d.m.yyyy: '), '%d.%m.%Y')
        tanaan = dt.today()

        # True, jos syntymäpäivä ei ole vielä ollut tänä vuonna
        syntymapaivaEiOllutVielaTanaVuonna = (tanaan.month, tanaan.day) < (syntymapaiva.month, syntymapaiva.day)

        # True muuttuu ykköseksi, false nollaksi
        ikaVuosissa = (tanaan.year - syntymapaiva.year - syntymapaivaEiOllutVielaTanaVuonna)
        ikaPaivissa = (tanaan - syntymapaiva).days
        
        print(f'Olet nyt {ikaVuosissa} vuotta, tarkemmin sanoen {ikaPaivissa} päivää')
    except ValueError as error:
        print('Syntymäpäivä tulee antaa muodossa d.m.yyyy == (päivä.kuukausi.vuosi)')
        print(error)

if __name__ == "__main__":
    main()