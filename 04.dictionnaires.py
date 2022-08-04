# Définitipn d'un dictionnaire

print("alien_0 = {'color': 'vert', 'points' : 5}")
alien_0 = {'color': 'vert', 'points' : 5}
print(f"La couleur de l'alien 0 est '{alien_0['color']}'")

# On ajoute des propriétés
alien_0['x_position'] = 0
alien_0['y_position'] = 25

# Comme une liste on peut déclarer le dictionnaire vide
alien_1 = {}
alien_1['color'] = 'vert'
alien_1['points'] = 25

## Supprimer clé-valeur
del alien_0['color']
print(alien_0)

## Get pour gérer les erreurs
points_actuels = alien_0.get('points','alien_0.get() me dit : Cette valeure n est pas définie') 
couleur_actuelle = alien_0.get('color','alien_0.get() me dit : Cette valeure n est pas définie') 
print(f"points : {points_actuels}")
print(f"couleur : {couleur_actuelle}")

## Ensemble (set)
langage_favori = {'jean': 'python', 'marc': 'python', 'olivier': 'php', 'stella': 'c'}
print('Un ensemble est une collection dont chaque élément doit être unique')
print('Il existe 2 manières de déclarer des ensembles')
### set
print(f'Les langages cités sont :')
for langage in set(langage_favori.values()):
    print(langage)
langages = {'python', 'python', 'php', 'c'}
print (sorted(langages))

## Imbrication


### exercices
print('\t---- Exercices d\'entrainements ----')
#### exercice 1 
user_0 = {}
user_0['prenom'] = 'Omer'
user_0['nom'] = 'Simpson'
user_0['age'] = '40'
user_0['adresse'] = '742 Evergreen Terrace, Springfield, États-Unis'

for key,value in user_0.items():
   print(f'{key} : {value}')

#### exercice 2
favorite_number = {
    'josh' : 6,
    'olivier' : 9,
    'bart' : 5
} 
liste_inscrits = []
for name in sorted(favorite_number.keys()):
    liste_inscrits.append(name)
print(f"la liste des inscrits et: \n{liste_inscrits}")

for name, number in sorted(favorite_number.items()):
    print(f"Le numéro favori de {name.title()} est le {number} ")

#### exercice 3 : fleuves et pays
fleuves = {
    'loire': 'france',
    'seine' : 'france',
    'volga': 'russie',
    'volta' : 'ghana', 
    'drina': 'serbie',
}
for fleuve, pays in fleuves.items():
    print(f"La {fleuve.title()} coule en {pays.title()}")
print("Les fleuves répertoriés :")
for fleuve in sorted(fleuves.keys()):
    print(fleuve.title())
print("Les pays présents dans la liste :")
for pays in sorted(set(fleuves.values())):
    print(pays.title())
