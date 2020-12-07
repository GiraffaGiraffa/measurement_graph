import os
import sys
import numpy as np
import pandas as pd

#Include your library path in sys
#sys.path.append(os.path.dirname(os.path.dirname(__file__)))
#sys.path.append(os.getcwd())

#Include your Library
from graph_library.pltgraph import Plot
from graph_library.csvreader import csv_data

save_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\figure'
data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\3.0.1.csv'
data = csv_data(data_path)
Plot(data['time'], data['V1'], 's', 'V', '$time$', '$voltage$', '3.0.1', save_path, False, 'pdf', labels = ('$V_{out}$'))

data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\3.0.2.csv'
data = csv_data(data_path)
Plot(data['time'], data['V1'], 's', 'V', '$time$', '$voltage$', '3.0.2', save_path, False, 'pdf', labels = '$V_{out}$')

data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\3.0.3.csv'
data = csv_data(data_path)
Plot(data['time'], data['V1'], 's', 'V', '$time$', '$voltage$', '3.0.3', save_path, False, 'pdf', labels = '$V_{out}$')

data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\3.0.4.csv'
data = csv_data(data_path)
Plot(data['time'], data['V1'], 's', 'V', '$time$', '$voltage$', '3.0.4', save_path, False, 'pdf', labels = '$V_{out}$')

data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\3.0.5.csv'
data = csv_data(data_path)
Plot(data['time'], data['V1'], 's', 'V', '$time$', '$voltage$', '3.0.5', save_path, False, 'pdf', labels = '$V_{out}$')

data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\3.1.1.csv'
data = csv_data(data_path)
Plot(data['time'], data['V1'], 's', 'V', '$time$', '$voltage$', '3.1.1', save_path, False, 'pdf', labels = '$V_{out}$')

data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\3.1.2.csv'
data = csv_data(data_path)
Plot(data['time'], data['V1'], 's', 'V', '$time$', '$voltage$', '3.1.2', save_path, False, 'pdf', labels = '$V_{out}$')

data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\3.0.5.fft.csv'
data = csv_data(data_path)
Plot(data['time'], data['V1'], 'Hz', 'dB', '$frequency$', '$intensity$', '3.0.5.fft', save_path, False, 'pdf', labels = '$V_{out}$')

data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\3.2.csv'
data = csv_data(data_path)
Plot(data['time'], data['V1'], 's', 'V', '$time$', '$voltage$', '3.2', save_path, False, 'pdf', labels = '$V_{out}$')

# variables in Plot
# Plot(X = data['V1'], Y = data['V2'], X_unit = 'V', Y_unit = 'V', X_name = '$V_1$', Y_name = '$V_2$', graph_name = 'example', save_path = save_path, linear_fit = True, File_format = 'pdf', label = 'None')
# default: linear_fit = False, File_format = 'pdf'

# single plot and linear regression
