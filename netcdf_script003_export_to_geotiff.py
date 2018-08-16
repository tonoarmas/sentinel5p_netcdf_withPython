# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 11:01:27 2018

@author: antdia
"""
from IPython import get_ipython
from netCDF4 import Dataset
import numpy as np
get_ipython().run_line_magic('matplotlib', 'qt')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from mpl_toolkits.basemap import Basemap
import gdal
import osr
import netCDF4
import os
my_example_nc_file = 'C:\\Temp\data\S5P_NRTI_L2__NO2.nc'
fh = Dataset(my_example_nc_file, mode='r')
print fh.file_format


#print (fh)
#print (fh.groups)
#print (fh.groups['PRODUCT'])
#print (fh.groups['PRODUCT'].variables.keys())
#print (fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision'])
lons = fh.groups['PRODUCT'].variables['longitude'][:][0,:,:]
lats = fh.groups['PRODUCT'].variables['latitude'][:][0,:,:]
no2 = fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision'][0,:,:]
no2_units = fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision'].units
#print (lons.shape) #-->(290L,450L)
#print (lats.shape) #-->(290L,450L)
#print (no2.shape) #-->(290L,450L)
#print (no2[:][3,3])

n = len(no2)
x = np.zeros((290,450), float)
print x.shape
#x[:,0] = lons[:]
#x[:,1] = lats[:]
#x[:,2] = no2[:]

nx = no2.shape[0]
ny = no2.shape[1]

#lons.shape[ny]
#xmin, ymin, xmax, ymax = [lons.min(), lats.min(), lons.max(), lats.max()]
xmin, ymin, xmax, ymax = -114.154,61.2847,49.3223,88.6367
#print xmin, ymin, xmax, ymax 
xres = (xmax - xmin) / float(nx)
yres = (ymax - ymin) / float(ny)
geotransform = (xmin, xres, 0, ymax, 0, -yres)


#Creates 1 raster band file
#dst_ds = gdal.GetDriverByName('GTiff').Create('c:\\temp\data\myGeoTIFF.tif', ny, nx, 1, gdal.GDT_Float32)
dst_ds = gdal.GetDriverByName('GTiff').Create('c:\\temp\data\myGeoTIFF.tif', 450, 290, 1, gdal.GDT_Float32)
#
dst_ds.SetGeoTransform(geotransform)    # specify coords
srs = osr.SpatialReference()            # establish encoding
#srs.ImportFromEPSG(3857)                # WGS84 lat/long
srs.ImportFromEPSG(4326)                # WGS84 lat/long
dst_ds.SetProjection(srs.ExportToWkt()) # export coords to file
#dst_ds.GetRasterBand(1).WriteArray(np.squeeze(no2))   # write r-band to the raster
dst_ds.GetRasterBand(1).WriteArray(no2)   # write r-band to the raster
dst_ds.FlushCache()                     # write to disk
dst_ds = None                           # save, close


