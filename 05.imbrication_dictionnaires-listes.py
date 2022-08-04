#Imbrications

## Liste d'aliens (disctionnaires dans une liste)
alien_0 = {'color': 'vert', 'points': 5}
alien_1 = {'color': 'vert', 'points': 5}
alien_2 = {'color': 'vert', 'points': 5}
aliens = [alien_0, alien_1, alien_2]
print(aliens[0])
print('Je vais maintenant créer 30 aliens')
aliens = []

### je définis 30 aliens identiques
for aliens_number in range(30):
    alien = {'color': 'vert', 'points': 5, 'speed' : 'lente'}
    aliens.append(alien)
print(f"Le nombre d'aliens est de {len(aliens)}")
print('Je veux modifier les 3 premiers')

### je récupère les 3 premiers verts 0,1,2 et change leur propriétés
for alien in aliens[:3]:
    if alien['color'] == 'vert':
        alien['color'] = 'jaune'
        alien['points'] = 10
        alien['speed'] = 'moyenne'
### j'affiche les 5 premiers pour m'assurer des changements
for alien in aliens[:5]:
    print(alien)

## Listes dans un dictionnaire
langage_favori = {
    'jean': ['python', 'go'],
     'marc': ['python', 'php'],
     'olivier': ['ruby', 'go'],
     'stella': ['c'],
    }
for name, langages in langage_favori.items():
    if len(langages) > 1:
        print(f"Les langages favoris de {name} sont :")
        for langage in langages:
            print(f"\t- {langage}")
    else:
        print(f"Le langage favoris de {name} est : {langages[0]}")

## Dictionnaire dans un dictionnaire
users = {
    'aeinstein': {
        'firstname' : 'albert', 
        'lastname' : 'einstein',
        'location' : 'princeton',
    },
    'mcurie': {
        'firstname' : 'marie', 
        'lastname' : 'curie',
        'location' : 'paris',
    },
}
for user, user_info in users.items():
    print(f"Nom d'Utilisateur : {user}")
    full_name = f"{user_info['firstname'].title()} {user_info['lastname'].title()}"
    print(f"Nom Complet: {full_name}")
    print(f"Lieu: {user_info['location'].title()}")

## Exercices

### Exercice 1: Affiche les infos des personnes
users = {
    'omerSimp34' : {
        'prenom': 'omer',
        'nom': 'simpson',
        'age': 40,
        'adresse': '742 Evergreen Terrace, Springfield, États-Unis'
    },
    'margeSimp' : {
        'prenom': 'marge',
        'nom': 'simpson',
        'age': 40,
        'adresse': '742 Evergreen Terrace, Springfield, États-Unis'
    },
}
for user, infos_user in users.items():
    print(f"\nVoici les infos de {user}")
    for label,info in infos_user.items():
        if label == 'prenom' or label == 'nom' : 
            info = info.title()
        print(f"\t-{label}: {info}")

### Exercice 2: dico animaux dans une liste
animal_0 = {'prenom':'marie', 'type': 'chat', 'proprietaire': 'dysney'}
animal_1 = {'prenom':'clochard', 'type': 'chien', 'proprietaire': 'dysney'}
animal_2 = {'prenom':'balou', 'type': 'ours', 'proprietaire': 'mowgli'}
pets = [animal_0,animal_1,animal_2]

i = 1
for animal in pets:
    print(f"\nVoici l'animal numéro {i}")
    for key,value in animal.items():
        print(f"{key}: {value}")
    i += 1

