import json

flag = True
pseudo = input("Veuillez choisir votre pseudo:\n")

while flag == True:
    mot_de_passe = input("Veuillez choisir votre mot de passe:\n")
    user = [pseudo, mot_de_passe]

    try:
        with open(f"./json/{pseudo}.json") as f:
            content = json.load(f)        
    except FileNotFoundError:
        with open (f"./json/{pseudo}.json","w") as f:
            json.dump(user,f)
            print("Vous venez de vous inscrire. Vous pouvez maintenant vous connecter.")
            break
    else:
        if mot_de_passe == content[1]:
            print(f"Content de te revoir {pseudo}")
            flag = False
        else :
            print("Refaisons un tour de boucle pour que tu retentes ta chance de mot de passes")   


