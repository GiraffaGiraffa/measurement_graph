import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy import stats
from matplotlib.pyplot import errorbar

#Include your library path in sys
#sys.path.append(os.path.dirname(os.path.dirname(__file__)))
#sys.path.append(os.getcwd())

#Include your Library
from graph_library.pltgraph import Plot
from graph_library.pltgraph import scale
from graph_library.csvreader import csv_data

save_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\figure'
# data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\1.1.1k.c.csv'
# data = csv_data(data_path)
# Plot([data['time'], data['time']], [data['V1'], data['V2']], 's', 'V', '$time$', '$voltage$', '1.1.1k.c', save_path, False, 'pdf', labels = ('$V_{out}$', '$V_{in}$'))

# data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\1.1.1k.s.csv'
# data = csv_data(data_path)
# Plot([data['time'], data['time']], [data['V1'], data['V2']], 's', 'V', '$time$', '$voltage$', '1.1.1k.s', save_path, False, 'pdf', labels = ('$V_{out}$', '$V_{in}$'))

# data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\1.1.1k.t.csv'
# data = csv_data(data_path)
# Plot([data['time'], data['time']], [data['V1'], data['V2']], 's', 'V', '$time$', '$voltage$', '1.1.1k.t', save_path, False, 'pdf', labels = ('$V_{out}$', '$V_{in}$'))

# data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\1.1.10.s.csv'
# data = csv_data(data_path)
# Plot([data['time'], data['time']], [data['V1'], data['V2']], 's', 'V', '$time$', '$voltage$', '1.1.10.s', save_path, False, 'pdf', labels = ('$V_{out}$', '$V_{in}$'))

# data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\1.2.1k.c.csv'
# data = csv_data(data_path)
# Plot([data['time'], data['time']], [data['V1'], data['V2']], 's', 'V', '$time$', '$voltage$', '1.2.1k.c', save_path, False, 'pdf', labels = ('$V_{out}$', '$V_{in}$'))

# data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\1.2.1k.t.csv'
# data = csv_data(data_path)
# Plot([data['time'], data['time']], [data['V1'], data['V2']], 's', 'V', '$time$', '$voltage$', '1.2.1k.t', save_path, False, 'pdf', labels = ('$V_{out}$', '$V_{in}$'))


data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\1.1.1k.t.csv'
data = csv_data(data_path)
X = [data['time'], data['time']]
Y = [data['V1'], data['V2']]
X_unit = 's'
Y_unit = 'V'
X_name = '$time$'
Y_name = '$voltage$'
graph_name = '1.1.1k.t'
linear_fit = True
File_format = 'pdf'
labels = ('$V_{out}$', '$V_{in}$')
X = np.array(X)
Y = np.array(Y)
plt.rc('font', size = 13)
plt.rcParams["font.family"] = "Times New Roman"

Xscale, xunit_prefix = scale(np.max(np.reshape(abs(X), -1)) - np.min(np.reshape(abs(X), -1)))
Yscale, yunit_prefix = scale(np.max(np.reshape(abs(Y), -1)) - np.min(np.reshape(abs(Y), -1)))
#linear reggretion
if linear_fit:
    a = [0.44183412/Xscale, 0.44283393/Xscale]
    plt.plot(a, [2.5/Yscale, 2.5/Yscale], color = 'blue', linewidth = 2)
else:
    plt.title('Curve between '+X_name+' and '+Y_name)

#scale
X/=Xscale
Y/=Yscale
    
plt.xlabel(X_name+'['+xunit_prefix+X_unit+']')
plt.ylabel(Y_name+'['+yunit_prefix+Y_unit+']')

if len(X.shape)==1:
    plt.plot(X, Y,'.', label= 'experiment' if linear_fit else None, markersize = 2, color = 'black')
else:
    if(len(labels) != X.shape[0]):
        print('len of label != input #')
        exit()
    for i in range(X.shape[0]):
        plt.plot(X[i], Y[i], label = labels[i], markersize = 2)
plt.legend()
plt.savefig(os.path.join(save_path, graph_name+'.'+File_format))
plt.show()


data_path = 'C:\\Users\\giraa\\source\\repos\\measurement_graph\\data\\1.2.1k.t.csv'
data = csv_data(data_path)
X = [data['time'], data['time']]
Y = [data['V1'], data['V2']]
X_unit = 's'
Y_unit = 'V'
X_name = '$time$'
Y_name = '$voltage$'
graph_name = '1.2.1k.t'
linear_fit = True
File_format = 'pdf'
labels = ('$V_{out}$', '$V_{in}$')
X = np.array(X)
Y = np.array(Y)
plt.rc('font', size = 13)
plt.rcParams["font.family"] = "Times New Roman"

Xscale, xunit_prefix = scale(np.max(np.reshape(abs(X), -1)) - np.min(np.reshape(abs(X), -1)))
Yscale, yunit_prefix = scale(np.max(np.reshape(abs(Y), -1)) - np.min(np.reshape(abs(Y), -1)))
#linear reggretion
if linear_fit:
    a = [0.4425372/Xscale, 0.44353638/Xscale]
    plt.plot(a, [2.5/Yscale, 2.5/Yscale], color = 'blue', linewidth = 2)
else:
    plt.title('Curve between '+X_name+' and '+Y_name)

#scale
X/=Xscale
Y/=Yscale
    
plt.xlabel(X_name+'['+xunit_prefix+X_unit+']')
plt.ylabel(Y_name+'['+yunit_prefix+Y_unit+']')

if len(X.shape)==1:
    plt.plot(X, Y,'.', label= 'experiment' if linear_fit else None, markersize = 2, color = 'black')
else:
    if(len(labels) != X.shape[0]):
        print('len of label != input #')
        exit()
    for i in range(X.shape[0]):
        plt.plot(X[i], Y[i], label = labels[i], markersize = 2)
plt.legend()
plt.savefig(os.path.join(save_path, graph_name+'.'+File_format))
plt.show()

# variables in Plot
# Plot(X = data['V1'], Y = data['V2'], X_unit = 'V', Y_unit = 'V', X_name = '$V_1$', Y_name = '$V_2$', graph_name = 'example', save_path = save_path, linear_fit = True, File_format = 'pdf', label = 'None')
# default: linear_fit = False, File_format = 'pdf'

# single plot and linear regression
