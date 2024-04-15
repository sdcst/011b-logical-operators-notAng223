#! python3
# Task2.py

"""
Ask the user to enter a number.
Tell them if the number is both a perfect square and divisible by 2.

Note:  Many languages have a problem when dealing with floating point
decimals, and python is no exception.
Sometimes, when finding the cube root of large numbers, like 729,
you may get 8.9999999999999999999998 instead of 9
To get around this, we can use the round() command
round() accepts 2 parameters, the number to be rounded, and how many decimals
a = round(3.999999999999998, 8) would round at the 8th decimal place, for example.
You don't want to round too early (ie to the nearest whole number) because that
might be too inaccurate.
(2 points) 

Inputs:
number

Outputs:
xx is both a perfect square and a divisible by 2.
xx is only a perfect square.
xx is only divisible by 2.

Example:
Enter a number: 8
8 is only divisible by 2.

Enter a number: 64
64 is both a perfect square and divisible by 2.
"""
round_off_const=0.001
number = float(input("enter a number: "))


is_square = abs(int(number**0.5)-number**0.5)<round_off_const
# divisable by 2 AND a interger
is_divisable = (int(number)%2==0) and (abs(float(int(number))-number)<round_off_const)

if is_square and is_divisable:
    print("divisable by 2 and a perfect square")
elif is_divisable:
    print("is divisable by 2, not a perfect square")
elif is_square:
    print("a perfect square, but not divisable by 2")
else:
    print("neither a perfact square or divisable by 2")
