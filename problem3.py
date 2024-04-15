#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 

You can use max() to help you find the largest number
You can use min() to help you find the smallest number
How can we find the middle number though?
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""

num_1_unorderd = int(input("enter first number: "))
num_2_unorderd = int(input("enter second number: "))
num_3_unorderd = int(input("enter third number: "))
num_list = [num_1_unorderd, num_2_unorderd, num_3_unorderd]
num_list.sort()
print(num_list)

num_1, num_2, num_3 = num_list[2], num_list[1], num_list[0] 
print(num_2**2+num_3**2)
if num_2**2+num_3**2 == num_1**2:
    print("Pythagorean triple!!!!!!!!!!!!")
else:
    print("not a Pythagorean triple")

