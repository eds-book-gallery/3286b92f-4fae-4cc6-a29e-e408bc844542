import sys
sys.path.append('../src')
import numpy as np
import matplotlib.pyplot as plt
import general.CreateDataName as cn
import general.Iterator as it
import general.plotting as rfplt
import xarray as xr

from general.constants import *


def load_mitgcm_data(data_raw_path):
    """Load original data"""
    
    ori = xr.open_dataset(f"{data_raw_path}cat_tave.nc")
    
    return ori


def mask_data(df):
    """Land mask"""
    
    land_mask = df['Mask'].values
    return land_mask


def get_exp_name(
    run_vars,
    data_prefix,
    exp_prefix ,
    model_prefix 
    
):
    data_name = f"{data_prefix}{cn.create_dataname(run_vars)}"
    model_name = f"{model_prefix}{data_name}"
    exp_name = f"{exp_prefix}{model_name}"
    
    return exp_name


def load_preds(
    pred_path, exp_nam
):
    
    filename = f'{pred_path}{exp_nam}_AveragedSinglePredictions.nc'
    preds = xr.open_dataset(filename)
    
    return preds

   
def get_av_abs_error(
    data_raw_path, pred_path, run_vars
):

    original = load_mitgcm_data(data_raw_path)
    mask = mask_data(original)
    exp_nam = get_exp_name(
        run_vars,
        data_prefix,
        exp_prefix ,
        model_prefix 
    )
    preds = load_preds(
        pred_path, 
        exp_nam
    )
    
    da_Av_AbsError = preds['Av_AbsErrors'].values
    da_CC = preds['Cor_Coef'].values
    Cor_Coef = np.where(mask==1, da_CC, np.nan)
    avg_err = np.where(mask==1, da_Av_AbsError, np.nan)

    
    return avg_err, preds, exp_nam


def graph_abs_error(
    avg_err,
    preds,
    cbar_label_err, 
    level,
    x_coord,
    exp_nam,
    figs_path
    
):
    fig, ax, im = rfplt.plot_depth_fld(
        avg_err[:,:,:], 
        'Averaged Absolute Errors', 
        level,
        preds['X'].values, 
        preds['Y'].values, 
        preds['Z'].values,
        text='(a)', 
        title=None, 
        min_value=0.0, 
        max_value=0.000306, 
        cmap='Reds',
        Sci=True
    )
    plt.show()
    plt.savefig(
        f"{figs_path}{exp_nam}_AvAbsErrors_z{str(level)}.png", 
        bbox_inches = 'tight', 
        pad_inches = 0.1, 
        format='png'
    )

    fig, ax, im = rfplt.plot_xconst_crss_sec(
        avg_err[:,:,:], 
        'Averaged Absolute Errors',
        x_coord,
        preds['X'].values, 
        preds['Y'].values, 
        preds['Z'].values,
        text='(b)', 
        title=None, 
        min_value=0.0, 
        max_value=0.000306, 
        cmap='Reds',
        cbar_label=cbar_label_err, 
        Sci=True
    )
    plt.show()
    
    plt.savefig(
        f"{figs_path}{exp_nam}_AvAbsErrors_x{str(x_coord)}.png", 
        bbox_inches = 'tight', 
        pad_inches = 0.1, 
        format='png'
    )

def main_pattern_errors(
    run_vars=run_vars,
    data_raw_path=data_raw_path, 
    pred_path=pred_path,
    cbar_label_err=cbar_label_err,
    level=level,
    x_coord=x_coord,
    figs_path=figs_path,
):
    avg_err, preds, exp_nam = get_av_abs_error(
        data_raw_path, pred_path, run_vars
    )
    
    graph_abs_error(
        avg_err,
        preds,
        cbar_label_err,
        level,
        x_coord,
        exp_nam,
        figs_path
    )
    
main_pattern_errors()