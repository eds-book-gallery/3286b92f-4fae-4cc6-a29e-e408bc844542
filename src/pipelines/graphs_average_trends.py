"""
Plots avergaged fluxes 
outputted creating spatial 
patterns of average trends
"""

import matplotlib.pyplot as plt
import xarray as xr
import itertools
import sys
sys.path.append('../../')
import src.general.plotting as rfplt

from src.general.constants import *
from itertools import zip_longest


def load_aveg_trend(
    data_interm_path
):
    """Load average trends"""
    
    filename=f"{data_interm_path}avera_trend.nc"
    dat = xr.open_dataset(filename)
    
    return dat


def graph_loops(
    plt, 
    dat, 
    figs_path, 
    text_avgs, 
    vars_avgs, 
    x_coord, 
    label_avgs
):
    for var in vars_avgs: 
        avg = dat[var].values
        fig, ax, im = rfplt.plot_xconst_crss_sec(
           avg[:,:,:],
           vars_avgs[var], 
           x_coord,
           dat['X'].values, 
           dat['Y'].values, 
           dat['Z'].values,
           text=text_avgs[var], 
           title=None, 
           min_value=None, 
           max_value=None, 
           diff=False,
           cmap='Reds', 
           cbar_label=label_avgs, 
           Sci=True
       )
        plt.savefig(
           f'{figs_path}fig02{text_avgs[var]}.png', 
            bbox_inches = 'tight', 
            pad_inches = 0.1, 
            format='png'
        )    
    
def get_ave_gra(
    vars_avgs, 
    names_avgs, 
    text_avgs, 
    data_interm_path, 
    figs_path,
    x_coord,
    label_avgs
):
    plt = rfplt.plot_parms()
    dat = load_aveg_trend(data_interm_path)
    vars_avgs = dict(zip_longest(vars_avgs, names_avgs,fillvalue=''))
    text_avgs = dict(zip_longest(vars_avgs, text_avgs,fillvalue=''))
    
    graph_loops(plt, dat, figs_path, text_avgs, vars_avgs, x_coord, label_avgs)
    

get_ave_gra(
    vars_avgs=vars_avgs, 
    names_avgs=names_avgs, 
    text_avgs=text_avgs, 
    data_interm_path=data_interm_path, 
    figs_path=figs_path,
    x_coord=x_coord,
    label_avgs=label_avgs
)