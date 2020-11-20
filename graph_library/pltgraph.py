#보류
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy import stats
import os
import sys
import pandas as pd
from matplotlib.pyplot import errorbar
def scale(xmax):
    if xmax>1e9:
        return 1e9, 'G'
    elif xmax>1e6:
        return 1e6, 'M'
    elif xmax>1e3:
        return 1e3, 'k'
    elif xmax>1:
        return 1, ''
    elif xmax>1e-3:
        return 1e-3,'m'
    elif xmax>1e-6:
        return 1e-6,'$\mu$'
    else:
        return 1e-9,'n'

def Plot(X, Y, X_unit, Y_unit, X_name, Y_name, graph_name, save_path, linear_fit = False, File_format = 'pdf'):
    X = np.array(X)
    Y = np.array(Y)
    plt.rc('font', size = 13)
    plt.rcParams["font.family"] = "Times New Roman"
    Xscale, xunit_prefix = scale(max(abs(X)))
    Yscale, yunit_prefix = scale(max(abs(Y)))

    #linear reggretion
    if linear_fit:
        x_llim = min(X)
        x_rlim = max(X)
        plt.title('Correlation between '+X_name+' and '+Y_name)
        fit_x = np.array(X)
        fit_y = np.array(Y)
        slope, intercept, r_value, p_value, std_err = stats.linregress(fit_x, fit_y)
        print('linear regression')
        print('y = (%f) + (%f) * x' % (intercept, slope))
        print('r^2 = %f' % r_value**2)
        print('R_DUT = ', slope)
        print('tau = ', -1/slope)
        x_reggression = np.linspace(x_llim, x_rlim, 10)
        y_reggression = intercept + slope * x_reggression

        #scale fitted line
        x_reggression/=Xscale
        y_reggression/=Yscale

        plt.plot(x_reggression, y_reggression, label='fitted', color = 'blue', linewidth = 2)
    else:
        plt.title('Curve between '+X_name+' and '+Y_name)

    #scale
    X/=Xscale
    Y/=Yscale
    
    plt.xlabel(X_name+'['+xunit_prefix+X_unit+']')
    plt.ylabel(Y_name+'['+yunit_prefix+Y_unit+']')

    plt.plot(X, Y,'.', label='experiment', markersize = 2, color = 'black')

    plt.legend()
    plt.savefig(os.path.join(save_path, graph_name+'.'+File_format))
    plt.show()