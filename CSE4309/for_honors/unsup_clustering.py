#Here goes the code that was written for n-dimensional minimum volume ellipsoid.

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
import sys
from sklearn.cluster import KMeans
import os

# Get Current working Directory
currentDirectory = os.getcwd()
currentDirectory_pic = currentDirectory+'/pictures/'
#to better organize all the pictures


filename = sys.argv[1]
print_value = int(sys.argv[2]) #will use this to print the information for the final cluster and not every cluster formed in the process.
graph_data = int(sys.argv[3])

# read data
Data = pd.read_csv(filename)
Point= np.array([Data.x,Data.y])

#print(Point)
if(graph_data == 1):
    fig = plt.figure( figsize=(4.5, 4) \
                    , dpi= 100 \
                    , facecolor='w' \
                    , edgecolor='w' \
                    ) # create figure object
    ax = fig.add_subplot(1,1,1) # Get the axes instance

    ax.plot( Point[0,:] \
            , Point[1,:] \
            , 'r.' \
            , markersize = 1 \
            ) # plot with color red, as line

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    fig.savefig(currentDirectory_pic+'points.png', dpi=200) # save the figure to an external file
    plt.show() # display the figure




def getMinVolPartition(Point, print_value):
    import numpy as np
    npoint = len(Point[0,:])
    ndim = len(Point[:,0])
    ncMax = npoint // (ndim + 1) # max number of clusters possible
    # // is floor division in python

    BoundingEllipsoidCenter = np.array([np.mean(Point[0,:]),np.mean(Point[1,:])])
    #the case is for two dimensional picture where all the x points' mean are calculated and all the y points' mean are calculated and is saved as boundingcenter
    #maybe, we can address n-dim case by making a loop where we make an array out of mean of each dimension's points' mean

    SampleCovMat = np.mat(np.cov(Point))
    #a covariance matrix is made using the points provided

    SampleInvCovMat = np.mat(np.linalg.inv(SampleCovMat))
    #inverse matrix of above covariance matrix is calculated

    PointNormed = np.mat(np.zeros((ndim,npoint)))
    # a 0 matrix of ndim x npoint is constructed which we call pointnormed
    #i=ndim, j=npoint

    for idim in range(ndim):
        PointNormed[idim,:] = Point[idim] - BoundingEllipsoidCenter[idim]
    #so we started with a null matrix, of given dimensions, then we fill out the matrix with corresponding Points
    #but this step shifts the supposed center of the ellipsoid to the origin of the grap and as a result shifting
    #all the other points by certain factor

    MahalSq = PointNormed.T * SampleInvCovMat * PointNormed
    #a picture depicting idea of mahalanobis distance is in this same directory.
    # formula for mahalanobis distance is D^2 = (x-<x>)^T C^(-1) (x-<x>)
    #i.e.; distance sqrd= Transposed matrix of (vector of data-vector of mean values of independent variables) X inverse of covariance matrix X (vector of data- vector of mean .....)

    maxMahalSq = np.max(MahalSq)
    #for mahalsq is a matrix that pops out of above given matrix arithmetic, we calculate the maximum mahalanobis distance
    #because max mahalsq helps us find the matrix with least covariance

    BoundingEllipsoidVolume = np.linalg.det(SampleCovMat) * maxMahalSq**ndim

    BoundingEllipsoidCovMat = SampleCovMat * maxMahalSq

    if(print_value == 1):
        print(
    """
    nd = {}
    np = {}
    ncMax = {}
    SampleCovMat = {}
    InvCovMat = {}
    max(MahalSq) = {}
    BoundingEllipsoidCenter = {}
    BoundingEllipsoidCovMat = {}
    BoundingEllipsoidVolume = {}
    """.format( ndim
              , npoint
              , ncMax
              , SampleCovMat[:]
              , SampleInvCovMat
              , maxMahalSq
              , BoundingEllipsoidCenter
              , BoundingEllipsoidCovMat
              , BoundingEllipsoidVolume
              )
    )

    return BoundingEllipsoidCenter, BoundingEllipsoidCovMat
    #scipy.spatial.distance.mahalanobis




def getRandMVU(numRandMVU,MeanVec,CovMat,isInside=True):
    """
    generates numRandMVU uniformly-distributed random points from
    inside an ndim-dimensional ellipsoid with Covariance Matrix CovMat,
    centered at MeanVec[0:ndim].
    Output:
        Numpy matrix of shape numRandMVU by ndim
    """
    import numpy as np
    ndim = len(MeanVec)
    #meanvec is center and ndim is the no of values in points in center

    AvgStdMVN = np.zeros(ndim)
    #we start with n dimensional columns and one row

    CovStdMVN = np.eye(ndim)
    #gives a unit matrix of ndim X ndim
    #Return a 2-D array with ones on the diagonal and zeros elsewhere.

    RandStdMVN = np.random.multivariate_normal(AvgStdMVN,CovStdMVN,numRandMVU)

    DistanceSq = np.sum(RandStdMVN**2, axis=1)

    #print(len(DistanceSq))
    if isInside:
        UnifRnd = np.random.random((numRandMVU,))
        UnifRnd = (UnifRnd**(1./ndim)) / np.sqrt(DistanceSq)

    CholeskyLower = np.linalg.cholesky(np.mat(CovMat))
    #print(CholeskyLower[1,0])
    RandMVU = np.zeros(np.shape(RandStdMVN))
    for iRandMVU in range(numRandMVU):
        if isInside:
            RandStdMVN[iRandMVU] *= UnifRnd[iRandMVU]
        else:
            RandStdMVN[iRandMVU] /= np.sqrt(DistanceSq[iRandMVU])
        for i in range(ndim):
            RandMVU[iRandMVU,i] = RandMVU[iRandMVU,i] + CholeskyLower[i,i] * RandStdMVN[iRandMVU,i]
            for j in range(i+1,ndim):
                RandMVU[iRandMVU,j] = RandMVU[iRandMVU,j] + CholeskyLower[j,i] * RandStdMVN[iRandMVU,i]
        RandMVU[iRandMVU] += MeanVec
    return RandMVU

#getRandMVU(numRandMVU,MeanVec,CovMat,isInside=True)



def Vol_calc(CovMat,ndim):
    Vol_ball = 1
    inv_mat = np.linalg.inv(CovMat)
    #now, to find out volume of ball in n-dim

    if(ndim % 2 == 0):
        Vol_ball = 1/np.math.factorial(ndim/2) * np.power(np.pi, (ndim/2))
    else:
        Vol_ball = (2**ndim)*(1/np.math.factorial(ndim))*(np.math.factorial((ndim-1)/2))*(np.power(np.pi,((ndim-1)/2)))
    #Volume of ellipsoid is sqrt of cov_met times of volume of ball in same dimension
    Vol_el = Vol_ball * np.sqrt(np.linalg.det(CovMat))
    return Vol_el



def sub_division(Points,ndim):

    if(print_value==1):
        print("\nCalculating for the subclusters:\n\n")

    MeanVec, CovMat = getMinVolPartition(Points,print_value)

#    Data_list = np.array([[j, Points.T['y'][i]] for i,j in enumerate(Points.T['x'])]) 
    
#    Data_list = np.array([[i[0] for i in Points.T], [i[1] for i in Points.T]]) 



    ####This is the line that is the problem###
    
    
    
    
    
    
    
    model =  KMeans(n_clusters = 2)
    kmeans=model.fit(Points.T)
    centroids = kmeans.cluster_centers_
    
    cluster_data1 = Data_list[np.where(kmeans.labels_==0)]
    cluster_data2 = Data_list[np.where(kmeans.labels_==1)]
    Points1 = np.zeros((2,len(cluster_data1)))
    Points2 = np.zeros((2,len(cluster_data2)))
    
    #print(Points,"\n\n", Points1, "\n\n", Points2)
    
     #changing the format of the data read so that I can use getMinVolPartition function on it
    
    for k in range(0,len(Points1[0])):
        Points1[0][k]=cluster_data1[k][0]
        Points1[1][k]=cluster_data1[k][1]
    MeanVec1, CovMat1 = getMinVolPartition(Points1,print_value)
    
    for k in range(0,len(Points2[0])):
        Points2[0][k]=cluster_data2[k][0]
        Points2[1][k]=cluster_data2[k][1]
    MeanVec2, CovMat2 = getMinVolPartition(Points2,print_value)
    
    #print("ndim =",ndim,"\n\nMeanvec, Covmat = ", MeanVec, CovMat,"\n\nMeanvec1, Covmat1 = ", MeanVec1, CovMat1,"\n\nMeanvec2, Covmat2 = ", MeanVec2, CovMat2)
    a =Vol_calc(CovMat,ndim)
    b= Vol_calc(CovMat1,ndim)
    c = Vol_calc(CovMat2,ndim)
    #print("\n\n\n","original,f_cluster,s_cluster = ",a,b,c,"sum_of_subclusters = ",b+c,"\n\n\n")
    
    #print(Points1,"\n\n\n",Points2,"\n\n\n")
    
    if(a<(b+c)):
        #no need to move further
        global counter
        counter+=1
        
    else:
        sub_division(Points1,ndim)
        sub_division(Points2,ndim)



#
#
#
#Executables starting from here
#
#
#



data = Data
Data_list=np.array([[j,data['y'][i]]for i,j in enumerate(data['x'])])


Point= np.array([data.x,data.y])
npoint = len(Point[0,:]) #number of points in the file
ndim = len(Point[:,0]) #number of dimensions from the data set in the file
ncMax = npoint // (ndim + 1) # max number of clusters possible
counter = 0

sub_division(Point, ndim)
print("\n\n\n",counter,"is the number of clusters required.\n\n\n")


if(graph_data == 1):
    final_draw = counter
    model =  KMeans(n_clusters = final_draw)
    kmeans=model.fit(data)
    centroids = kmeans.cluster_centers_
    fig = plt.figure(figsize=(4,3))
    for i in range(final_draw):
        plt.scatter([x[0] for x in Data_list[np.where(kmeans.labels_==i)]],[y[1] for y in Data_list[np.where(kmeans.labels_==i)]])
        plt.scatter([x[0] for x in centroids],[y[1] for y in centroids],color='k')
    plt.show()




    #Finally, here I am trying to plot the points with surrounding ellipsoids for each cluster

    fig = plt.figure( figsize=(4.5, 4) \
                    , dpi= 100 \
                    , facecolor='w' \
                    , edgecolor='w' \
                    ) # create figure object
    ax.set_xlabel('X')
    ax.set_ylabel('Y')


    for no_of_clusters in range(0,counter): 
        
        cluster_data = Data_list[np.where(kmeans.labels_==no_of_clusters)]
        
        final_points = cluster_data.T
        
        MeanVec_final, CovMat_final = getMinVolPartition(final_points, print_value)

        RandMVU = getRandMVU( numRandMVU=1000 #this many points to be generated
                            , MeanVec=MeanVec_final #this is supposed to be the supposed center
                            , CovMat=CovMat_final #this will be the covariance of the ellipsoid we will be drawing
                            , isInside = False
                            )

        # plot the points
        plt.plot( final_points[0,:] \
                , final_points[1,:] \
                , 'r.' \
                , markersize = 2 \
                )

        # plot the center point
        plt.plot( MeanVec_final[0] \
                , MeanVec_final[1] \
                , 'b.' \
                , markersize = 10 \
                )

        # plot the bounding ellipsoid
        plt.scatter(RandMVU[:,0],RandMVU[:,1],1)

    plt.show()
    fig.savefig(currentDirectory_pic+'after_picture.png', dpi=200) # save the figure to an external fil
