import unittest
from app import calculate

expected_result = {'costs': {'a': 5, 'b': 2, 'c': 9, 'd': 7, 'end': 8},
                   'parents': {'a': 'start', 'b': 'start', 'c': 'a', 'd': 'a', 'end': 'd'}}



class TestCalculation(unittest.TestCase):

    def test_calculate(self):
        result = calculate(request)
        self.assertEqual(result, str(expected_result), f"Should be \n %s" % expected_result)


if __name__ == '__main__':
    unittest.main()
