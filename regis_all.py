import subprocess
import os
import time
import shutil
from tqdm import tqdm
# import SimpleITK as sitk
# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# from time import time

moving_folder = './data/imagesTr_Contrast/'
fixed_folder = './data/imagesTr_NonContrast/'
moving_label_folder = './data/labelsTr_Contrast/'
infer_label_folder = './data/labelsTr_NonContrast_pred/'

moving_ls = sorted(os.listdir(moving_folder))
fixed_ls = sorted(os.listdir(fixed_folder))
moving_label_ls = sorted(os.listdir(moving_label_folder))

for i in tqdm(range(len(moving_ls))):
    # print(moving_ls[i][:5], fixed_ls[i][:5])
    os.mkdir( './data/reg_FFD/' + moving_ls[i][:5])
    
    subprocess.run('reg_aladin -ref ' + fixed_folder + fixed_ls[i] +
            ' -flo ' + moving_folder + moving_ls[i] +
            ' -res ./data/reg_FFD/' + moving_ls[i][:5] + '/' + moving_ls[i][:5] + '_affine.nii.gz' +
            ' --aff ./data/reg_FFD/' + moving_ls[i][:5] + '/' + moving_ls[i][:5] + '_affine_matrix.txt', shell=True)
    
    subprocess.run('reg_f3d -ref ' + fixed_folder + fixed_ls[i] +
            ' -flo ' + moving_folder + moving_ls[i] +
            ' -res ./data/reg_FFD/' + moving_ls[i][:5] + '/' + moving_ls[i][:5] + '_FFD.nii.gz' +
            ' -aff ./data/reg_FFD/' + moving_ls[i][:5] + '/' + moving_ls[i][:5] + '_affine_matrix.txt' +
            ' -cpp ./data/reg_FFD/' + moving_ls[i][:5] + '/' + moving_ls[i][:5] + '_FFD_cpp.nii.gz', shell=True)
    
    subprocess.run('reg_resample -ref ' + fixed_folder + fixed_ls[i] +
            ' -flo ' + moving_label_folder + moving_label_ls[i] +
            # ' -res ./data/reg_FFD/' + moving_ls[i][:5] + '/' + moving_ls[i][:5] + '_FFD_label_infer.nii.gz' +
            ' -res ' + infer_label_folder + moving_ls[i][:5] + '_FFD_label_infer.nii.gz' +
            ' -cpp ./data/reg_FFD/' + moving_ls[i][:5] + '/' + moving_ls[i][:5] + '_FFD_cpp.nii.gz' +
            ' -inter 0', shell=True)
    
