from animal import Chien 
from animal import Oiseau
# import entrainement_Animal -> entrainement_Animal.Chien("","")
 
my_dog = Chien('Pupy',8,"Dog Allemand")
print(my_dog.name)
print(my_dog.age)
print(my_dog.eats())
print(f"{my_dog.name} a {my_dog.nbre_pattes} pattes")
print(f"{my_dog.name} est un {my_dog.race}.")
print(f"Mon chien fait {my_dog.crier()}")

my_bird = Oiseau("Titi", 25, "Canari")
print(f"{my_bird.name} est un {my_bird.race}. il a {my_bird.age} ans. Il a donc {my_bird.nbre_pattes} pattes et {my_bird.nbre_ailes} ailes.")