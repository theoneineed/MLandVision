#Nabin Chapagain
#1001551151


#k_means(<data_file>, <K>, <initialization>)

# Importing all needed libraries
import numpy as np
import math
import sys
import random
import matplotlib.pyplot as plt

fname = sys.argv[1]
k = int(sys.argv[2])
initialization = sys.argv[3]

if(initialization == "round_robin" or initialization == "random"):
    k = k
else:
    print("wrong input for initialization!!! Try again with round_robin or random")
    exit(0)

file_mat_raw = np.loadtxt(fname)
dim = file_mat_raw.ndim
no_row = len(file_mat_raw)
no_col = 1
if(dim != 1):
    no_col =len(file_mat_raw[0])

b = np.random.randint(1,k+1, size = no_row )

if(initialization == 'round_robin'):
    for i in range(no_row):
        if((i+1)%k == 0):
            b[i] = k
        else:
            b[i] = (i+1)%k

file_mat = np.column_stack((file_mat_raw,b))

#now I have read the file and assigned a column to store the value of assigned cluster, I will proceed to compute the means
#It might be better to use recursion for this case

poss_clusters = np.arange(1,k+1)

centers = np.zeros([k, no_col])
dist = np.zeros([k, 1])


counter = 1
while(counter > 0):
    counter = 0
    for i in range(k):
        dummy_var = np.mean(file_mat[:][file_mat[:,-1]==i+1], axis=0)
        centers[i] = dummy_var[0:no_col]

    
    #now need to calculate euclidean distance for each point in individual rows from each of the centers
    for i in range(no_row):
        for j in range(k):
            dist[j] = np.linalg.norm(file_mat_raw[i] - centers[j])

        
        supposed_cluster = np.argmin(dist)+1
        if(file_mat[i,-1] != supposed_cluster):
            file_mat[i,-1] = supposed_cluster
            counter += 1
            
if(no_col == 1):
    for i in range(no_row):
        print('%10.4f --> cluster %d\n'% (file_mat[i,0], file_mat[i,-1]))
if(no_col == 2):
    for i in range(no_row):
        print('(%10.4f, %10.4f) --> cluster %d\n'% (file_mat[i,0], file_mat[i,1], file_mat[i,-1]))
        

        
#colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
if(no_col == 2):
    fig = plt.figure( figsize=(3, 3) \
                    , dpi= 100 \
                    , facecolor='w' \
                    , edgecolor='w' \
                    ) # create figure object
    

for i in range(k):
    choice = file_mat_raw[:][file_mat[:,-1] == i+1]
    if(no_col == 2):
        plt.scatter(choice[:,0],choice[:,1])
        
        plt.scatter(centers[:,0],centers[:,1], c= 'k')
if(no_col == 2):        
    plt.show()

    