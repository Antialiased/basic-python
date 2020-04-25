# Exercise 1: sum13
# Write a function that returns the sum of the numbers in the array, 
# returning 0 for an empty array. Except the number 13 is very unlucky,
# so it does not count and numbers that come immediately after a 13 also do not count.
# sum13([1, 2, 2, 1]) = 6
# sum13([1, 1]) = 2
# sum13([1, 2, 2, 1, 13]) = 6

# Write your function here:
def sum13(nums):
    return 0

# ======================================================

# Exercise 2: Factorial
# Write a function that when given a number, returns its factorial.
# The factorial n! of a number n is the product of all positive integers less than or equal to n:
# n! = n * (n-1) * (n-2)  * ... * 3 * 2 * 1
# Note: python has a function for doing factorials but don't use it!

# Write your function here:
def factorial(num):
    return 0

# ======================================================

# Test code: don't edit this
import math
import unittest

class TestExercises(unittest.TestCase):
    def test_exercise_1(self):
        for i in range(12):
            self.assertEqual(factorial(i), math.factorial(i))

    def test_exercise_2(self):
        self.assertEqual(sum13([1,2,2,1]), 6)
        self.assertEqual(sum13([1,1]), 2)
        self.assertEqual(sum13([1,2,2,1,13]), 6)
        self.assertEqual(sum13([1,2,2,1,13, 145]), 6)

unittest.main()