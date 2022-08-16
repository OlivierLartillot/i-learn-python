class Employe:

    def __init__(self,prenom, nom, salaire_annuel):
        self.prenom= prenom
        self.nom= nom
        self.salaire_annuel = salaire_annuel

    def give_raise(self, prime="5000"):
        try:
            salaire_augmente = int(self.salaire_annuel) +  int(prime)
        except:
            texte = "Tu ne peux pas entrer du texte pour une prime !"
            return texte
        else:
            return salaire_augmente