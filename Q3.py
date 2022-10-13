# Given a string text, you want to use the characters of text to form as many instances of the word "cricket" as possible.
# You can use each character in text at most once. Return the maximum number of instances that can be formed.

# Example: text = "tlcezikcar"
# Output = 1

# text = "pekki"
# Output = 0


"""The program takes a string and uses its characters to form a word and displays max number of instances that word is formed."""

# my_result = "cricket"
# my_result = "criket"


my_text = "tlcezikcar"   # Input string

c = 0                    # Initialize the the characters of the string to a int value and conider it as a counter for each character
r = 0
i = 0
k = 0
e = 0
t = 0


for p in my_text:
    if p == "c":
        c += 1
    elif p == "r":
        r += 1
    elif p == "i":
        i += 1
    elif p == "k":
        k += 1
    elif p == "e":
        e += 1
    elif p == "t":
        t += 1

# Char should be used once hence min function is called.
my_result = min(c//2, r, i, k, e, t)

print(my_result)
