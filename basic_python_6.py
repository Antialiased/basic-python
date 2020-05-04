# Exercise 1: number to string
# Given a number, return a string that represents that number in decimal.
# You can use the chr() function to turn an integer to a character.
# Example:
# 1234 -> '1234'
def to_decimal_string(i : int) -> str:
    return ""

# Exercise 2: number to binary string
# Given a number, return a string that represents that number in binary.
# You can read about binary numbers here: https://www.purplemath.com/modules/numbbase.htm
# Example:
# 1234 -> '10011010010'
def to_binary_string(i : int) -> str:
    return ""
    
# Exercise 3: number to hexadecimal string
# Given a number, return a string that represents that number in hexadecimal.
# You can read about hexadecimal here: https://www.purplemath.com/modules/numbbase3.htm
# Example:
# 1234 -> '4D2'
def to_hex_string(i : int) -> str:
    return ""

# Test code: don't edit this

import random
import unittest

class TestExercises(unittest.TestCase):
    def test_exercise_1(self):
        for i in range(100):
            ri = random.randint(0, 10000)
            s = to_decimal_string(ri)
            self.assertEqual(s, '{0}'.format(ri))

    def test_exercise_2(self):
        for i in range(100):
            ri = random.randint(0, 10000)
            s = to_binary_string(ri)
            self.assertEqual(s, '{0:b}'.format(ri))

    def test_exercise_3(self):
        for i in range(100):
            ri = random.randint(0, 10000)
            s = to_hex_string(ri)
            self.assertEqual(s, '{0:x}'.format(ri))



unittest.main()