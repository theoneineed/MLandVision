#Nabin Chapagain
#1001551151


#value_iteration(<environment_file>, <non_terminal_reward>, <gamma>, <K>)


# Importing all needed libraries
import numpy as np
import math
import sys
import random

fname = sys.argv[1]
non_terminal_reward = float(sys.argv[2])
gamma = float(sys.argv[3])
k = int(sys.argv[4])#number of iterations

#print("\n")
U_frm_file = np.genfromtxt(fname,dtype='str', delimiter=',')
#print(U_frm_file)

size_mat = U_frm_file.shape
number_rows = int(size_mat[0])
number_columns = int(size_mat[1])

#print("\n",size_mat)
#print("\n")
U_prime = np.zeros(size_mat)
U_prime+=non_terminal_reward
#print(U_prime)

rows_X, cols_X = np.where(U_frm_file[:,:] == 'X')
U_prime[rows_X,cols_X] = 0

rows_1, cols_1 = np.where(U_frm_file[:,:] == '1.0')
U_prime[rows_1,cols_1] = 1.0

rows_n1, cols_n1 = np.where(U_frm_file[:,:] == '-1.0')
U_prime[rows_n1,cols_n1] = -1.0


#print(U_prime)
#print(rows_X[0]," and ",cols_X[0])

def Max_prob_calc(U,row,column):
    prob_r = 0
    prob_l = 0
    prob_u = 0
    prob_d = 0
    prob_steady = 0
    right_sum = left_sum = up_sum = down_sum = 0

    #for right
    if(column+1 != number_columns):
        prob_r = 0.8
        right_sum += prob_r * U[row, column+1]
    else:
        prob_steady+=0.8

    if(row+1 != number_rows):
        prob_d = 0.1
        right_sum += prob_d*U[row+1, column]
    else:
        prob_steady+=0.1

    if(not row-1 < 0):
        prob_u = 0.1
        right_sum += prob_u*U[row-1, column]
    else:
        prob_steady+=0.1

    right_sum +=  prob_steady*U[row,column]






    prob_r = prob_l = prob_u = prob_d = prob_steady = 0
    #resetting values

    #for down
    if(row+1 != number_rows):
        prob_d = 0.8
        down_sum += prob_d*U[row+1, column]
    else:
        prob_steady += 0.8
    
    if(column+1 != number_columns):
        prob_r = 0.1
        down_sum += prob_r*U[row, column+1]
    else:
        prob_steady+=0.1

    if(not column-1 < 0):
        prob_l = 0.1
        down_sum += prob_l*U[row,column-1]
    else:
        prob_steady+=0.1

    down_sum += prob_steady*U[row,column]






    prob_r = prob_l = prob_u = prob_d = prob_steady = 0
    #resetting values

    #for left
    if(not column-1 < 0):
        prob_l = 0.8
        left_sum += prob_l*U[row,column-1]
    else:
        prob_steady += 0.8

    if(row+1 != number_rows):
        prob_d = 0.1
        left_sum += prob_d*U[row+1, column]
    else:
        prob_steady+=0.1

    if(not row-1 < 0):
        prob_u = 0.1
        left_sum += prob_u*U[row-1, column]
    else:
        prob_steady+=0.1

    left_sum +=prob_steady*U[row,column]






    prob_r = prob_l = prob_u = prob_d = prob_steady = 0
    #resetting values


    #for up
    if(not row-1 < 0):
        prob_u = 0.8
        up_sum += prob_u*U[row-1, column]
    else:
        prob_steady += 0.8

    if(column+1 != number_columns):
        prob_r = 0.1
        up_sum += prob_r*U[row, column+1]
    else:
        prob_steady+=0.1

    if(not column-1 < 0):
        prob_l = 0.1
        up_sum += prob_l*U[row,column-1]
    else:
        prob_steady+=0.1
    
    up_sum += prob_steady*U[row,column]



    return max(left_sum,up_sum,right_sum,down_sum)





#repeat
for i in range(1,k+1):
    U = U_prime
    sigma = 0
    for row in range(int(size_mat[0])):
        for column in range(int(size_mat[1])):
            #what we are doing is for each state in our matrix, we update the value of matrix using new formula
            if(U_prime[row,column] in [0.0,1.0,-1.0]):
                continue
            else:
                #print(U_prime[row,column])
                U_prime[row,column] = non_terminal_reward + gamma * Max_prob_calc(U, row, column)
                #if((U_prime[row,column]-U[row,column])>sigma):
                    #sigma = U_prime[row,column]-U[row,column]
print('\n utilities:')
for i in range(len(U)):
    for j in range(len(U[0])):
        print('%6.3f'%(U[i,j]),end=' ')
    print('\n',end='')




print('\n policy:')

last_mat = np.zeros(size_mat,dtype='S1')
#print('\n',last_mat)

for row in range(number_rows):
    for column in range(number_columns):
        if((row - 1 ) >= 0 and (row+1)<number_rows and (column-1) >= 0 and (column+1)<number_columns):
            l_u_r_d = np.array([U[row,column-1],U[row-1,column],U[row, column+1],U[row+1,column]])
            max_index = np.argmax(l_u_r_d)
            if(max_index==0):
                last_mat[row,column] = '<'
            elif(max_index==1):
                last_mat[row,column] = '^'
            elif(max_index==2):
                last_mat[row,column] = '>'
            else:
                last_mat[row, column] = 'v'

        elif((row-1)<0 and (row+1)<number_rows and (column-1) >= 0 and (column+1)<number_columns):
            l_r_d = np.array([U[row,column-1],U[row,column+1],U[row+1,column]])
            max_index = np.argmax(l_r_d)
            if(max_index == 0):
                last_mat[row,column] = '<'
            elif (max_index==1):
                last_mat[row,column] = '>'
            else:
                last_mat[row, column] = 'v'
        
        elif((row - 1 ) >= 0 and (row+1)>=number_rows and (column-1) >= 0 and (column+1)<number_columns):
            l_u_r = np.array([U[row,column-1],U[row-1,column],U[row,column+1]])
            max_index = np.argmax(l_u_r)
            if(max_index == 0):
                last_mat[row,column] = '<'
            elif (max_index==1):
                last_mat[row,column] = '^'
            else:
                last_mat[row, column] = '>'
        

        elif((row - 1 ) >= 0 and (row+1)<number_rows and (column-1) < 0 and (column+1)<number_columns):
            u_r_d = np.array([U[row-1,column],U[row,column+1],U[row+1,column]])
            max_index = np.argmax(u_r_d)
            if(max_index == 0):
                last_mat[row,column] = '^'
            elif (max_index==1):
                last_mat[row,column] = '>'
            else:
                last_mat[row, column] = 'v'
        
        elif((row - 1 ) >= 0 and (row+1)<number_rows and (column-1) >= 0 and (column+1)>=number_columns):
            u_l_d = np.array([U[row-1,column],U[row,column-1],U[row+1,column]])
            max_index = np.argmax(u_r_d)
            if(max_index == 0):
                last_mat[row,column] = '^'
            elif (max_index==1):
                last_mat[row,column] = '<'
            else:
                last_mat[row, column] = 'v'

        elif((row-1)<0 and (column-1)<0):
            r_d = np.array([U[row,column+1],U[row+1,column]])
            max_index = np.argmax(r_d)
            if(max_index == 0):
                last_mat[row,column] = '>'
            else:
                last_mat[row,column] = 'v'
        
        elif((row+1)>=number_rows and (column-1)<0):
            r_u = np.array([U[row,column+1],U[row-1,column]])
            max_index = np.argmax(r_u)
            if(max_index == 0):
                last_mat[row,column] = '>'
            else:
                last_mat[row,column] = '^'

        elif((row-1)<0 and (column+1)>=number_columns):
            l_d = np.array([U[row,column-1],U[row+1,column]])
            max_index = np.argmax(l_d)
            if(max_index == 0):
                last_mat[row,column] = '<'
            else:
                last_mat[row,column] = 'v'
 
        elif((row+1)>=number_rows and (column+1)>=number_columns):
            l_u = np.array([U[row,column-1],U[row-1,column]])
            max_index = np.argmax(l_u)
            if(max_index == 0):
                last_mat[row,column] = '<'
            else:
                last_mat[row,column] = '^'
        

        if((row,column)==(rows_X,cols_X)):
            last_mat[row,column]='X'
        elif((row,column)==(rows_1,cols_1) or (row,column)==(rows_n1,cols_n1)):
            last_mat[row,column]='o'

#print(last_mat)



for row in range(number_rows):
    for column in range(number_columns):
        ch = str(last_mat[row,column], 'utf-8')
        print(ch,end=' ')
    print('\n',end='')