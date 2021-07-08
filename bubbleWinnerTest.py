# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest
from bubbleWinner import *


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        games = [["Bucks", "Clippers"], [
            "Clippers", "Suns"], ["Suns", "Bucks"]]
        results = [0, 0, 1]
        expected = "Suns"
        actual = bubbleWinner(games, results)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
