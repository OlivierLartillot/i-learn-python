# Fonctions
## Bases
def greet_user(username = "olivier"):
    '''Afficher Bonjour'''
    print(f"Bonjour {username.title()}. Content de te rencontrer.")

name = input("Comment t'appelles tu ?\n")
### appels par argument
greet_user(name)
### appel argument par mot clé 
greet_user(username="Patrcik")
### appel valeur par défault
greet_user()

## Return
print("\n\tUtilisation de Return")
def full_name(firstname, lastname):
    '''retourner le nom complet'''
    full_name = f"{firstname.title()} {lastname.title()}"
    return full_name

user_full_name = full_name("Omer", "Simpson")
print(f"Bienvenue {user_full_name}") 

## Nombre arbitraire d'arguments
print("\n\tNombre arbitraire d'arguments\n")
def make_pizza(*toppings):
    print("Mon nombre d'ingrédients varie :")
    for topping in toppings:
        print(f"-{topping}")

make_pizza("pepperoni")
make_pizza("champignons", "lardons")

## Nombre arbitraire d'argments par mot-clé
print("\n\tNombre arbitraire d'argments par mot-clé\n")
def build_profile(firstName, lastName, **user_infos):
    user_infos['first_name'] = firstName.title()
    user_infos['last_name'] = lastName.title()
    return user_infos

user1 = build_profile("omer", "Simpson", particularité= "stupide") 
user2 = build_profile("Marge", "Simpson", particularité= "femme d'Omer") 
user3 = build_profile("Bart", "Simpson", taille= "1m20") 

print(user1)
print(user2)
print(user3)
