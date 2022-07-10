#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
def multiple_iterations():
    y_new = np.array([[11,3,1],[2,-6,1],[-6,6,1]])
    w = np.array([[1,-2,0],[0,-1,2],[1,3,-1]])
    d = np.array([[1,-1,-1],[-1,1,-1],[-1,-1,1]])
    c = 1
    iter = 5
    out = np.zeros((3,3))
    r = np.zeros((3,3))
    net = np.dot(y_new[0],np.transpose(w))
    for i in range(1,iter):
        out[i]=net
        out[i][out[i]>0]=1
        out[i][out[i]<0]= -1
        r[0] = d[0]-out[0]
        delta_w=0.5*np.dot(np.transpose(r),y_new)
        w=w+delta_w
        print(w)
        return w
multiple_iterations()


# In[ ]:




