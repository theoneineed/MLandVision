#Nabin Chapagain
#1001551151


#linear_regression(<training_file>, <test_file>, <degree>, <lambda>)


# Importing all needed libraries
import numpy as np
import math
import sys
from statistics import mean, median, mode, stdev
fname = sys.argv[1]
fname1 = sys.argv[2]
degree = int(sys.argv[3])
lambda_in = int(sys.argv[4])

#loading files into matrices
mat_train = np.loadtxt(fname)
mat_test= np.loadtxt(fname1)

no_train_mat_row = len(mat_train)
no_train_mat_col = len(mat_train[0])

#phi matrix has degree dependent columns
no_phi_mat_row = no_train_mat_row
no_phi_mat_col = (no_train_mat_col-1)*degree +1

no_row_x = no_phi_mat_col

phi_dim =(no_phi_mat_row, no_phi_mat_col)

phi_mat = np.zeros(phi_dim)


for i in range (0,no_phi_mat_row):
    for j in range(0,no_phi_mat_col):
        if (j==0):
            phi_mat[i][j]=1
        else:
            if(j % degree == 0):
                phi_mat[i][j]=np.power(mat_train[i][j//degree-1],degree)
            else:
                phi_mat[i][j] = np.power(mat_train[i][j//degree + 1-1],(j % degree))

t = mat_train[:,-1]

phi_mat_tr =phi_mat.T
I = np.identity(no_phi_mat_col)

one_more_step = np.linalg.pinv(lambda_in*I + phi_mat_tr.dot(phi_mat)).dot(phi_mat_tr)
w = one_more_step.dot(t)


for i in range (0,len(w)):
    print('w%d = %.4f'%(i,w[i]))

#number of attributes is important for getting value of y
no_att = len(mat_test[0])-1

for i in range (0,len(mat_test)):
    y = w[0]
    counter=1
    for j in range(0, no_att):
        for k in range(1,degree+1):
            y += w[counter]*np.power(mat_test[i][j],k)
            counter+=1
    sqert = abs(y-mat_test[i,-1])**2
    print("ID=%5d, output=%14.4f, target value = %10.4f, squared error = %.4f"%(i+1,y,mat_test[i,-1],sqert))
