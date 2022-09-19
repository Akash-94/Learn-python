# Write a function such that all odd numbers come before even numbers,
# and sort the odd numbers in ascending order and even numbers in descending order.
# For example, the string '1982376455' becomes '1355798642'

"""The program first gets the integers checks whether the number is odd or even and adds to its respective lists
the odd numbers are sorted in ascending order and the even numbers in descending order, finally both the lists are joined (odd+even)
output is shown"""


def sorted_list(my_list):
    '''This function sorts the odd-even values in descending-ascending order respectively.'''

    even_list = []  # initialize empty list
    odd_list = []

    for i in (my_list):
        if i % 2 == 0:
            even_list.append(str(i))
            even_list.sort(reverse=True)  # sort values in descending order
        else:
            odd_list.append(str(i))
            odd_list.sort()  # sort values in ascending order

        # get's a new list in odd-even format
        new_list = "".join(odd_list + even_list)

    return new_list


my_list = [1, 9, 8, 2, 3, 7, 6, 4, 5, 5]
print(sorted_list(my_list))
# print(type(new_list))
