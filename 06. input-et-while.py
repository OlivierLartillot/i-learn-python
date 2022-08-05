from operator import truediv


age = input('Quel age as tu ?')
flag = False

while flag == False: 
    try:
        int(age)
        it_is = True
    except ValueError:
        it_is = False

    if it_is == True:
        statut = "mineur"
        age = int(age)
        if age >= 18:
            statut = "majeur"
        print(f"Tu as {age} ans, tu es {statut}.")
        flag == True
        break
    else:
        age = input('Tu dois entrer un chiffre !\nQuel age as tu ?')
        
    
## Exercices

###Exercice 1 ajoute des ingrédients (modifié ++)

name = input('\nComment t appeles tu ?')
ingredients_en_stock = ['cornichons', 'poivrons', 'tomates', 'oignons', 'champignons', 'saumon', 'olives']
dico_aide = {
    "terminer" : "terminer: Pour envoyer votre commande",
    "liste" : "liste: Pour voir la liste des ingrédients disponible"
}
print(f'Bonjour {name.title()}.\n\n Voici la liste des ingrédients disponibles:\n {ingredients_en_stock}\n')
liste_ingredients = []
liste_pizzas = []
flag = True

while flag == True:
    if liste_ingredients:
        print(f'Les ingérdients choisis : {liste_ingredients}')
    ingredient = input("Quel ingrédient veux tu ajouter ?\n\tplus de commandes: aide\n")
    ingredient = ingredient.lower()
    if ingredient == 'terminer':
        # enregistrer la pizza dans une liste
        
        liste_pizzas.append(liste_ingredients)
        liste_ingredients = []
        # demander si l'on veut une autre pizza
        other_pizza = input('Veux tu une autre pizza ? oui/non\n')
        other_pizza = other_pizza.lower()
        ## si oui => continue
        if other_pizza == 'oui':
            continue
        ## si non on sort de la boucle
        else:
            flag = False 
    elif ingredient == 'aide':
        for label,texte in dico_aide.items():
            print(f'\t-{texte}')
        continue
    elif ingredient == 'liste':
        print(f"Voici les ingrédients en stock:\n{ingredients_en_stock}")
    elif ingredient not in ingredients_en_stock:
        print(f"\tDésolé ! L'ingredients {ingredient} n'existe pas dans nos stock")
        continue
    else:
        liste_ingredients.append(ingredient)

print(f'{name.title()}, tu as choisi :')
for pizza in liste_pizzas:
    print(f'- {pizza}')
print('Ta commande sera prête dans 5 minutes !')  

