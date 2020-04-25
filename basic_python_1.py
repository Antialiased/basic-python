# Exercise 1: FizzBuzz
# Write a function that, when given a number, does the following:
# - If the number is divisible by 3, print 'Fizz'.
# - If the number is divisible by 5, print 'Buzz'.
# - If the number is divisible by both 3 and 5, print 'FizzBuzz'
# - If it is not divisible by either 3 or 5, print the number.
# Expected output:
# 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16

# Write your function here:
def fizz_buzz(num):
    ()

# ======================================================

# Exercise 2: Prime Numbers
# Write a function that, when given a list of numbers, prints all the numbers that are prime.
# (A prime number can only be divided evenly by itself or 1)

# Write your function here:
def print_primes(nums):
    ()

# ======================================================

# Exercise 3: Sum of Primes
# Write a function that, when given a list of numbers, 
# prints the *sum* of all the numbers that are prime.
# (hint: you can re-use the code you wrote in exercise 2 by moving it into a separate function)
# like 'def is_prime(num)' that returns a bool saying whether a single number is prime or not.

# Write your function here:
def print_sum_of_primes(nums):
    ()

# ======================================================

# Test code: don't edit this
print("Testing Exercise 1:")
for i in range(1, 32):
    fizz_buzz(i)
print('==================================================')
print("Testing Exercise 2:")
import random
random.seed(123)
random_nums = list()
for i in range(100):
    random_nums.append(random.randint(2, 30))
print_primes(random_nums)
print('==================================================')

print("Testing Exercise 3:")
print_sum_of_primes(random_nums)
print('==================================================')
