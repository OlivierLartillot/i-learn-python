import unittest

from functions.city_functions import get_city_country

class CityCountryTestCase(unittest.TestCase):
    
    def test_city_country(self):
        '''test avec des noms'''
        formatted_city_country = get_city_country('monTPellier','fRance')
        self.assertEqual(formatted_city_country, 'Montpellier, France')
    def test_city_country_population(self):
        '''test avec des noms'''
        formatted_city_country = get_city_country('monTPellier','fRance',250000)
        self.assertEqual(formatted_city_country, 'Montpellier, France - population: 250000')


if __name__ == '__main__':
    unittest.main()