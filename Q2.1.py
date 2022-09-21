# Write a function such that all odd numbers come before even numbers,
# and sort the odd numbers in ascending order and even numbers in descending order.
# For example, the string '1982376455' becomes '1355798642'


"""The program gets the string, convert each character to integer and then checks whether the number is odd or even and adds to its strings.
the odd numbers are sorted in ascending order and the even numbers in descending order, finally both the stings are joined (odd+even)
output is shown"""


# odd - ascending
# even - descending
# input - 1982376455
# output - 1355798642


def sorted_string(my_string):
    '''This function sorts the odd-even values in descending-ascending order respectively and stores it in string format
    the function takes "my_string" with integers as a parameter, when called upon the function returns sorted string..'''

    even_string = ""  # initialize empty strings
    odd_string = ""

    for i in my_string:
        if int(i) % 2 == 0:       # Convert each charater to int and then checks for odd/even
            even_string += str(i)
        else:
            odd_string += str(i)

    # sorts the string in descending order
    even_string = ''.join(sorted(even_string, reverse=True))
    # sorts the string in ascending order
    odd_string = ''.join(sorted(odd_string))
    # print(even_string)
    # print(odd_string)
    new_string = odd_string + even_string

    return new_string


my_string = "1982376455"
print(sorted_string(my_string))
