#On définit une classe chien

'''Comme  dans bcp de lanages, on met une MAJUSCULE à notre Classe'''

class Dog:
    '''On modélise un chien'''
    ##Un constructeur
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eats(self):
        '''un chien qui mange'''
        print(f"{self.name} est entrain de manger")
    
    def sit(self):
        '''un chien qui est assis'''
        print(f"{self.name} est assis")


new_dog_0 = Dog('Beethoven', 8)
new_dog_1 = Dog('Crusti', 2)


print(f"\nbienvenue {new_dog_0.name}. Tu es un gentil chien de {new_dog_0.age} ans")
print(f"Qu'est ce qu'est entrain de faire {new_dog_0.name} ?")
new_dog_0.eats()
print("\n")
print(f"bienvenue {new_dog_1.name}. Tu es un gentil chien de {new_dog_1.age} ans")
print(f"Qu'est ce qu'est entrain de faire {new_dog_1.name} ?")
new_dog_1.sit()

while True:
    ajouter_chien = input("Veux tu ajouter un chien ? oui/non\n")
    if ajouter_chien.lower() == 'oui':
        dog_is_added = True
        nom_chien = input("Comment s'appelle ce chien ? \n")
        age_chien = input(f"Quel âge à {nom_chien}?\n")
        break
    elif ajouter_chien.lower() == 'non':
        dog_is_added = False
        break
    else:
        continue
if dog_is_added:
    new_dog_3 = Dog(nom_chien,age_chien)
    print(f"Bienvenue {new_dog_3.name}. Tu es un gentil chien de {new_dog_3.age} ans")
    print(f"Qu'est ce qu'est entrain de faire {new_dog_3.name} ?")
    new_dog_3.eats()
else:
    print("Tu n'as pas ajouté de chien")

    



    
        