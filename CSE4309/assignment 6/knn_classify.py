#Nabin Chapagain
#1001551151

#knn_classify(<training_file>, <test_file>, <k>)

# Importing all needed libraries
import numpy as np
import math
import sys
import random
from scipy import stats
from scipy.spatial import distance
import statistics as s
from statistics import mean, median, mode, stdev

fname = sys.argv[1]
fname1 = sys.argv[2]
k_nearest = int(sys.argv[3])

mat_train = np.loadtxt(fname)
mat_train_prime = mat_train[:,0:-1]
mat_test= np.loadtxt(fname1)
mat_test_prime = mat_test[:,0:-1]

no_train_mat_row = len(mat_train) 
no_train_mat_col = len(mat_train[0])

mean_arr = np.zeros(no_train_mat_col-1)
std_arr = np.zeros(no_train_mat_col-1)
std_in_between = 0

#getting mean and standard deviation for each attribute before normalizing

for i in range (0,no_train_mat_col-1):
    mean_arr[i] = mean(mat_train[:,i])
    std_in_between = stdev(mat_train[:,i])
    if (std_in_between == 0):
        std_in_between = 1
    std_arr[i] = std_in_between

#next step, normalizing the values


for j in range(0,no_train_mat_col-1):
    mat_train[:,j] = (mat_train[:,j] - mean_arr[j])/std_arr[j]
    # F(v) = (v - mean)/std


for j in range(0,no_train_mat_col-1):
    mat_test[:,j] = (mat_test[:,j] - mean_arr[j])/std_arr[j]
    # F(v) = (v - mean)/std

#here, we have normalized training matrix and test matrix

classification_accuracy = 0

for i in range(0,len(mat_test)):
    E_dist = np.zeros(no_train_mat_row)
    for k in range(len(E_dist)):
        E_dist[k]= distance.euclidean(mat_test_prime[i],mat_train_prime[k])

    accuracy = 0
    true_class =  mat_test[i][-1]

    k_nearest_points = E_dist.argsort()[:k_nearest]
    #This is the index of k_nearest_points number of lowest numbers in the list E_dist 
    
    predicted_array = mat_train[k_nearest_points,-1]

    accuracy = 0
    mode_class = s.multimode(predicted_array)
    mode_class.sort()
    #print(mode_class,"\n")
    if(len(mode_class) == 1):
        predicted_class = mode_class[0]

        if(predicted_class == true_class):
            accuracy = 1
    else:
        #now to deal with ties
        for m in range(0,len(mode_class)):
            predicted_class = mode_class[m]
            if(true_class == predicted_class):
                accuracy = len(np.where(true_class == mode_class))/len(mode_class)
                break

    object_id = i+1
    print('ID=%5d, predicted=%3d, true=%3d, accuracy=%4.2f'%( object_id, predicted_class, true_class, accuracy))
    classification_accuracy+=accuracy
print('classification accuracy=%6.4f\n'% (classification_accuracy/len(mat_test)))












