# Exercise 1: String to number
# Given a string, return the number that it represents.
# Example:
# '1234' -> 1234
def to_int(s : str) -> int:
    return 0

# Exercise 2: mean/median/mode
# Print the mean, median and mode of the length of the words in the given list.
def print_mean_median_mode(words: list) -> None:
    ()

# Exercise 3: letter histogram
# Plot a histogram graph that shows how frequent each letter is in the english language, given a list of english words.
# You can use PyPlot to do this.
def draw_letter_histogram(words: list) -> None:
    ()

# Test code: don't edit this
import unittest
import random


class TestExercises(unittest.TestCase):
    def test_exercise_1(self):
        for i in range(100):
            ri = random.randint(0, 10000)
            my_ri = to_int('{0}'.format(ri))
            self.assertEqual(my_ri, ri)

unittest.main()

words_file = open("words_alpha.txt", 'r')
words_list = words_file.readlines()
for i in range(len(words_list)):
    words_list[i] = words_list[i].rstrip()
random.shuffle(words_list)

print_mean_median_mode(words_list)
draw_letter_histogram(words_list)