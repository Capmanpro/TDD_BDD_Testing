from unittest import TestCase, main
from prakt3 import *


class prakt3Test(TestCase):
    def test_desk(self):
        self.assertEqual(mytictactoe([1, 2, 3, 4, 5, 6, 7, 8, 9]), None)

    def test_victory(self):
        self.assertTrue(check_Victory({'X': [1, 3, 5, 7, 9], 'O': [2, 4, 6]}, 'X'))
        self.assertTrue(check_Victory({'X': [3, 1, 2], 'O': [2, 4, 6]}, 'X'))

    def test_tie(self):
        self.assertTrue(check_Tie({'X': [3, 1, 9, 5, 7], 'O': [2, 4, 6, 8]}))

    def test_change(self):
        self.assertEqual(change_players('X'), 'O')
        self.assertEqual(change_players('O'), 'X')

if __name__ == '__main__':
    main()
