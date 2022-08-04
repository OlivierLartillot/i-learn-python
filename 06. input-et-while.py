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
        
    
