
""" Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
Example
Let us assume the following comma separated input sequence is given to the program:
100,150,180
The output of the program should be:
18,22,24 """

print("Give me the numbers")
#numbers=input()
#listOfNumbers=numbers.split(",")

from math import sqrt

entrada="100,150,180,187,200"
values=[]

items=[x for x in entrada.split(",")]

C=50
H=30
for D in items:
    values.append(str(round(sqrt((2*C*float(D))/H))))

print(",".join(values))



""" import math
c=50
h=30
values = []

items=[x for x in input().split(",")]
for d in items:
    values.append(str(round(math.sqrt(2 * c * float(d)/h))))


print(",".join(values))
 """


