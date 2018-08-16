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
my_example_nc_file = 'C:\\Temp\data\S5P_NRTI_L2__NO2____20180727T004306_20180727T004806_04068_01_010100_20180727T022935.nc'
fh = Dataset(my_example_nc_file, mode='r')
#print (fh)
#print (fh.groups)
#print (fh.groups['PRODUCT'])
#print (fh.groups['PRODUCT'].variables.keys())
#print (fh.groups['PRODUCT'].variables['nitrogendioxide_tropospheric_column_precision'])
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

xi, yi = m(lons, lats)

# Plot Data
cs = m.pcolor(xi,yi,np.squeeze(no2),norm=LogNorm(), cmap='jet')

# Add Grid Lines
#m.drawparallels(np.arange(-80., 81., 10.), labels=[1,0,0,0], fontsize=10)
#m.drawmeridians(np.arange(-180., 181., 10.), labels=[0,0,0,1], fontsize=10)

# Add Coastlines, States, and Country Boundaries
#m.drawcoastlines()
#m.drawstates()
#m.drawcountries()

# Add Colorbar
#cbar = m.colorbar(cs, location='bottom', pad="10%")
#cbar.set_label(no2_units)

# Add Title
#plt.title('NO2 in atmosphere')
#plt.show()

n = len(no2)
x = np.zeros((n,3), float)

#x[:,0] = lons[:]
#x[:,1] = lats[:]
#x[:,2] = no2[:]

#nx = lons.shape[0]
#nx = len(lons)
#ny = len(lats)
#xmin, ymin, xmax, ymax = [lons.min(), lats.min(), lons.max(), lats.max()]
#xres = (xmax - xmin) / float(nx)
#yres = (ymax - ymin) / float(ny)
#geotransform = (xmin, xres, 0, ymax, 0, -yres)


##Creates 1 raster band file
#dst_ds = gdal.GetDriverByName('GTiff').Create('c:\\temp\data\myGeoTIFF.tif', ny, nx, 1, gdal.GDT_Float32)
##
#dst_ds.SetGeoTransform(geotransform)    # specify coords
#srs = osr.SpatialReference()            # establish encoding
#srs.ImportFromEPSG(3857)                # WGS84 lat/long
#dst_ds.SetProjection(srs.ExportToWkt()) # export coords to file
#dst_ds.GetRasterBand(1).WriteArray(x)   # write r-band to the raster
#dst_ds.FlushCache()                     # write to disk
#dst_ds = None                           # save, close


