# Ccndition simple

car = "Ferrari"

if car.lower() == "ferrari":
    print(f'Votre voiture de rêve est une : {car.title()}')

print ('Liste des marques de voitures en magasins :')
cars = ['audi', 'bmw', 'toyota', 'peugeot', 'renault']
#cars = []
if cars:
    cars.sort()
    for car in cars:
        if car == 'bmw':
            print(car.upper())
        else:
            print(car.title())
else:
    print("Il n'y a pas de voitures dans cet entrepot")

print('Utilisation de in (array)')
marque = 'Audi'
if marque.lower() in cars:
    print(f"{marque} est bien dans la liste de nos voitures")

print('Utilisation de not in (array)')
marque = 'Lamborghini'
if marque.lower() not in cars:
    print(f"{marque} n'est pas dans la liste de nos voitures")

print('Tests avec elif')
age = 15
if age < 11:
    statut = 'enfant'
elif age < 18:
    statut = 'ado'
else:
    statut = 'adulte'
print(f'{age} ans ! Tu es un {statut}')


marques_rechechees = ['ferrari','peugeot', 'toyota']

for marque in marques_rechechees:
    if marque in cars:
        print(f"La marque {marque} que tu recherches es bien présente chez nous")
    else:
        print(f"Nous n'avons pas la marque {marque} que tu recherches chez nous")