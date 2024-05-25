import unittest
from multiply import multiply_3_numbers


class TestMultipy(unittest.TestCase):

    def test_1_(self):
        result = multiply_3_numbers(2, 4, 6)
        self.assertEqual(result, 40)

    def test_2(self):
        result = multiply_3_numbers(10000, 5, 200)
        self.assertEqual(result, 143500)


if __name__ == "__main__":
    unittest.main()
