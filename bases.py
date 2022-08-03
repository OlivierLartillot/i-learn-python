print('hello world !')

# Variables Simples en python, méthodes format et title 
first_name = 'ada'
last_name = 'lovelace'
full_name = f"{first_name} {last_name}"
print(full_name.title())

# Un peu concaténation et strip (lstrip & rstrip)
nom_personne = " olivier leleloup  "
nom_personne = nom_personne.title().strip()
message = f'Bonjour {nom_personne}! Veux tu apprendres Python ?'
print(message)

# Quelques méthodes pour le texte
nom = "faNNy"
print(f'Le nom entré par l \'utilisateur est => {nom}')
print(f'Le nom en majuscules est => {nom.upper()}')
print(f'Le nom en minuscules est => {nom.lower()}')
print(f'Le nom bien écrit est => {nom.title()}')


famous_personne = "albert Einstein"
citation = '"Sans vouloir me froisser avec les gens du sud-ouest, une chocolatine ça n\'existe pas !"'
famous_personne = famous_personne.title().strip()
citation = citation. strip()
print(f"{famous_personne} à  dit:\n\t{citation}")
