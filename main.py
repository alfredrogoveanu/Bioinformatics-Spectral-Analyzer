from matplotlib import pyplot as plt
import numpy as np
randn = np.random.randn
from pandas import *

#Array declarations
w, h = 20, 10;
Mat_A = [[0 for x in range(w)] for y in range(h)]
Mat_B = [[0 for x in range(w)] for y in range(h)]
Mat_M = [[0 for x in range(w)] for y in range(h)]

fileA = open(r"Matrix_A.txt","r+")
fileB = open(r"Matrix_B.txt","r+")

#Open contents for the A matrix and store them in the Mat_A array
j = 0
with open('Matrix_A.txt') as f:
    for line in f:
        for i in range(w):
            data=line.split()
            Mat_A[j][i] = float(data[i])
        j = j + 1

#Open contents for the B matrix and store them in the Mat_B array
j = 0
with open('Matrix_B.txt') as f:
    for line in f:
        for i in range(w):
            data=line.split()
            Mat_B[j][i] = float(data[i])
        j = j + 1

#Distance, we assume it's 100, it ranges from 0 to 100
d = 100

#Find the maximum in the A array
Max_A = 0
for i in range(h):
    for j in range(w):
        if Mat_A[i][j] > Max_A:
            Max_A = Mat_A[i][j]

#Find the maximum in the B array
Max_B = 0
for i in range(h):
    for j in range(w):
        if Mat_B[i][j] > Max_B:
            Max_B = Mat_B[i][j]

#Generating the M matrix
#Seeting up the plot of the table, using a gradient from #5A8AC6 to #FFEB84 and #F8696B
array_big = []
for i in range(h):
    array = []
    for j in range(w):
        Mat_M[i][j] = (d / Max_A) * Mat_A[i][j] + (100 - d) / Max_B * Mat_B[i][j]
        if Mat_M[i][j] < 8.33 :
            array.append("#5A8AC6")
        elif Mat_M[i][j] < 16.67 :
            array.append("#00A6D4")
        elif Mat_M[i][j] < 25 :
            array.append("#00BFCC")
        elif Mat_M[i][j] < 33.33 :
            array.append("#47D3B3")
        elif Mat_M[i][j] < 41.67 :
            array.append("#99E295")
        elif Mat_M[i][j] < 50 :
            array.append("#BDDD7E")
        elif Mat_M[i][j] == 50 :
            array.append("#FFEB84")
        elif Mat_M[i][j] < 58.33 :
            array.append("#DFD570")
        elif Mat_M[i][j] < 66.67 :
            array.append("#FFCB6E")
        elif Mat_M[i][j] < 75 :
            array.append("#FFB364")
        elif Mat_M[i][j] < 83.33 :
            array.append("#FF9A61")
        elif Mat_M[i][j] < 91.67 :
            array.append("#FF8264")
        elif Mat_M[i][j] <= 100 :
            array.append("#F8696B")
    array_big.append(array)

#Plotting the restulting M matrix.
idx = Index(np.arange(1,11))
df = DataFrame(Mat_M, index=idx)
vals = np.around(df.values,2)
fig = plt.figure(figsize=(15,8))
ax = fig.add_subplot(111, frameon=True, xticks=[], yticks=[])
the_table=plt.table(cellText=vals, rowLabels=df.index, colLabels=df.columns,
                    colWidths = [0.03]*vals.shape[1], loc='center',
                    cellColours=array_big)
#plt.show()
plt.savefig('Matrix_M_1.png')

#Plotting the restulting M matrix, without colours
fig = plt.figure(figsize=(15,8))
ax = fig.add_subplot(111, frameon=True, xticks=[], yticks=[])
the_table=plt.table(cellText=vals, rowLabels=df.index, colLabels=df.columns,
                    colWidths = [0.03]*vals.shape[1], loc='center')
#plt.show()
plt.savefig('Matrix_M_2.png')

#Plotting the restulting M matrix, without colours
the_table=plt.table(rowLabels=df.index, colLabels=df.columns,
                    colWidths = [0.03]*vals.shape[1], loc='center',
                    cellColours=array_big)
#plt.show()
plt.savefig('Matrix_M_3.png')