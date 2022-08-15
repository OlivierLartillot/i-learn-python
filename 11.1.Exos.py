# Exos 1: Exception nombre + texte
number_1 = input("Veuillez entrer le nombre 1 à additionner:\n")
number_2 = input("Veuillez entrer le nombre 2 à additionner:\n")
try:
    number_1 = int(number_1)
    number_2 = int(number_2)
except:
    print("Désolé mais nous ne savons pas additionner des chiffres et des lettres...")
else:
    total = number_1 + number_2
    print(f"Le total de votre addition est égal à {total}")

# Exos 2: Exception avec boucle while
flag = True

while flag == True:
    number_1 = input("Veuillez entrer le nombre 1 à additionner:\n")
    number_2 = input("Veuillez entrer le nombre 2 à additionner:\n")
    try:
        number_1 = int(number_1)
        number_2 = int(number_2)
    except:
        print("Désolé mais nous ne savons pas additionner des chiffres et des lettres...")
    else:
        total = number_1 + number_2
        print(f"Le total de votre addition est égal à {total}")   
        flag = False