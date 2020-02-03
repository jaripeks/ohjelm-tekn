import datetime

syntynyt = int(input('Anna syntymävuotesi: '))
nyt = datetime.datetime.now().year

#olettaa että syntymäpäivä on jo tältä vuodelta mennyt/menossa
print(f'Olet nyt {nyt - syntynyt} vuotta.')
print(f'Täytät sata vuotta vuonna {syntynyt + 100}')