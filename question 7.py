
""" Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
Note: i=0,1.., X-1; j=0,1,¡­Y-1.
Example
Suppose the following inputs are given to the program:
3,5
Then, the output of the program should be:
[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]  """

#dimX=int(input("X:"))
#dimY=int(input("Y:"))

dimX=3
dimY=5

""" 
result=[]

for x in range(dimX):
    row=[]
    for y in range(dimY):
        row.append(x*y)

    result.append(row) """


multilist = [[0 for col in range(dimX)] for row in range(dimY)]

print(multilist)

for row in range(dimY):
    for col in range(dimX):
        multilist[row][col]= row*col

print(multilist)


