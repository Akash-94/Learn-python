# Given a string text, you want to use the characters of text to form as many instances of the word "cricket" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Example: text = "tlcezikcar"
# Output = 1

# text = "pekki"
# Output = 0


"""The program takes a string and uses its characters to form a word and displays max number of instances that word is formed."""

# my_result = "cricket"
# my_result = "criket"


from collections import Counter


my_input = "tlcezikcar"  # Input string
my_string = Counter(my_input)

print(min(my_string['c']//2, my_string['r'], my_string['i'],
          my_string['k'], my_string['e'], my_string['t']))  # Char should be used once hence min function is called.
