# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 11:01:27 2018

@author: antdia
"""

from netCDF4 import Dataset
import numpy as np

my_example_nc_file = 'C:\Temp\data\S5P_NRTI_L2__NO2.nc'
fh = Dataset(my_example_nc_file, mode='r')
#print (fh)
#print (fh.groups)
#print (fh.groups['PRODUCT'])
#print (fh.groups['PRODUCT'].variables.keys())
#print (fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision'])
lons = fh.groups['PRODUCT'].variables['longitude'][:][0,:,:]
lats = fh.groups['PRODUCT'].variables['latitude'][:][0,:,:]
no2 = fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision'][0,:,:]
print (lons.shape)
print (lats.shape)
print (no2.shape)


no2_units = fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision'].units