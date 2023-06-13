import pickle
import os
import numpy as np
import sys
sys.path.append('../src')
from general.constants import *
import plotting as rfplt
import xarray as xr
import time as tt
import matplotlib.pyplot as plt

def make_error_plots(mitgcm_filename,exp_name,cntrl_name):
    #-------------------
    # Read in land mask 
    #-------------------
    mitgcm_ds = xr.open_dataset(mitgcm_filename)
    land_mask = mitgcm_ds['Mask'].values
    da_T = mitgcm_ds['Ttave'].values


    data_filename=pred_path+exp_name+'_AveragedSinglePredictions.nc'
    ds = xr.open_dataset(data_filename)
    da_Av_Error=ds['Av_Errors'].values
    da_Av_AbsError=ds['Av_AbsErrors'].values
    da_wtd_Av_Error=ds['Weighted_Av_Errors'].values
    da_CC=ds['Cor_Coef'].values

    cntrl_filename = pred_path+cntrl_name+'_AveragedSinglePredictions.nc'
    cntrl_ds = xr.open_dataset(cntrl_filename)
    da_cntrl_Av_AbsError=cntrl_ds['Av_AbsErrors'].values
    da_cntrl_CC=cntrl_ds['Cor_Coef'].values

    #Plotting Cross-section at 13 degrees East
    point = [ 2, 8, 6]
    level = point[0]
    y_coord = point[1]
    x_coord = point[2]

    # mask data
    Av_Error = np.where(land_mask==1, da_Av_Error, np.nan)
    Av_AbsError = np.where(land_mask==1, da_Av_AbsError, np.nan)
    wtd_Av_Error = np.where(land_mask==1, da_wtd_Av_Error, np.nan)
    Cntrl_Av_AbsError = np.where(land_mask==1, da_cntrl_Av_AbsError, np.nan)
    Cor_Coef = np.where(land_mask==1, da_CC, np.nan)
    Cntrl_Cor_Coef = np.where(land_mask==1, da_cntrl_CC, np.nan)

    z_size = Av_Error.shape[0]
    y_size = Av_Error.shape[1]
    x_size = Av_Error.shape[2]

    #print('Av_Error.shape')
    #print(Av_Error.shape)
    print("\n ================================================")
    print("\n Plotting the absolute error from predictions across the grid at 500 different times averaged to give a spatial pattern of errors. \n")
    print("================================================\n")

    
    fig, ax, im = rfplt.plot_xconst_crss_sec(Av_AbsError[:,:,:], 'Averaged Absolute Errors', x_coord,
                                         mitgcm_ds['X'].values, mitgcm_ds['Y'].values, mitgcm_ds['Z'].values,
                                         text='(a)', title=None, min_value=0.0, max_value=0.000306, cmap='Reds',
                                         cbar_label=cbar_label, Sci=True)
    plt.show()

    
    
    #Plot x cross section of difference between cntrl and exp
    print("\n ================================================")

    print("\n Plotting the difference between this and the control run, with areas shaded in red indicating where the error has increased as a consequence of withholding information about the vertical structure, and blue indicating areas where the predictions are improved. \n")

    print("================================================\n")

    
    fig, ax, im = rfplt.plot_xconst_crss_sec(
    Av_AbsError[:,:,:]-Cntrl_Av_AbsError, 
    'Diff in Averaged Absolute Errors with Control Run', 
    x_coord,
    mitgcm_ds['X'].values, mitgcm_ds['Y'].values, mitgcm_ds['Z'].values,
    text='(b)', title=None, min_value=None, max_value=None, diff=True,
    cbar_label=cbar_label, Sci=True)
    plt.show()
    
    
  