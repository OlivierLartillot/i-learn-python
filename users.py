'''
    Ensemble de Classe dcrivant les utilsateurs
'''
class User():
    def __init__(self, first_name, last_name, pseudo, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.pseudo = pseudo
        self.email = email
        self.password = password
        self.login_attempts = 0
        self.mes_privileges = Privileges("user") 

    def describe_user(self):
        '''Récupère Prénom Nom de l'utilisateur'''
        texte = f"{self.first_name.title()} {self.last_name.title()}"
        return texte

    def greet_user(self):
        '''Dis bonjour à Prénom Nom de l'utilisateur'''
        texte = f"Bienvenue sur my site .com {self.describe_user()}"
        return texte
    
    def increment_login_attempts(self):
        '''Augmente de 1 l'attribut login_attempts a chaque essai de connexion'''
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        '''réinitialise le login_attempts à 0'''
        self.login_attempts = 0


class Admin(User):

    def __init__(self, first_name, last_name, pseudo, email, password):
        super().__init__(first_name, last_name, pseudo, email, password)
        self.mes_privileges = Privileges("admin") 
    

class Privileges:
    def __init__(self, role):
        if role.lower() == "admin":
            self.privileges = ["peut ajouter des posts", "peut supprimer des posts", "peut bannir des utilisateurs"]
        else:
            self.privileges = ["tu as le droit de te taire", "tu as le droit de rien dire"]
        
    
    def show_privileges(self):
        '''Montre nous tes privilèges'''
        texte = ""
        for droit in self.privileges:
            texte += f"\t-{droit}\n"
        return texte

