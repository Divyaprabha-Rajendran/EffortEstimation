import pandas as pd
import scipy.stats as stats
import numpy as np

def data_groupby_pandas(data_req,group):
    group_by = data_req.groupby(group)
    print ([group_by.get_group(x) for x in group_by.groups])

def data_groupby(list1,list2):
    unique=set(list1)
    grouped_list={}
    for each in unique:
        value_list=[]
        for i in range(0,len(list1)):
            if each==list1[i]:
                value_list.append(list2[i])
        grouped_list[each]=value_list
    return  grouped_list

def anova_f_statistic(value_dict):
    value_list_array = []
    for key, value in value_dict.items():
        if (len(value) > 1):
            value_list_array.append(value)
    F, p = stats.f_oneway(value_list_array)
    #print('F statistic = {:5.3f} and probability p = {:5.3f}'.format(F, p))
    return ('{:5.3f} , {:5.3f}'.format(F, p))








































