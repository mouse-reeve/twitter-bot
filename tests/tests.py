''' test language creation '''
from bot import generator
import unittest

class Tests(unittest.TestCase):
    ''' my tests are as comprehensive as a ... '''

    def test_tweet_structure(self):
        ''' check if a valid data object is created '''
        data = generator.get_tweet()

        self.assertIn('status', data)


if __name__ == '__main__':
    unittest.main()
