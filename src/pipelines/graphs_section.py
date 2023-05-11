"""
Plots instantaneous fields from 
MITgcm dataset
multiple cross sections
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import xarray as xr

sys.path.append('../src/general/')
from constants import *
from netCDF4 import Dataset


def load_data(path_data):
    """Read in netcdf file and get shape
    """
    
    print('Reading in ds ...')
    da = xr.open_dataset(path_data)
    # Apply the Mask
    dam = np.where(
        da['Mask']==1, 
        da['Ttave'][time:time+2,:,:,:],
        np.nan
    )
    print(f'Shape: {dam.shape}')

    return dam, da


def set_plot_pars():
    
    plt.rcParams.update({'font.size': 10})
    plt.rc('font', family='sans serif')
    plt.rc('xtick', labelsize='x-small')
    
    return plt


def plot_depth_fields(
    select,
    min_value, 
    max_value, 
    x_label, 
    y_label, 
    lon_arange, 
    lat_arange,
    da_x, 
    da_y,
    name_o,
    lab,
    cmap
):
    plt = set_plot_pars()
    fig = plt.figure(figsize=(2.5, 4.5), dpi=300)
    ax = fig.add_subplot(1, 1, 1)
    im = ax.pcolormesh(
        select, 
        vmin=min_value, 
        vmax=max_value, 
        edgecolors='face', 
        snap=True,
        cmap=cmap
    )
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_xticks(lon_arange)
    ax.set_xticklabels(
        np.round(da_x.values[np.array(lon_arange).astype(int)], decimals=-1).astype(int)
    ) 
    ax.set_yticks(lat_arange)
    ax.set_yticklabels(
        np.round(da_y.values[np.array(lat_arange).astype(int)], decimals=-1).astype(int)
    ) 
    plt.text(-0.1, 0.86, lab, transform=fig.transFigure)
    plt.savefig(
        f"{plotdir}{name_o}", 
        format='png', 
        bbox_inches = 'tight', 
        pad_inches = 0.1
    )
    return plt, im, ax
    
    
    
def plot_cross_sections(
    select,
    min_value, 
    max_value,
    lat_label,
    depth_label,
    lat_arange,
    depth_arange,
    da_y,
    da_z,
    name_o,
    lab,
    cmap
):
    plt = set_plot_pars()
    fig = plt.figure(figsize=(3.6, 2.0), dpi=300)
    ax = fig.add_subplot(1, 1, 1)
    im = ax.pcolormesh(
        select,
        vmin=min_value, 
        vmax=max_value, 
        edgecolors='face', 
        snap=True,
        cmap=cmap
    )
    ax.invert_yaxis()
    ax.set_xlabel(lat_label)
    ax.set_ylabel(depth_label)
    ax.set_xticks(lat_arange)
    ax.set_xticklabels(
        np.round(da_y.values[np.array(lat_arange).astype(int)], decimals=-1).astype(int)
    ) 
    ax.set_yticks(depth_arange)
    ax.set_yticklabels(da_z.values[np.array(depth_arange)].astype(int))
    plt.text(-0.055, 0.86, lab, transform=fig.transFigure)
    plt.savefig(
        f"{plotdir}{name_o}", 
        format='png',
        bbox_inches = 'tight', 
        pad_inches = 0.1
    )
    
    return plt
