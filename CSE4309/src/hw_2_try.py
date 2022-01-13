#Nabin Chapagain
#1001551151

#training

# Importing all needed libraries
import numpy as np
import math
import sys
from statistics import mean, median, mode, stdev
n=0
#taking argument from command line
fname = sys.argv[1]
fname1 = sys.argv[2]
mat = np.loadtxt(fname)
mat_test= np.loadtxt(fname1)
#loads file into matrix form
no_row_test= len(mat_test)
no_row = len(mat)
num_acc=0
no_col = len(mat[0])
temp = mat.view(np.ndarray)
np.lexsort((temp[:, no_col-1], ))
#sorts the matrix on the basis of ascending order using the column that I selected
mat1 = temp[np.lexsort((temp[:, no_col-1], ))]
no_of_class=1
array=[0]*100

array[0]=0
index=1
for i in range(0,no_row):
    if(i+1<no_row):
        if(mat1[i+1][no_col-1]-mat1[i][no_col-1] != 0):
            no_of_class+=1
            array[index]=i+1
            index+=1
array[index]=no_row-1
P_C=np.zeros(no_of_class)

for j in range(0, no_of_class):
    P_C[j]=(array[j+1]-array[j])/no_row

mean_arr = np.zeros((no_of_class, no_col-1))
stdev_arr = np.zeros((no_of_class, no_col-1))
#save mean and standard deviation in matrix form

for j in range(0,no_of_class):
    data=mat1[array[j]:array[j+1],:]
    for col in range(0,no_col-1):
        mean_arr[j][col] = mean(data[:,col])
        stdev_arr[j][col] = stdev(data[:,col])
        if(stdev_arr[j][col] < 0.01):
            stdev_arr[j][col] = 0.01

for i in range(0, len(mean_arr)):
    for j in range(0, no_col-1):
        print('Class %d, attribute %d, mean = %.2f, std = %.2f'%(i+1, j+1, mean_arr[i][j], stdev_arr[i][j]))

    #testing

for i in range(0, no_row_test):
    test_line = mat_test[i]
    prob_x_class = []
    for class_no in range(0,no_of_class):
        Prob_x_class_i = 1
        for att in range(0, no_col-1):
            x = test_line[att]
            Gauss_prob = (1/(stdev_arr[class_no][att] * np.sqrt(2*np.pi))) * np.exp(-np.power((x - mean_arr[class_no][att]),2)/(2*np.power(stdev_arr[class_no][att],2)))
            Prob_x_class_i = Prob_x_class_i * Gauss_prob
        prob_x_class.append(Prob_x_class_i)
    P_x= sum(prob_x_class*P_C)
#need to apply Baye's rule now
    P_C_X = np.multiply(prob_x_class , P_C)/P_x
    maxim = np.amax(P_C_X)
    acc=-1
    maxim_index = np.where(P_C_X == np.amax(P_C_X))
    if(maxim_index[0]+1==test_line[no_col-1]):
        acc=1
    else:
        acc=0

    if(acc==1):
        num_acc+=1
    print("ID=%5d, predicted=%3d, probability = %.4f, true=%3d, accuracy=%4.2f\n"%(i+1,maxim_index[0]+1,maxim, test_line[no_col-1],acc))
print("classification accuracy=%6.4f"%(num_acc/len(mat_test)))
