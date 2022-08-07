# Nombre d'arguments arbitraire

nom = "sebounet"
print(f"Nombre d'arguments arbitraires")

## Liste de garnitures dans un sandwich
def recap_sandwich(*ingredients):
    for ingredient in ingredients:
        print(f"-{ingredient}")

def make_sandwich():
    print("q pour terminer le sandwich")
    ingredient = True
    ingredients_pour_sandwich = []

    while ingredient != "q":
        ingredient = input("ajoute un ingrédient:\n") 
        if ingredient != "q":
            ingredients_pour_sandwich.append(ingredient)
    return ingredients_pour_sandwich

my_ingredients = make_sandwich()
recap_sandwich(my_ingredients, "salade")



## Fabrique à voiture
print("\n\t Bienvenue dans la fabrique à voiture")

def make_car(marque,modele,**voiture):
    voiture['marque'] = marque
    voiture['modele'] = modele
    return voiture
def show_cars_liste(liste):
    for cars in liste:
        print(f"\n")
        print(f"Marque : {cars['marque']} ")
        print(f"Modèle : {cars['modele']} ")

        for label,info in cars.items():
            if label != "marque" and label != "modele" :
                print(f"{label}: {info}")
        
### on défini 3 voitures 
car1 = make_car("BMW", "M5", couleur="Noire", siege="cuir")
car2 = make_car("Ferrari", "F-40", couleur="Rouge", particularité="très chère")
car3 = make_car("Dacia", "Sandero", couleur="Blanche", particularité="pas chère")

### on ajoute ces voitures à la liste
cars = [car1,car2, car3]
flag = True

### on propose a l'utilisateur d'ajouter une nouvelle voiture
###! nécessite plus de vérifications
while flag:
    new_car = input("Veux tu créer une nouvelle voiture: oui/non\n")
    if new_car == "non":
        break
    else:    
        new_marque = input("Nouvelle marque\n")
        new_modele = input("Nouveau modèle\n")
        voiture = make_car(new_marque, new_modele)
        flag_infos_supp = True
        ### on demande si tu veux ajouter des informations supplémentaires sur ce véhicule
        while flag_infos_supp:
            plus_d_infos = input("Veux tu rentrer d'autres infos sur ce véhicule ? oui/non\n")
            if plus_d_infos == "non":
                break
            else:
                ### on ajoute ces informations supplémentaires et on repart dansla boucle
                ### en demandant si tu veux ajouter des informations supplémentaires
                nouveau_label = input("entre le nom d'un label (exemple: couleur)\n")
                nouvelle_info = input(f"entre l'information : {nouveau_label}\n")
                voiture[nouveau_label] = nouvelle_info
        cars.append(voiture)

show_cars_liste(cars)

