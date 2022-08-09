# Exercice d'entrainement
# Les animaux du zoo
'''
Ensemble de classes servant à décrire ou faire exécuter des actions
à des animaux classés par mamifere et oiseaux
'''
import random

class Animal:
    '''On modélise un animal'''
    ##Un constructeur
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eats(self):
        '''un animal qui mange'''
        texte = f"{self.name} est entrain de manger"
        return texte

    def sleeps(self):
        '''Un animal qui dort'''
        texte = f"zzz, zzzz, {self.name} est entrain de dormir"
        return texte


class Mamifere(Animal):
    '''On modélise un mamifère, héritier d'animal (Animal->Mamifere)'''
    def __init__(self, name, age):
        super(). __init__(name, age)
        self.nbre_pattes = 4
        self.type = type


class Oiseau(Animal):
    '''On modélise un oiseau, héritier d'animal (Animal->Oiseau)'''
    def __init__(self, name, age, race):
        super(). __init__(name, age)
        self.nbre_pattes = 2
        self.nbre_ailes = 2
        self.type = type
        self.race = race
    def crier(self):
        texte = f"{self.name} est entrain de faire Cuicui"
        return texte


class Chien(Mamifere):
    ''''Un Chien est une classe fille de mamifère (Animal->Mamifere->Chien)'''
    def __init__(self, name, age,race):
        super(). __init__(name, age)
        self.type = "chien"    
        self.race = race   
        # Une liste d'abboiements pour varier les plaisirs
        self.cri = ["waf waf","wouf wouf", "wouf waf"]
    
    def crier(self):
        '''Un chien varie les abboiements ! Sauf les dogs allemands...'''
        if self.race.lower() == "dog allemand":
            abboiement = self.cri[1]
        else:
            dernier_index = len(self.cri)-1
            index_abboiement = random.randint(0,dernier_index)
            abboiement = self.cri[index_abboiement]

        texte = f"{self.name} est entrain de faire {abboiement}"
        return texte







