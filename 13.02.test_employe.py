import unittest

from employe import Employe

class TestEmploye(unittest.TestCase):
    
    def setUp(self):
        '''créer une instance d'"Employe"'''
        self.salaire = 5000
        self.salaire = int(self.salaire)
        self.employe = Employe('Omer','Simpson',self.salaire)

    def test_prime_defaut(self):
        '''test give_raise sans argument'''
        prime_defaut = 5000
        prime = self.employe.give_raise()
        self.assertEqual(prime, self.salaire + prime_defaut)
        print(f'salaire({self.salaire}) avec prime de base ({prime_defaut}): {prime}')
    
    def test_prime_personnalise(self):
        '''test give_raise avec argument'''
        prime_perso_method = "10000"
        prime_perso_test= int(prime_perso_method)
        prime = self.employe.give_raise(prime_perso_method)
        self.assertEqual(prime, self.salaire + prime_perso_test)
        print(f'salaire({self.salaire}) avec prime de {prime_perso_test}: {prime}')

    def test_prime_personnalise_texte(self):
        '''test give_raise avec argument interdit'''
        prime_perso_method = "Blabla"
        prime = self.employe.give_raise(prime_perso_method)
        self.assertEqual(prime, "Tu ne peux pas entrer du texte pour une prime !")
        print(prime)

if __name__ == '__main__':
    print('Voici les retours des tests: ')
    unittest.main()