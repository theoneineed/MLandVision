#Nabin Chapagain
#1001551151


#decision_tree(<training_file>, <test_file>, <option>, <pruning_thr>)

# Importing all needed libraries
import numpy as np
import math
import sys
import random
import statistics

fname = sys.argv[1]
fname1 = sys.argv[2]
option = sys.argv[3]
pruning_thr = sys.argv[4]

mat_train = np.loadtxt(fname)
mat_test= np.loadtxt(fname1)

train_max = mat_train[:,0:-1].max()

no_train_mat_row = len(mat_train) 
no_train_mat_col = len(mat_train[0])

if(option == "optimized" or "randomized"):
    option_rot = 1
elif(option == "forest3"):
    option_rot = 3
elif(option == "forest15"):
    option_rot = 15
else:
    print("wrong input for option. Case sensitive: optimized, randomized, forest3, forest15\n")

def DTL_Toplevel(examples, pruning_thr):#returns a decision tree
    attributes = np.arange(0,no_train_mat_col-1,1)
    default = DISTRIBUTION(examples)
    default = np.where(default == np.amax(default))

    return DTL(examples, attributes,int(default[0][0]),pruning_thr)


class Node:
    def __init__(self, best_attribute, best_threshold, gain):

        self.left_child = None
        self.right_child = None
        self.best_attribute = best_attribute
        self.best_threshold = best_threshold
        self.gain = gain


        
def DISTRIBUTION(examples):
    #print(examples)
    diff_classes = np.unique(examples[:,-1])
    len_row = len(examples)
    p_dist = np.zeros(len(diff_classes))
    for i in range(len(diff_classes)):
        cl_elem_ind = np.where(examples[:,-1] == diff_classes[i])
        len_cl_ele = len(cl_elem_ind[0])
        p_dist[i] = len_cl_ele/len_row
    return p_dist

def DTL(examples, attributes, default, pruning_thr):
    #returns a decision tree
    if (len(examples)<pruning_thr):
        return default
    elif ((np.unique(examples[:,-1])).size == 1):
        return int(examples[0,-1])
    else:
        examples_left =[]
        examples_right =[]
        global option
        if (option == "optimized"):
            (best_attribute, best_threshold, gain)= CHOOSE_ATTRIBUTE_O(examples, attributes)
        else:
            (best_attribute, best_threshold, gain)= CHOOSE_ATTRIBUTE_R(examples, attributes)
        tree = Node(best_attribute, best_threshold,gain)
        for i in range(len(examples)):
            if (examples[i][best_attribute]<best_threshold):
                examples_left.append(examples[i])
            else:
                examples_right.append(examples[i])
        examples_left = np.array(examples_left)
        examples_right = np.array(examples_right)
        dist = DISTRIBUTION(examples)
        dist_max = np.where(dist==np.amax(dist))
        tree.left_child = DTL(examples_left, attributes, int(dist_max[0][0]),pruning_thr)
        tree.right_child = DTL(examples_right, attributes, int(dist_max[0][0]),pruning_thr)
        return tree

def CHOOSE_ATTRIBUTE_O(examples, attributes):
    #returns (attribute,threshold)
    max_gain = best_attribute = best_threshold = -1
    
    for A in attributes:
        attribute_values = examples[:,A]
        L = np.amin(attribute_values)
        M = np.amax(attribute_values)
        for K in range(1,51):
            threshold = L + (K*(M-L))/51
            gain = INFORMATION_GAIN(examples, A, threshold)
            if (gain > max_gain):
                max_gain = gain
                best_attribute = A
                best_threshold = threshold
    return (best_attribute, best_threshold, gain)


def RANDOM_ELEMENT(attributes):
    return random.choice(attributes)

def CHOOSE_ATTRIBUTE_R(examples, attributes):
    #returns (attribute,threshold)
    max_gain = best_threshold = -1
    A = RANDOM_ELEMENT(attributes)
    attribute_values = examples[:,A]
    L = np.amin(attribute_values)
    M = np.amax(attribute_values)
    for K in range(1,51):
        threshold = L+K*(M - L)/51
        gain = INFORMATION_GAIN(examples, A, threshold)
        if (gain > max_gain):
            max_gain = gain
            best_threshold = threshold
    return (A, best_threshold, gain)

def Entropy_calc(dist):
    entr = 0
    for i in range(0,len(dist)):
        entr = entr - dist[i]*np.log2(dist[i])
    return entr

def INFORMATION_GAIN(examples, A, threshold):
    examples_left =[]
    examples_right =[]
    
    for i in range(len(examples)):
        if (examples[i][A] < threshold):
            examples_left.append(examples[i])
        else:
            examples_right.append(examples[i])
    examples_left = np.array(examples_left)
    examples_right = np.array(examples_right)
    
    dist = DISTRIBUTION(examples)
    entr_left =0
    entr_right =0
   
    if (examples_left.size != 0):
        dist_left = DISTRIBUTION(examples_left)
        entr_left = Entropy_calc(dist_left)
    if (examples_right.size != 0):
        dist_right = DISTRIBUTION(examples_right)
        entr_right = Entropy_calc(dist_right)
    
    inf_gain = Entropy_calc(dist)- (examples_left.size / examples.size) * entr_left - (examples_right.size / examples.size) * entr_right
    return inf_gain



def bfs(root, tree_id):
    to_visit = []
    if root:
        to_visit.append(root)
    node_no = 1

    while to_visit:
        current = to_visit.pop(0)
        #feature = (current.best_attribute)
        if (type(current) == np.int64 or type(current) == int):
            gain=0
            feature = current
            threshold = -1
        else:
            gain = current.gain
            feature = current.best_attribute
            threshold = current.best_threshold
            if (current.left_child is not None):
                to_visit.append(current.left_child)
            if (current.right_child is not None):
                to_visit.append(current.right_child)
        print('tree=%2d, node=%3d, feature=%2d, thr=%6.2f, gain=%f\n'%(tree_id, node_no, feature, threshold, gain))
        node_no+=1


decision_forest=[]
for i in range(1,option_rot+1):
    top_level = DTL_Toplevel(mat_train, 50)
    bfs(top_level,i)
    decision_forest.append(top_level)


def traversing(root):
    class_acc=0
    for i in range(0,len(mat_test)):
        current = root
        while (type(current) not in [int,np.int64]):
            if(mat_test[i][current.best_attribute] < current.best_threshold):
                current = current.left_child
            else:
                current = current.right_child
        predicted = current
        if(predicted == mat_test[i,-1]):
            accuracy = 1
        else:
            accuracy = 0
        class_acc+=accuracy
        print("D=%5d, predicted=%3d, true=%3d, accuracy=%4.2f\n"%(i+1, predicted, mat_test[i,-1], accuracy))
    class_acc = class_acc/len(mat_test)
    print("classification accuracy=%6.4f\n"%(class_acc))


if(option == "optimized" or option == "randomized"):
    traversing(top_level)


def traversing_dec_forest(decision_forest):
    class_acc = 0
    predicted_list=[]
    for i in range(0,len(mat_test)):
        for j in range(0,len(decision_forest)):
            current = decision_forest[j]
            while (type(current) not in [int,np.int64]):
                if(mat_test[i][current.best_attribute] < current.best_threshold):
                    current = current.left_child
                else:
                    current = current.right_child
            predicted_list.append(current)
        
        predicted = statistics.mode(predicted_list)
        #the class which shows up the most in decision trees has more chance of being the right answer.
        if(predicted == int(mat_test[i,-1])):
            accuracy = 1
        else:
            accuracy = 0
        class_acc+=accuracy
        print("D=%5d, predicted=%3d, true=%3d, accuracy=%4.2f\n"%(i+1, predicted, mat_test[i,-1], accuracy))
    class_acc = class_acc/len(mat_test)
    print("classification accuracy=%6.4f\n"%(class_acc))




if(option == "forest3" or option == "forest15"):
    traversing_dec_forest(decision_forest)





















