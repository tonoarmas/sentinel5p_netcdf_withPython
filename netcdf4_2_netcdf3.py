# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 14:28:49 2018

@author: antdia
"""

from netCDF4 import Dataset

#input file
dsin = Dataset("c:\\temp\\data\\S5P_NRTI_L2__NO2____20180727T004306_20180727T004806_04068_01_010100_20180727T022935.nc")

#output file
dsout = Dataset("C:\\temp\\data\crop.nc3", "w", format="NETCDF3_CLASSIC")

#Copy dimensions
for dname, the_dim in dsin.dimensions.iteritems():
    print dname, len(the_dim)
    dsout.createDimension(dname, len(the_dim) if not the_dim.isunlimited() else None)


# Copy variables
for v_name, varin in dsin.variables.iteritems():
    outVar = dsout.createVariable(v_name, varin.datatype, varin.dimensions)
    print varin.datatype
    
    # Copy variable attributes
    outVar.setncatts({k: varin.getncattr(k) for k in varin.ncattrs()})
    
    outVar[:] = varin[:]
# close the output file
dsout.close()