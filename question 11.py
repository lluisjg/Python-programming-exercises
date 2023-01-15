""" Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console. """

input="0100,0011,1010,1001"

result=[]

listOfNumbers=input.split(",")
for item in listOfNumbers:
    number = int(item,2)
    if number%5 == 0:
        result.append(item)


print(" ".join(result))