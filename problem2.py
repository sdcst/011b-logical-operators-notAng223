#! python3

"""
Problem 2
Factors are positive integers that divide evenly into another integer.
The user will enter in two numbers. Determine if the smaller is a factor of the larger

You can use an if statement to determine which is larger, or use the
max() function to determine the larger of the two
(2 marks)

inputs:
an integer
an integer

outputs:
xx is a factor of yy
xx is not a factor of yy

examples:
Enter a number: 10
Enter another number: 2
2 is a factor of 10

Enter a number: 4
Enter another number: 25
4 is not a factor of 25
"""

num_1_unorderd = int(input("enther a number: "))
num_2_unorderd = int(input("enther another number: "))

num_1 = max(num_1_unorderd, num_2_unorderd)
num_2 = min(num_1_unorderd, num_2_unorderd)

is_divisable = num_1%num_2==0
if is_divisable:
    print(str(num_2)+" is a factor of "+str(num_1)+"!!!")
else:
    print(str(num_2)+" is NOT a factor of "+str(num_1))


