import unittest

from functions.name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    
    def test_first_last_name(self):
        '''test avec des noms'''
        formatted_name = get_formatted_name('omer','simpson')
        self.assertEqual(formatted_name, 'Omer Simpson')
    def test_first_middle_last_name(self):
        '''test avec des noms'''
        formatted_name = get_formatted_name('wolfgang','mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()