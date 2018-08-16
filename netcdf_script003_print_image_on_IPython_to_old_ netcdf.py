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
print (fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column'])
#print (fh.groups['PRODUCT'].variables['ground_pixel'])
#print (fh.groups['PRODUCT'].variables['scanline'])
#print (fh.groups['PRODUCT'].variables['corner'])
#ds_lon = fh.groups['PRODUCT'].variables['longitude'][:][0,:,:]
#ds_lat = fh.groups['PRODUCT'].variables['latitude'][:][0,:,:]
corners = fh.groups['PRODUCT'].variables['corner'][:][0,:,:]
print (corners)
#longs = ds_lon
#lats = ds_lat
#ds_lon = None
#ds_lat = None
#proj_out = osr.SpatialReference()
#proj_gcp = osr.SpatialReference()
#proj_gcp.ImportFromEPSG(4326)
#transf = osr.CoordinateTransformation(proj_gcp, proj_out)
#ul = transf.TransformPoint(float(longs[0][0]), float(lats[0][0]))
#lr = transf.TransformPoint(float(longs[len(longs)-1][len(longs[0])-1]), float(lats[len(longs)-1][len(longs[0])-1]))
#ur = transf.TransformPoint(float(longs[0][len(longs[0])-1]), float(lats[0][len(longs[0])-1]))
#ll = transf.TransformPoint(float(longs[len(longs)-1][0]), float(lats[len(longs)-1][0]))
#gt0 = ul[0]
#gt1 = (ur[0] - gt0) / len(longs[0])
#gt2 = (lr[0] - gt0 - gt1*len(longs[0])) / len(longs)
#gt3 = ul[1]
#gt5 = (ll[1] - gt3) / len(longs)
#gt4 = (lr[1] - gt3 - gt5*len(longs) ) / len(longs[0])
#geotransform = (gt0,gt1,gt2,gt3,gt4,gt5)
#no2 = fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision'][0,:,:]
#cols = no2.shape[0]
#rows = no2.shape[1]
#
#driver = gdal.GetDriverByName('netCDF')
#outRaster = driver.Create('c:\\temp\data\output3.nc', cols, rows, 1, gdal.GDT_Float32)
#outRaster.SetGeoTransform(geotransform)
#outRaster.GetRasterBand(1).WriteArray(no2)
#outRasterSRS = osr.SpatialReference()
#outRasterSRS.ImportFromEPSG(4326)
#outRaster.SetProjection(outRasterSRS.ExportToWkt())
#outRaster = None
