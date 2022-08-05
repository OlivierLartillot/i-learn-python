# Tickets de cinéma
tarifs = {
    "tarif_0": 0 ,
    "tarif_1": 10 ,
    "tarif_2": 15,
}

nbre = input("Combien etes vous de personnes ?")
noms = []
#traite le résultat entré pour s'assurer que c est bien un nombre/chiffre
nbre = int(nbre)
i = 1
# récupère le nom des personnes
while i <= nbre:
    nom = input(f"Quel est le nom de la personne n° {i}\n")
    noms.append(nom)
    i += 1 
    
i=1
personnes = []
# récupère l'age des personnes
while i <= len(noms):
    age = input(f"Quel est l'age de {noms[i-1].title()}\n")
    age = int(age)
    personne = {"nom": noms[i-1], "age": age}
    personnes.append(personne)
    i += 1
somme = []
# annonce le prix pour chaque personne
for personne in personnes:
    tarif = 0
    if personne["age"] < 3:
        tarif = tarifs["tarif_0"]
    elif personne["age"] < 13:
        tarif = tarifs["tarif_1"]
    else:
        tarif = 15
    somme.append(tarif) 
    print(f" -{personne['nom'].title()}: {tarif} euros")

print(f"\t Tu dois {sum(somme)} euros")

# annonce le prix total