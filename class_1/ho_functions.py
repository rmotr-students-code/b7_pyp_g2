def string2number(a_string):
    convertions = [int, float]
    for convertion in convertions:
        try:
            return convertion(a_string)
        except ValueError:
            pass

    raise ValueError("You haven't provided a number")


import unittest


class String2NumberTestCase(unittest.TestCase):
    def test_cast_string_into_integer(self):
        self.assertEqual(string2number('2'), 2)

    def test_cast_string_into_float(self):
        self.assertEqual(string2number('2.8'), 2.8)
        
unittest.main()