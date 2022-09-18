# Write a program which will find all such numbers which are divisible by 7
# but are not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

"""The program should get the values in the range of 2000 to 3200 
and check that number is divisible by 7 and is not a multiple of 5 (ie not divisible by 5)"""

my_list = []


for i in range(2000, 3201):
    if (i % 7 == 0) and (i % 5 != 0):
        my_list.append(str(i))


print(", ".join(my_list))
