import pandas as pd
import scipy.stats as stats


#import EffortEstimation.Correlation_Matrix.Data_Visualization as norm
#from EffortEstimation.Correlation_Matrix import ANOVA_Test as anova


def check_data(data_list,default_value):
    for i in range(0,len(data_list)):
        if "str" not in str(type(data_list[i])):
            data_list[i]=default_value.strip()
            #print ("gotcha")
    return data_list

def check_priority(data_list,default_value,parent):
    for i in range(0,len(data_list)):
        if "str" not in str(type(data_list[i])) or "Unassigned" in data_list[i] :
            if "str" not in str(type(parent[i])) or "Unassigned" not in parent[i] :
                data_list[i]=parent[i]
            else:
                data_list[i] = default_value
    return data_list

def convert_to_hours(data_list):
    for i in range(0,len(data_list)):
        data_list[i]=int(data_list[i])
        if data_list[i] > 0:
            data_list[i]=round(data_list[i]/(1000*60*60),1)
    return data_list

def check_story_pts(data_list,time_list,hours):
    for i in range(0,len(data_list)):
        if "str" not in str(type(data_list[i])) or "not rated" in data_list[i]:
            data_list[i]=round(time_list[i]/hours,0)
        elif "str" in str(type(data_list[i])):
            data_list[i] = data_list[i].replace("pts", "")
            data_list[i] = data_list[i].replace("pt", "")
            data_list[i]=int(data_list[i])
    return data_list


def Print_list(data_list):
    for data in data_list:
        print ((data))
    print ("***************************************")


#Print_list(ASIL_list)
#Print_list(ObjType_list)
#Print_list(VerifCritSW_list)
#Print_list(Priority_list)
#Print_list(Estimate_list)
#Print_list(TimeSpent_list)
#Print_list(StoryPoints_list)

#norm.kernel_distribution(TimeSpent_list)
#norm.kernel_distribution(StoryPoints_list,"StoryPoints")
#norm.kernel_distribution(Links_list,"Links")
#norm.univariate_countplot("ObjType","ObjType",data)
#norm.bivariate_bar_plot("ObjType", "VerifCritSW", data)
#norm.bivariate_bar_plot(ObjType_list,VerifCritSW_list,"ObjType","VerifCritSW")


#norm.plot_normality(StoryPoints_list)
#norm.kernel_distribution(StoryPoints_list,"Storypts")
#F, p = stats.f_oneway(TimeSpent_list,TimeSpent_list)
#print (F,p)

#anova.data_groupby(data_required['ObjType','StoryPoints'],"ObjType")
#value_dict=anova.data_groupby(ObjType_list,StoryPoints_list)
#anova.anova_f_statistic(value_dict)