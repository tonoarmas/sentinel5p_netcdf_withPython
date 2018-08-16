# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 11:01:27 2018

@author: antdia
"""

from netCDF4 import Dataset
import numpy as np

my_example_nc_file = 'C:\Temp\data\S5P_NRTI_L2__NO2.nc'
fh = Dataset(my_example_nc_file, mode='r')
print (fh)