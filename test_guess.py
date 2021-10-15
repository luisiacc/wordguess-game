import unittest
from guess import Guesser


class TestMain(unittest.TestCase):
    my_list = ['balance', 'balanceado', 'boralence', 'bala', 'bol']
    letters1 = 'aabecnl'

    def test_regular_output(self):
        """Should give words with all letters in"""
        self.assertEqual(Guesser(self.letters1, self.my_list).get_matches(), self.my_list[:3])

    def test_with_maximun_lenght_achieved(self):
        """ Should give words with maximun length"""
        self.assertEqual(Guesser(self.letters1, self.my_list, max_len=7).get_matches(), ['balance'])

    def test_minimal_matches_in_word(self):
        """Shoudl give words with at least the minimal matches especified"""
        self.assertEqual(Guesser(self.letters1, self.my_list, min_matches=2).get_matches(), self.my_list)


if __name__ == '__main__':
    unittest.main()