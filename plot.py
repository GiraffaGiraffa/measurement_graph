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
data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\1.1.1k.c.csv'
data = csv_data(data_path)
Plot([data['time'], data['time']], [data['V1'], data['V2']], 's', 'V', '$time$', '$voltage$', '1.1.1k.c', save_path, False, 'pdf', labels = ('$V_{out}$', '$V_{in}$'))

data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\1.1.1k.s.csv'
data = csv_data(data_path)
Plot([data['time'], data['time']], [data['V1'], data['V2']], 's', 'V', '$time$', '$voltage$', '1.1.1k.s', save_path, False, 'pdf', labels = ('$V_{out}$', '$V_{in}$'))

data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\1.1.1k.t.csv'
data = csv_data(data_path)
Plot([data['time'], data['time']], [data['V1'], data['V2']], 's', 'V', '$time$', '$voltage$', '1.1.1k.t', save_path, False, 'pdf', labels = ('$V_{out}$', '$V_{in}$'))

data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\1.1.10.s.csv'
data = csv_data(data_path)
Plot([data['time'], data['time']], [data['V1'], data['V2']], 's', 'V', '$time$', '$voltage$', '1.1.10.s', save_path, False, 'pdf', labels = ('$V_{out}$', '$V_{in}$'))

data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\1.2.1k.c.csv'
data = csv_data(data_path)
Plot([data['time'], data['time']], [data['V1'], data['V2']], 's', 'V', '$time$', '$voltage$', '1.2.1k.c', save_path, False, 'pdf', labels = ('$V_{out}$', '$V_{in}$'))

data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\1.2.1k.t.csv'
data = csv_data(data_path)
Plot([data['time'], data['time']], [data['V1'], data['V2']], 's', 'V', '$time$', '$voltage$', '1.2.1k.t', save_path, False, 'pdf', labels = ('$V_{out}$', '$V_{in}$'))


# variables in Plot
# Plot(X = data['V1'], Y = data['V2'], X_unit = 'V', Y_unit = 'V', X_name = '$V_1$', Y_name = '$V_2$', graph_name = 'example', save_path = save_path, linear_fit = True, File_format = 'pdf', label = 'None')
# default: linear_fit = False, File_format = 'pdf'

# single plot and linear regression
