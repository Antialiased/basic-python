# Exercise 1: Given a list of all english words, print the longest word.
def print_longest_word(english_words):
    ()

# ======================================================

# Exercise 2: Given a list of all english words, print all the palindromes.
# A palindrome is a word that read the same forwards and backwards,
# such as 'abba' or 'sees'
def print_palindromes(english_words):
    ()

# ======================================================

# Exercise 3: Spellchecker. Given a list of all english words and a test word, return whether
# the test word is in English or not (i.e whether the test word appears in the list).

def is_in_english_dictionary(english_words, test_word):
    ()


# Test code: don't edit this

import random
words_file = open("words_alpha.txt", 'r')
words_list = words_file.readlines()
for i in range(len(words_list)):
    words_list[i] = words_list[i].rstrip()
random.shuffle(words_list)
print_longest_word(words_list)
print_palindromes(words_list)

import unittest

class TestExercises(unittest.TestCase):
    def test_exercise_3(self):
        self.assertTrue(is_in_english_dictionary(words_list), 'apple')
        self.assertTrue(is_in_english_dictionary(words_list), 'plump')
        self.assertFalse(is_in_english_dictionary(words_list), 'dapwok')
        self.assertFalse(is_in_english_dictionary(words_list), '235')

unittest.main()