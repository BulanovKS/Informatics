import unittest
from Ex_2 import MNK

class TestEmptyLists(unittest.TestCase):
    def test_empty_X_Y(self):
        self.assertEqual(MNK([],[]), "X and Y must not be empty")

    def test_empty_X(self):
        self.assertEqual(MNK([], [1, 2, 3]), "X must not be empty")

    def test_empty_Y(self):
        self.assertEqual(MNK([1, 2, 3], []), "Y must not be empty")

class TestRepeatedValues(unittest.TestCase):
    def test_empty_X_Y(self):
        self.assertEqual(MNK([1, 1, 2], [1, 2, 3]), "X must not include repeated values")

if __name__ == "__main__":
    unittest.main()