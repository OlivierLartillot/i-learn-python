# Importer des modules

## On peut importer des modules de plusieurs façon
print("Un exemple simple d'utilisation : on importe tout le module et on y accède grace au point\n\timport user\n\tprint(user.user_fullname('omer', 'simpson'))")
print("on importe la fonction (exemple avec alias)\n\tfrom user import user_fullname as fn\n\tprint(fn('omer', 'simpson'))")
print("autre Façon de faire\n\timport user as u => u.user_fullname\n\tfrom user import * (on imorte tout avec *)")

## Exemples d'imports
from user import user_fullname as fn
from user import greet_user as gu
from user import user_age

### la fonction qui retourne Prenom Nom
full_name = fn('omer', 'simpson')
### la fonction qui dit bonjour a [argument="full_name"]
gu(full_name)
print(user_age(40))

