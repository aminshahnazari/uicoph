import numpy as np

#Defining a and b with 2*2 size
a=[[1.,2.],[4.,5.]]
b=[[1.,2.],[3.,4.]]

#Createing a blank array with required dimensions
c=np.zeros([4,4])

#Looping through c elements and determining value of each index
for i in range(4):
    for j in range(4):
        c[i][j]= a[(i)//2][(j)//2] * b[(i)%2][(j)%2]


print c
