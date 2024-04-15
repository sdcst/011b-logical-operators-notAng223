#! python3
"""
Ask the user to enter a number. 
Tell them if the number is a positive integer
(2 points) 

inputs:
a number of any type

outputs:
xx is a positive integer.
xx is not a positive integer

example:
Enter a number: -3
-3 is not a positive integer

Enter a number: 2.4
2.4 is not a positive integer

Enter a number: 5
5 is a positive integer

Enter a number: 4.0
4.0 is a positive integer
"""

number = float(input("enter a number: "))

is_positave_bool = number>0
is_int_boot = float(int(number))==number

if is_positave_bool and is_int_boot:
    print("is a positave interger!")
else:
    print("NOT a postive interger")