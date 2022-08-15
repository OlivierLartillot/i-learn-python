from datetime import date


class Evenement():
    def __init__(self, name, date_evenement, heure_evenement, nombre_min, nombre_max,create_by, create_date):
        self.name = name
        self.date = date_evenement
        self.heure_evenement = heure_evenement
        self.nombre_min = nombre_min
        self.nombre_max = nombre_max
        self.create_by = create_by
        self.create_date = create_date

    def show_details(self):
        texte = f"Events = {self.name}\n"
        texte += f"Aura lieu le {self.date} a {self.heure_evenement}"
        return texte

    def get_name(self):
        return self.name
    def set_name(self, nouveauNom):
        self.name = nouveauNom
        return self.name


    
evenement_1 = Evenement("Evasion en Bateau","10/08/2022","17h00",5,20,"Olivier","09/08/2022")

print(evenement_1.show_details())
print(f"nom de l'événement = {evenement_1.get_name()}")
nouveau_nom = input("Entre le nouveau nom pour cet événement: \n")
evenement_1.set_name(nouveau_nom)
print(f"Nouveau nom de l'événement = {evenement_1.get_name()}")


