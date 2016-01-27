import unittest
from mathx.super_sum import super_sum

class SuperSumTest(unittest.TestCase):
    def test_two_numbers(self):
        result = super_sum(20, 20)
        self.assertEqual(result, 40)
