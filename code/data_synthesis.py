# Load package
from pathlib import Path
import pandas as pd
import numpy as np
import pickle
import os, sys

#%%
with open('../configuration.txt', 'r') as f:
    lines = f.readlines()
project_path = lines[0].split("'")[1]
file_name = lines[1].split("'")[1]
epsilon_list = lines[2].split('=')[1].split(',')
epsilon_list = list(map(float, epsilon_list)) #change as number form

os.sys.path.append(project_path)
from syndp.algorithm import original_timedp as odp

# read_data
project_dir = Path(project_path)
data_dir = project_dir.joinpath('data')

pd.read_csv(data_dir.joinpath())

# %%
