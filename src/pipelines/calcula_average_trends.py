"""
Calculates average trends 
from various processes 
across the MITgcm dataset
"""

import numpy as np
import xarray as xr
import netCDF4 as nc4
import sys

sys.path.append('../../')
from src.general.constants import *


def read_mitgcm_trends(data_raw_path):
    """
    Read in netcdf file for shape and variables
    """
    
    dat = xr.open_dataset(f"{data_raw_path}cat_tave.nc")
    
    return dat


def netcdf_array(data_interm_path):
    
    """
    Set up new netcdf array
    """
    
    nc = nc4.Dataset(
        f"{data_interm_path}avera_trend.nc",
        'w',
        format='NETCDF4'
    ) 
    
    return nc


def create_dimens(
    nc,
    dat
):
    """Create dimensions"""
    nc.createDimension('T', None)
    nc.createDimension('Z', dat['Z'].shape[0])
    nc.createDimension('Y', dat['Y'].shape[0])
    nc.createDimension('X', dat['X'].shape[0])
    nc.createDimension('Yp1', dat['Yp1'].shape[0])
    nc.createDimension('Xp1', dat['Xp1'].shape[0])
    
    return nc


def get_mean(
    var,
    dat,
    start=start,
    skip=skip
):
    
    mean = np.nanmean(
    np.abs(dat[var].data[:start*skip+1:skip,:,:,:]),
    axis=0
    )
    
    return mean

    
def create_variables(
    dat,
    nc,
    start,
    skip
):
    """Create variables and get averages"""
    
    nc_T = nc.createVariable('T', 'i4', 'T')
    nc_T[:] = dat['T'].data[1:start*skip+1:skip]

    nc_Z = nc.createVariable('Z', 'i4', 'Z')
    nc_Z[:] = dat['Z'].data

    nc_Y = nc.createVariable('Y', 'i4', 'Y') 
    nc_Y[:] = dat['Y'].data

    nc_X = nc.createVariable('X', 'i4', 'X')
    nc_X[:] = dat['X'].data

    nc_Yp1 = nc.createVariable('Yp1', 'i4', 'Yp1')  
    nc_Yp1[:] = dat['Yp1'].data

    nc_Xp1 = nc.createVariable('Xp1', 'i4', 'Xp1')
    nc_Xp1[:] = dat['Xp1'].data

    nc_Av_ADVr_TH = nc.createVariable('Av_ADVr_TH', 'f4', ('Z', 'Y', 'X'))
    nc_Av_ADVr_TH[:,:,:] = get_mean('ADVr_TH', dat)

    nc_Av_ADVx_TH = nc.createVariable('Av_ADVx_TH', 'f4', ('Z', 'Y', 'Xp1'))
    nc_Av_ADVx_TH[:,:,:] = get_mean('ADVx_TH', dat)
    
    nc_Av_ADVy_TH = nc.createVariable('Av_ADVy_TH', 'f4', ('Z', 'Yp1', 'X'))
    nc_Av_ADVy_TH[:,:,:] = get_mean('ADVy_TH', dat)
    
    nc_Av_DFrE_TH = nc.createVariable('Av_DFrE_TH', 'f4', ('Z', 'Y', 'X'))
    nc_Av_DFrE_TH[:,:,:] = get_mean('DFrE_TH', dat)

    nc_Av_DFrI_TH = nc.createVariable('Av_DFrI_TH', 'f4', ('Z', 'Y', 'X'))
    nc_Av_DFrI_TH[:,:,:] = get_mean('DFrI_TH', dat)

    nc_Av_DFxE_TH = nc.createVariable('Av_DFxE_TH', 'f4', ('Z', 'Y', 'Xp1'))
    nc_Av_DFxE_TH[:,:,:] = get_mean('DFxE_TH', dat)
    
    nc_Av_DFyE_TH = nc.createVariable('Av_DFyE_TH', 'f4', ('Z', 'Yp1', 'X'))
    nc_Av_DFyE_TH[:,:,:] = get_mean('DFyE_TH', dat)
    
    nc_Av_TOTTTEND= nc.createVariable('Av_TOTTTEND','f4', ('Z', 'Y', 'X'))
    nc_Av_TOTTTEND[:,:,:] = get_mean('TOTTTEND', dat)
    
    nc_Av_UVELTH  = nc.createVariable('Av_UVELTH', 'f4', ('Z', 'Y', 'Xp1'))
    nc_Av_UVELTH[:,:,:] = get_mean('UVELTH', dat)
    
    nc_Av_VVELTH  = nc.createVariable('Av_VVELTH', 'f4', ('Z', 'Yp1', 'X'))
    nc_Av_VVELTH[:,:,:] = get_mean('VVELTH', dat)
    
    nc_Av_WVELTH  = nc.createVariable('Av_WVELTH' , 'f4', ('Z', 'Y', 'X'))
    nc_Av_WVELTH[:,:,:] = get_mean('WVELTH', dat)


def obtain_averga_trends(
    data_raw_path,
    data_interm_path,
    start,
    skip
):
    """Obtain averages trends and save"""

    dat = read_mitgcm_trends(data_raw_path)
    nc = netcdf_array(data_interm_path)
    nc = create_dimens(nc, dat)
    
    create_variables(dat, nc, start, skip)
    
    nc.close()
    

obtain_averga_trends(
    data_raw_path,
    data_interm_path,
    start,
    skip
)