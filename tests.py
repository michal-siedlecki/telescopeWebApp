import json
import unittest

from app import home, calculate, GREETING_MESSAGE


class TestGreetingMessage(unittest.TestCase):

    def test_greeting(self):
        ''' Test if home() returns expected invitation message '''
        expected_message = GREETING_MESSAGE
        message = json.loads(str(home('GET', {}).get('data')))
        self.assertEqual(message, expected_message, f"Should be \n %s" % expected_message)


class TestCalculation(unittest.TestCase):
    '''Tests if calculations are correct'''
    expected_result = {'costs': {'a': 5, 'b': 2, 'c': 9, 'd': 7, 'end': 8},
                       'parents': {'a': 'start', 'b': 'start', 'c': 'a', 'd': 'a', 'end': 'd'}}

    with open("sample_request.json", 'r') as f:
        request = json.loads(f.read())

    def test_calculate(self):
        result = calculate(self.request)
        self.assertEqual(result, str(self.expected_result), f"Should be \n %s" % self.expected_result)


if __name__ == '__main__':
    unittest.main()
