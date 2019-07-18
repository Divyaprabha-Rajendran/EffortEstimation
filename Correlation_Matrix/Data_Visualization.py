from matplotlib import pyplot as plt
import pandas as pd
import matplotlib.mlab as mlab
import numpy as np
import scipy.stats
import seaborn as sns



def Univariate_Numerical_Plot(Attribute,data):
    plt.figure(1)
    sns.set(color_codes=True)
    sns.distplot(data[0])
    plt.xlabel(Attribute[4])

    plt.figure(2)
    sns.set(color_codes=True)
    sns.distplot(data[1])
    plt.xlabel(Attribute[5])

    plt.figure(3)
    sns.set(color_codes=True)
    sns.distplot(data[2])
    plt.xlabel(Attribute[6])

    plt.figure(4)
    sns.set(color_codes=True)
    sns.distplot(data[3])
    plt.xlabel(Attribute[7])

    plt.show()

def Univariate_Categorical_Plot(data_required):
    plt.figure(1)
    sns.set(style="darkgrid")
    sns.countplot(x="ASIL", data=data_required[['ASIL']])
    plt.xlabel("ASIL")

    plt.figure(2)
    sns.set(style="darkgrid")
    sns.countplot(x="ObjType", data=data_required[['ObjType']])
    plt.xlabel("ObjType")

    plt.figure(3)
    sns.set(style="darkgrid")
    sns.countplot(x="VerifCritSW", data=data_required[['VerifCritSW']])
    plt.xlabel("VerifCritSW")

    plt.figure(4)
    sns.set(style="darkgrid")
    sns.countplot(x="Priority", data=data_required[['Priority']])
    plt.xlabel("Priority")

    plt.show()

def Bivariate_Categorical_plot(data_required,attribute1,attribute2):
    #print (data_required[[attribute1,attribute2]])
    sns.set(style="darkgrid")
    sns.countplot(x=attribute1,hue=attribute2, data=data_required[[attribute1,attribute2]])
    plt.xlabel(attribute1)
    plt.ylabel(attribute2)
    plt.show()

def Bivariate_Numerical_plot(data_required,attribute1,attribute2):
    plt.scatter(data_required[4],data_required[5], label= "stars", color= "green",
            marker= "*")
    plt.xlabel(attribute1)
    plt.ylabel(attribute2)
    plt.show()

def Categorical_scatter_plot(data_required,attribute1,attribute2):
    sns.set(style="darkgrid")
    sns.catplot(x=attribute1, y=attribute2,data=data_required[[attribute1,attribute2]]);
    plt.xlabel(attribute1)
    plt.ylabel(attribute2)
    plt.show()
