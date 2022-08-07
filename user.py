'''module de fonction user'''
def user_fullname(first, last):
    '''renvoie => Prénom Nom'''
    full_name = f'{first.title()} {last.title()}'
    return full_name

def user_age(age):
    '''phrase de présentation de l'age'''
    texte = f'Tu as {age} ans !'
    return texte

def greet_user(fullname):
    '''print le texte de bienvenue personnalisé'''
    texte = print(f"Bonjour et bienvenue {fullname}")
    return texte