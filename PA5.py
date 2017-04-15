# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 07:25:18 2016

@author: Sriharsha 
"""

import numpy as np
from matplotlib import pyplot as plt

# load masks obatined from four other segmenation methods (previously formated
# from mat files)
masksGroudTruth = np.load('birdfall_masksGroundTruth.npy')[:,:,:26]
masksDagSeg = np.load('birdfall_masksDagSeg.npy')[:,:,:26]
masksJOTSeg = np.load('birdfall_masksJOTSeg.npy')[:,:,:26]
masksKegSeg = np.load('birdfall_masksKeySeg.npy')[:,:,:26]
masksSeamSeg = np.load('birdfall_masksSeamSeg.npy')[:,:,:26]

# generate Baseline masks
masksBaseline = np.where(((masksDagSeg + masksJOTSeg +  \
                           masksKegSeg + \
                           masksSeamSeg)/4) > 0.5,1,0).astype('uint8')

# create a list for the titles of each figure according to the mask
titleSeg = ('GroundTruth', 'DagSeg', 'JOTSeg', 'KeySeg', 'SeamSeg', 'Baseline')

# plot masks for each segmentaiton method
for i in range(np.size(titleSeg)):
    plt.figure()
    
    if (i < 5):
        masksTemp = np.load("birdfall_masks%s.npy" % titleSeg[i])[:,:,:26]
    else:
        masksTemp = masksBaseline
    
    # calculate the average per-frame pixel error rate in comparison with
    # groundtruth
    tempErr = np.round(np.size(\
                               np.where(\
                                        (masksTemp.flatten() \
                                         ^ masksGroudTruth.flatten())==1)\
                                        )/masksTemp.shape[2])
    
    plt.suptitle("%s, with err = %d" % (titleSeg[i],  tempErr.astype('int')))
    
    # plot masks for each frame
    for j in range(masksTemp.shape[2]):
        plt.subplot(5,6,j+1)
        plt.title('Frame #%d' % (j+1))
        plt.imshow(masksTemp[:,:,j], cmap='gray')
        plt.axis('off')
