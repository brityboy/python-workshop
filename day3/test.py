import unittest
from lecture import foo

class ScratchTests(unittest.TestCase):
    def test_foo(self):
        expected = 7
        result = foo(6)
        self.assertEqual(expected, result)
