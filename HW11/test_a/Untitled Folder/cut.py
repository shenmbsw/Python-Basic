# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:46:32 2016

@author: shen
"""

                if flag == 1:                                         #2nd compare through the boundary not finished
                    if (ac.shape == bc.shape):
                        if((ac[0, :, :] !=bc[0, :, :]).any()):
                            if((ac[:, 0, :] != bc[:, 0, :]).any()):
                                if((ac[0, :, :] != bc[-1, :, :]).any()):
                                    if((ac[:, 0, :] != bc[:, -1, :]).any()):
                                        flag = 0
                                        
                    elif ((ac.shape[1],ac.shape[0]) == bc.shape[0:2]):
                        ac = ac.swapaxes(0,1)
                        if((ac[0, :, :] !=bc[0, :, :]).any()):
                            if((ac[0, :, :] != bc[-1, :, :]).any()):
                                if((ac[:, 0, :] != bc[:, 0, :]).any()):
                                    if((ac[:, 0, :] != bc[:, -1, :]).any()):
                                        flag = 0
                        if debug:
                            if flag==0:
                                print(ac[:,:,1],"\n")
                                print(bc[:,:,1],"\n")
                                print((ac[:, 0, :] != bc[:, -1, :]).any())
                    else:
                        flag = 0
                        
                        
                        
                        
                                            if debug==0:
                        if flag==0:
                            print(ac[:,:,1],"\n")
                            print(bc[:,:,1],"\n")
                            print((ac[:, 0, :] != bc[:, -1, :]).any())