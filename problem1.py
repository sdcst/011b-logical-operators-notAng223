#! python3
 
"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue

Enter a number: 36
36 is frue

Enter a number: 16
16 is not frue
"""

number = int(input("enter a interger: "))

is_8_div = number%8==0
is_6_div = number%6==0

if is_6_div and (not is_8_div):
    print("NUMBER IS FRUE!!!")
else:
    print("NOT FRUE!!!!")

