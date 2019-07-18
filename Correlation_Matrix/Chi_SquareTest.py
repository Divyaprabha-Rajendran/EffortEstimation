import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

import EffortEstimation.Correlation_Matrix.Data_Visualization as norm


def find_col_length(data_list):
    unique=set()
    for each in data_list:
        if "str" not in str(type(each)) or "-" in each:
            continue
        else:
            unique.add(each)
    print (len(unique))

def chi_square_test(data,col1,col2):
    data_list1=data[col1]
    data_list2=data[col2]
    data = []
    contingency_table=pd.crosstab(data_list1,data_list2,margins=True,dropna=True)
    for i in range(0, len(contingency_table) - 1):
        temp_list= (contingency_table.iloc[i][0:len(set(data_list2))-1].values)
        data.append(temp_list)
    f_obs = np.array([data])
    return ((stats.chi2_contingency(f_obs)[0:2]))


