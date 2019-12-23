# Import the unit testing package
import unittest

# Import the module to be tested
from get_data import get_data

# Define the tests
class TestGetData(unittest.TestCase):

    # Test the one digit input code cases
    def test_get_data_one_digit_non_breakcode(self):
        self.assertEqual(get_data(1, 0, [1, 2, 3, 4, 5, 6]), [2, 3, 4], "The single digit opcodes 1 or 2 data_getter "
                         "doesn't get the right data.")

    def test_get_data_one_digit_greater_than_two(self):
        self.assertEqual(get_data(3, 0, [1, 2, 3, 4, 5, 6]), [2], "The single-digit opcodes greater than two aren't "
                         "getting the right data.")

    # Test the one digit breakcode case:
    def test_get_data_one_digit_breakcode(self):
        self.assertEqual(get_data(99, 0, [1, 2, 3, 4, 5, 6]), "The data getter found a break code.", "The single digit "
                                  "breakcode handling data_getter isn't working right.")

    # Test the multi-digit non-breakcode case:
    def test_get_data_multidigit_non_breakcode(self):
        self.assertEqual(get_data([2, 0, 1, 0], 0, [1002, 4, 3, 4, 33]), [33, 3, 4], "The multi-digit non-breakcode handler "
                         "isn't working right.")

    # TODO: Add a test case for if the opcode part of the multidigit is 3 or 4 (so it'll be a 2-digit list)

    # Test the multi-digit breakcode case:
    def test_get_data_multidigit_breakcode(self):
        self.assertEqual(get_data([99, 0, 1, 0], 0, [9901, 4, 3, 4, 33]), "The data getter found a break code.",
                         "The multidigit breakcode handling data_getter isn't working right.")

if __name__ == '__main__':
    unittest.main()
