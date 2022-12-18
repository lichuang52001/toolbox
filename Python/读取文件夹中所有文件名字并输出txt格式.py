# list all filenames in specific folder
"""
Created on Wed Aug 14 19:24:16 2019
@author: Chuang Li
E-mail: lichuang52001@gmail.com
"""
#%% import packages
import os
import numpy as np

#%% locate filepath
filepath = 'E:\\Videos from WD\\Videos\\'

#%% get filenames
name = os.listdir(filepath)

#%% save filenames
np.savetxt('name.txt', name, delimiter=',',fmt='%s')
