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
#print (fh.groups['PRODUCT'].variables['ground_pixel'])
#print (fh.groups['PRODUCT'].variables['scanline'])
#print (fh.groups['PRODUCT'].variables['corner'])
lons = fh.groups['PRODUCT'].variables['longitude'][:][0,:,:]
lats = fh.groups['PRODUCT'].variables['latitude'][:][0,:,:]
no2 = fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision'][0,:,:]
#print (lons.shape) #-->(290L,450L)
#print (lats.shape) #-->(290L,450L)
#print (no2) #-->(290L,450L)
#print (no2[:][3,3])
#
#
no2_units = fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision'].units
lon_0 = lons.mean()
lat_0 = lats.mean()

m = Basemap(width=5000000,height=3500000,
            resolution='l',projection='stere',\
            lat_ts=40,lat_0=lat_0,lon_0=lon_0)
# convert to map projection coords.
# Note that lon,lat can be scalars, lists or numpy arrays.
xi, yi = m(lons, lats)
print (xi)
# Plot Data
cs = m.pcolor(xi,yi,np.squeeze(no2),norm=LogNorm(), cmap='jet')
# Add Grid Lines
m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)
# Add Coastlines, States, and Country Boundaries
m.drawcoastlines()
m.drawstates()
m.drawcountries()
# Add Colorbar
#cbar = m.colorbar(cs, location='bottom', pad="10%")
#cbar.set_label(no2_units)
# Add Title
#plt.title('NO2 in atmosphere')
#plt.show()


###from here: https://pcjericks.github.io/py-gdalogr-cookbook/raster_layers.html#create-raster-from-array
#def array2raster(newRasterfn,rasterOrigin,pixelWidth,pixelHeight,array):
#cols = no2.shape[1]
cols = xi.shape[1]
rows = yi.shape[0]
print (cols, rows)

xMin = xi.min()
yMin = yi.min()
array = np.squeeze(no2)
yMax = yi.max()
xMax = xi.max()

nx = no2.shape[0]
ny = no2.shape[1]

#lons.shape[ny]
#xmin, ymin, xmax, ymax = [lons.min(), lats.min(), lons.max(), lats.max()]

#print xmin, ymin, xmax, ymax 
xRes = (xMax - xMin) / float(nx)
yRes = (yMax - yMin) / float(ny)
#geotransform = (xmin, xres, 0, ymax, 0, -yres)


#
#
driver = gdal.GetDriverByName('GTiff')
outRaster = driver.Create('c:\\temp\data\output2.tif', cols, rows, 1, gdal.GDT_Float32)
outRaster.SetGeoTransform((xMin, xRes, 0, yMin, 0, yRes))
outband = outRaster.GetRasterBand(1)
outband.WriteArray(no2)
outRaster.GetRasterBand(1).WriteArray(array)
outRasterSRS = osr.SpatialReference()
outRasterSRS.ImportFromEPSG(3411)
outRaster.SetProjection(outRasterSRS.ExportToWkt())
outband.FlushCache()
#    


