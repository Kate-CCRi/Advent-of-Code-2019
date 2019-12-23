# import the unit testing package
import unittest

# from the get_opcodes file, import the get_opcodes method
from get_opcodes import get_opcodes


class TestGetOpcodes(unittest.TestCase):

    # Test the "single digit parameter length" case
    def test_get_opcodes_single(self):
        self.assertEqual(get_opcodes(1), 1, "A list with a single integer in it is not being processed correctly.")

    # Test the "5-digit with all positions filled" case
    def test_get_opcodes_multiple(self):
        self.assertEqual(get_opcodes(12345), [5, 4, 3, 2, 1], "A list of five integers in it is not being "
                                                                        "processed correctly.")

    # Test the " 1 < x < 5 digit case with zeros filled in for the missing digits" case
    def test_get_opcodes_zero_fill(self):
        self.assertEqual(get_opcodes(1002), [2, 0, 1, 0], "A list that requires zero-filling is not being "
                                                               "processed correctly.")

if __name__ == '__main__':
    unittest.main()
