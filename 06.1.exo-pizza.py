# Commande de pizza / pizze

name = input('\nComment t appeles tu ?')
ingredients_en_stock = ['cornichons', 'poivrons', 'tomates', 'oignons', 'champignons', 'saumon', 'olives']
dico_aide = {
    "liste" : "liste: Pour voir la liste des ingrédients disponible",
    "terminer" : "terminer: Pour envoyer votre commande ou choisir une autre pizza",
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
        flag_terminer = False
        while flag_terminer == False:
            if other_pizza == 'oui':
                flag_terminer = True
                continue
            ## si non on sort de la boucle
            elif other_pizza == 'non':
                flag_terminer = True
                flag = False 
            else:
                other_pizza = input('Tu dois répondre à cette question:\nVeux tu une autre pizza ? oui/non\n')
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

attente_par_pizza = 5
nombre_pizze = len(liste_pizzas)
temps_attente_estime = attente_par_pizza * nombre_pizze
print(f'{name.title()}, tu as choisi :')
for pizza in liste_pizzas:
    print(f'- {pizza}')
print(f'Ta commande sera prête dans {temps_attente_estime} minutes !')  

