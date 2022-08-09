'''
Voici le programme qui importe les classes User et Admin
'''

from users import User, Admin

new_user = User("Omer","Simpson","OSimp34","Omer@mail.com","simpson1234")
print(new_user.greet_user())
print(f"tu as essayé de te connecter {new_user.login_attempts} fois")
new_user.increment_login_attempts()
print(f"tu as essayé de te connecter {new_user.login_attempts} fois")
new_user.increment_login_attempts()
print(f"tu as essayé de te connecter {new_user.login_attempts} fois")
new_user.increment_login_attempts()
print(f"tu as essayé de te connecter {new_user.login_attempts} fois")
print(f"cette fois c est la bonne je vais te réinitialiser ")
new_user.reset_login_attempts()
print(f"Ton compteur d'essai est à nouveau à {new_user.login_attempts} fois")

new_admin = Admin("Laurent","Outan","Louou","louou@mail.com","123456cestPasTresSecure")
print(f"Bonjour {new_admin.pseudo}. Tu es Admin.\nJe vais te lire tes droits:")
print(new_admin.mes_privileges.show_privileges())

print(f"Bonjour {new_user.pseudo}. Tu es User.\nJe vais te lire tes droits:")
print(new_user.mes_privileges.show_privileges())









