#Nabin Chapagain
#1001551151


#neural_network(<training_file>, <test_file>, <layers>, <units_per_layer>, <rounds>)

# Importing all needed libraries
import numpy as np
import math
import sys
import random

fname = sys.argv[1]
fname1 = sys.argv[2]
no_layers = int(sys.argv[3])
Unitspl = int(sys.argv[4])
#units_per_layer = how many perceptrons to place at each HIDDEN layer
#Note that this number is not applicable either to the input layer or to the output layer
rounds = int(sys.argv[5])
#rounds is the number of training rounds that you should use
#Each training round consists of using the whole training set once (i.e., using each training example once to update the weights)

if(no_layers<2):
    print('The minimum number of layers should be 2 including input and output layer.\n\n')
    exit()
eta = 1

mat_train = np.loadtxt(fname)
mat_test= np.loadtxt(fname1)

train_max = mat_train[:,0:-1].max()

no_train_mat_row = len(mat_train)
no_train_mat_col = len(mat_train[0])

for i in range(no_train_mat_row):
    for j in range(no_train_mat_col-1):
        mat_train[i][j] = mat_train[i][j]/train_max

#print(mat_test,"\n\n\n\n\n\n")

for i in range(len(mat_test)):
    for j in range(no_train_mat_col-1):
        mat_test[i][j] = mat_test[i][j]/train_max

#print(mat_test)

"""
Training Phase

"""

train_mat_uniq = np.unique(mat_train[:,-1])
#This gives us a vector with s-values

random.seed()
#seed in order to get random values

Dim = max((no_train_mat_col-1),Unitspl,len(train_mat_uniq))
#usinf the max value possible so there will not be any shortage of memory space later
wt = np.zeros((no_layers, Dim, Dim))
bias = np.zeros((no_layers, Dim))

units2b_used=0




#sigmoid function to call later
def sigmoid(x):
    sig = 1/(1+ np.exp(-x))
    return sig




for i in range (0,no_layers):
    for j in range (0,Dim):
        for k in range(0,Dim):
            wt[i][j][k]= (random.random()/20)*(random.randrange(-1,1))



for i in range(0,no_layers):
    for j in range(0,Dim):
        bias[i][j] = (random.random()/20)*(random.randrange(-1,1))

#we need to go as many rounds as asked
for l in range(0,rounds):
    print("Round",l, "starting.. \n\n\n")
    #browsing through each individual row of train_mat
    for i  in range(0, no_train_mat_row):
        t= np.zeros(len(train_mat_uniq))
        #we are making a test vector here
        for j in range(0,len(train_mat_uniq)):
            if(mat_train[i][-1]==train_mat_uniq[j]):
                t[j]=1
            t_t = t.T #transpose of hot_vector

        z_output = np.zeros((no_layers, Dim))



        for j in range(0,no_train_mat_col-1):
            z_output[0][j]=mat_train[i][j]

        a_wtdsum = np.zeros((no_layers, Dim))


        for j in range(1,no_layers):
            for k in range(0,Dim):
                wtd_sum =bias[j][k]

                if((j-1) != 0):
                    for m in range(0,Dim):
                        wtd_sum += wt[j][k][m]*z_output[j-1][m]

                elif((j -1)==0):
                     for m in range(0,no_train_mat_col-1):
                        wtd_sum += wt[j][k][m]*z_output[j-1][m]

                a_wtdsum[j][k] = wtd_sum



                z_output[j][k] = sigmoid(a_wtdsum[j][k])

        #now to compute new delta values
        delta = np.zeros((no_layers, Dim))

        for j in range(0,len(train_mat_uniq)):
            delta[no_layers-1][j]= (z_output[no_layers-1][j] - t[j]) * z_output[no_layers-1][j] * (1-z_output[no_layers-1][j])


        for j in range(no_layers-2, 0,-1):
            for k in range(0,Dim):
                del_in =0
                if (j+1 == no_layers-1):
                    units2b_used = len(train_mat_uniq)
                else:
                    units2b_used = Dim

                for looping in range(0,units2b_used):
                    del_in += delta[j+1][looping] * wt[j+1][looping][k]
                delta[j][k] = del_in *z_output[j][k] * (1 - z_output[j][k])


        units2b_used = 0
        for j in range(1,no_layers):

            if(j==no_layers-1):
                units2b_used = len(train_mat_uniq)
            else:
                units2b_used = Dim

            for m in range(0,units2b_used):
                bias[j][m] = bias[j][m] - eta * delta[j][m]

                units_loop = 0
                if (j-1 == 0):
                    units_loop = no_train_mat_col-1
                else:
                    units_loop = Dim

                for n in range (0, units_loop):
                    wt[j][m][n] = wt[j][m][n] - eta * delta[j][m]* z_output[j-1][n]


    eta*=0.98
    #eta gets updated with each row in the training matrix

"""
Classification Phase
"""
av_acc=0

test_mat_uniq = np.unique(mat_test[:,-1])


for i in range(0,len(mat_test)):
    t= np.zeros(len(test_mat_uniq))
    #we are making a test vector here

    z_output = np.zeros((no_layers, Dim))

    for j in range(0,no_train_mat_col-1):
        z_output[0][j]=mat_test[i][j]

    a_wtdsum = np.zeros((no_layers, Dim))

    for j in range(1,no_layers):
        if(j==no_layers-1):
            Units2b_used = len(test_mat_uniq)
        else:
            Units2b_used = Dim
        for k in range(0,Units2b_used):
            wtd_sum =bias[j][k]

            if((j-1) != 0):
                for m in range(0,Dim):
                    wtd_sum += wt[j][k][m]*z_output[j-1][m]

            elif((j -1)==0):
                for m in range(0,no_train_mat_col-1):
                    wtd_sum += wt[j][k][m]*z_output[j-1][m]

            a_wtdsum[j][k] = wtd_sum


            z_output[j][k] = sigmoid(a_wtdsum[j][k])
    #z_output has to be updated with each run

    object_id = i+1
    predicted_class_index = np.where(z_output[no_layers-1] == z_output[no_layers-1].max())
    predicted_class = (test_mat_uniq[predicted_class_index[0][0]])

    accuracy = 0
    true_class = mat_test[i][-1]
    if(predicted_class == true_class):
        accuracy=1

    print('ID=%5d, predicted=%3d, true=%3d, accuracy=%4.2f\n'%(object_id, predicted_class, true_class, accuracy));
    av_acc+=accuracy
av_acc = av_acc/len(mat_test)
#this is for average of accuracy for the whole test_file

print('classification accuracy=%6.4f\n'% av_acc);
