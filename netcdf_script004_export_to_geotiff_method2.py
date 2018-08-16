# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 11:01:27 2018

@author: antdia
"""
from osgeo import gdal, osr, gdal_array
import xarray as xr
import numpy as np

"""
Function to read the original files projection
"""
in_filename = 'c:\temp\data\S5P_NRTI_L2__NO2.nc'
var_name = 'no2'
#Open netCDF file
src_ds = gdal.Open(in_filename)
subdataset = 'NETCDF:"' + in_filename + '":' + var_name
src_ds_sd = gdal.Open(subdataset)
#begins to read info of the named variable (i.e, subdataset)
#NDV = src_ds_sd.GetRasterBand(1).GetNoDataValue()
xsize =src_ds_sd.RasterXSize
ysize =src_ds_sd.RasterYSize
GeoT = src_ds_sd.GetGeoTransform()
Projection = osr.SpatialReference()
Projection.ImportFromWkt(src_ds_sd.GetProjectionRef())
#close the subdataset and the whole dataset
src_ds_sd = None
src_ds = None
#read data using xarray
xr_ensemble = xr.open_dataset(in_filename)
data = xr_ensemble[var_name]
data = np.ma.masked_array(data, mask=data==NDV,fill_value=NDV)
print NDV, xsize, ysize, GeoT, Projection, data
        
