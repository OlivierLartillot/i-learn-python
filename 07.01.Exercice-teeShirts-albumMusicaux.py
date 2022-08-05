# Exercices tee-shirt
print("\nExo tee shirt")
def make_shirt(taille="L", message="J'adore Python !"):
    '''Retourne un tee shirt adapté au client'''
    print(f"Tu as choisi un tee-shirt de taille {taille.title()}")
    print(f"Le message inscrit dessus sera:\n{message}")
make_shirt()
make_shirt(taille = "m",message="Rage against the machine !")

# Exercices albums musicaux
def make_album(artiste, titre, nbre_chansons=None):
    album = {"nom_artiste" : artiste, "titre_album": titre }
    if nbre_chansons:
        album["nombre_chansons"] = nbre_chansons
    return album

print(make_album("Jhonny","J'ai l'idée"))
print(make_album("De palme","Chansons de La plage", 43))
artiste = input("nom de l artiste\n")
album = input("nom de l album\n")
nbre_chansons = input("nbre chansons\n")
doc_album = make_album(artiste, album, nbre_chansons)

for key, value in doc_album.items():
    print(f"{key}: {value}")


