import os
import sys
import numpy as np
import pandas as pd

#Include your library path in sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

#Include your Library
from graph_library.pltgraph import Plot
from graph_library.csvreader import csv_data

#save_path = save figure
#data_path = csv file path
save_path = os.path.join(os.path.dirname(__file__), 'figure')
data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data\\exp_0.6_1.6_.._4.6_tri_0_5V_100kOhm_100Ohm_IB_VCE.csv')

#data = dictionary format data from WaveForms exported raw data
data = csv_data(data_path)

# variables in Plot
# Plot(X = data['V1'], Y = data['V2'], X_unit = 'V', Y_unit = 'V', X_name = '$V_1$', Y_name = '$V_2$', graph_name = 'example', save_path = save_path, linear_fit = True, File_format = 'pdf')
# default: linear_fit = False, File_format = 'pdf'

Plot(data['V1'], data['V2'], 'V', 'V', '$V_1$', '$V_2$', 'example', save_path, True, 'pdf')