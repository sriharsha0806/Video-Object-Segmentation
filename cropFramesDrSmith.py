# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 12:44:31 2016

@author: Sriharsha 
"""

import numpy as np
import scipy.cluster.hierarchy as hcluster
import scipy.cluster.vq as kcluster

#import skimage
from matplotlib import pyplot as plt


masksBaseline = np.load('./birdfall_masksBaseline.npy')

framesRGB = np.load('./framesRGB.npy')

masksDialated = np.zeros(framesRGB[:26,:,:,0].shape)

croppedLabelsBLM = np.zeros(framesRGB[:26,:,:,0].shape)

M,N = masksBaseline[:,:,0].shape
x,y=np.ogrid[0:M,0:N]

for i in range(masksDialated.shape[0]):
    indx = np.where(masksBaseline[:,:,i]==1)
    
    for j in range(indx[0].size):
        masksDialated[i]+=np.where(\
                            np.sqrt((x-indx[0][j])**2+(y-indx[1][j])**2)\
                                     <=50,1,0)
        masksDialated[i] = np.where(masksDialated[i]>0,1,0)
    
#    skimage.morphology.binary_dilation(masksBaseline[:,:,i],\
#    skimage.morphology.disk(50),out=masksDialated[i]).astype('uint8')
        
    croppedLabelsBLM[i] = masksBaseline[:,:,i] + masksDialated[i]
        
croppedFramesRGB = (framesRGB[:26]*\
                    masksDialated[:,:,:,np.newaxis]).astype('uint8')

appPrior = np.zeros(masksBaseline.shape)                    

for k in range(1): #range(croppedFramesRGB.shape[0]):
    indx = np.where(croppedLabelsBLM[k]!=0)
    X = croppedFramesRGB[k,indx[0],indx[1]]/255
    Y = masksBaseline[indx[0],indx[1],k]
    
    Xclustered = kcluster.kmeans(X.astype('float64'), 500)
    #Xclustered = hcluster.fclusterdata(X, 10, criterion="distance", \
    #method='single')
    numClusters =10# np.unique(Xclustered)
    C = Xclustered[0] #np.zeros((numClusters.size,X.shape[1]))
    #for c in range(C.shape[0]):
    #    C[c]=np.mean(X[np.where(Xclustered==c+1)],0)
        
    Z = np.zeros((Y.size,C.shape[0]))
    
    for m in range(Z.shape[0]):
        for n in range (Z.shape[1]):
            Z[m,n]= np.linalg.norm(X[m]-C[n])
            
    Z = np.exp(-Z/.01)
    H = np.dot(Z.transpose(),Z)
    I = np.eye(C.shape[0])
    U = np.dot(Z.transpose(),Y)
    W = np.dot(np.linalg.inv(H+0.1*I),U)
    
    appPrior[indx[0],indx[1],k] = np.dot(Z,W)
    
#    pixPrior = np.dot(Z,W)
#
#    for p in range(indx[0].size):
#        appPrior[indx[0][p],indx[1][p],k]=pixPrior[p]

#    frameSuPix=np.load('./frameSuPixs.npy')
#    
#    appModel = frameSuPix[:,:,0]*masksDialated[0]
#
#suPixId = np.unique(appModel[np.nonzero(appModel)])
#
#for a in range(suPixId.size):
#    phiA = np.sum(appPrior[np.where(appModel==suPixId[a])])
#    appModel=np.where(appModel==suPixId[a],phiA,appModel)
    

    
