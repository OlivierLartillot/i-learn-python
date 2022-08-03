#----------------- Listes  -----------------------------
print(" \n\t1.Etudions les listes")
animaux_d_afrique = ['lion', 'girafe', 'eléphant','rhinocéros', 'léopard','hippopotame','chat']
print(animaux_d_afrique)
print(f"l'animal avec l index 0 est : {animaux_d_afrique[0]}")

# Insérer
print(" \n\t\t1.a.Insérer")
animaux_d_afrique.append('zèbre')
animaux_d_afrique.insert(0, 'surricate')
print('Nous ajoutons des animaux avec append et insert')
print(animaux_d_afrique)

# Supprimer
print(" \n\t\t1.b.Supprimer")
del animaux_d_afrique[0]
print ('On vient de supprimer [0] avec Del')
print(animaux_d_afrique)
animal_pop = animaux_d_afrique.pop()
print ('On vient de supprimer le dernier élément avec pop()')
print(animaux_d_afrique)
print ('je peux quand meme l utiliser !!!')
print(f'L\'animal supprimé est le : {animal_pop.upper()}')
chat = animaux_d_afrique.remove('chat')
print(f"On peut supprimer un élément en particulier par son index ou sa valeur \n\t - tableau.pop(-1) => -1 = dernier élément \n\t - tableau.remove('chat')") 
print(animaux_d_afrique)

# Organiser une liste
print(" \n\t\t1.c.Organiser")
print("Avec sorted, c'est trié temporairement")
print(sorted(animaux_d_afrique))
print("Le tableau est toujours égal à ça :")
print(animaux_d_afrique)
print("Avec sort, le changement est irréversible :")
animaux_d_afrique.sort()
print(animaux_d_afrique)
animaux_d_afrique.sort(reverse=True)
print(animaux_d_afrique)
print('Ordre inverse de la liste : définitf et pas alphabétique juste inverse les index !!!')
animaux_d_afrique.reverse()
print(animaux_d_afrique)
print("avec len(ma_liste) je sais combien d'item contient ma liste")
print(f"la liste lenght => {len(animaux_d_afrique)}")

# boucle for et indentation
print(" \n\t2.Voici une boucle for")
i = 1
for animal in animaux_d_afrique:
   print(f"{i}. {animal.title()}")
   i = i+1

# Range
for value in range(1,5):
    print (f'{value}. range')

liste = list(range(1,6))
print (f'ceci est créé avec la fonction list : {liste}')

liste = []
for value in range(1,5):
    value_x_10 = value * 10
    liste.append(value_x_10)
    print (f'la liste au fur et à mesure: {liste} ')

# min et max
print(f'les minimum et max de la liste sont :\n - {min(liste)} \n - {max(liste)}')

print('En utilisant la "compréhension de liste cela donne :')
values_x_10 = [value * 10 for value in range(1,11)]
print(values_x_10)

# tranche de liste
print(f'Les 3 premieres occurences grace a une tranche 0:3 :\n{values_x_10[0:3]}')
print(f'Les 3 premieres occurences grace a une tranche :3 :\n{values_x_10[:3]}')
print(f'Les dernieres occurences grace a une tranche 5: :\n{values_x_10[5:]}')
print(f'ou -5: :\n{values_x_10[-5:]}')

# Copier une liste
print('\tCopions la liste d\'un ami avec tranche [:] et ajoutons avec append')
pizzas_olivier = ['calzone', 'reggina']
pizzas_estelle = pizzas_olivier[:]
pizzas_estelle.append('margherita') 
print(f'Les pizza préférées d\'Olivier: \n {pizzas_olivier}')
print(f'Les pizza préférées d\'Estelle: \n {pizzas_estelle}')

# Tuples
my_tuple = (100, 200, 300)
i = 1
for item in my_tuple:
    print(f'tuple item numéro {i} : {item}')
    i = i+1

print ('on ne peut pas changer un tuple comme ceci !!! \n   my_tuple[0] = 500 => ERROR !!!')

