# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 20:02:16 2016

@author: Sriharsha
"""

import numpy as np
from matplotlib import pyplot as plt

masksBaseline = np.load('./birdfall_masksBaseline.npy')
frameSuPixs = np.load('./frameSuPixs.npy')

suPixsLabeled = frameSuPixs[:,:,:masksBaseline.shape[2]]\
*np.where(masksBaseline==0,-1,1)

phiG = np.zeros((frameSuPixs.max(),masksBaseline.shape[2]))

for i in range(suPixsLabeled.shape[2]):
    for j in range(frameSuPixs.max()):
        countPixVoted = np.size(np.where(suPixsLabeled[:,:,i]==j+1)[0])
        if (countPixVoted != 0):
            countPixTotal = np.size(np.where(frameSuPixs[:,:,i]==j+1)[0])
            phiG[j,i] = countPixVoted/countPixTotal
            
                
