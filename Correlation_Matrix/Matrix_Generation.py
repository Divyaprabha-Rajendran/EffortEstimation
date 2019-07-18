from prettytable import PrettyTable

import EffortEstimation.Correlation_Matrix.Chi_SquareTest as chi
import EffortEstimation.Correlation_Matrix.Data_Preparation as dp
import EffortEstimation.Correlation_Matrix.Pearson_Product as ppm
from EffortEstimation.Correlation_Matrix import ANOVA_Test as anova, Chi_SquareTest

categorical_cols=["ASIL","ObjType","VerifCritSW","Priority"]
Numerical_cols=["StoryPoints","Estimate","TimeSpent","Links"]

def Numerical_Correlation(Numerical_list,logger):
    Pearson_list=[]
    for i in range(0,len(Numerical_list)):
        for j in range(0,len(Numerical_list)):
            Pearson_list.append(Numerical_cols[i]+" and "+Numerical_cols[j]+"  "+str(ppm.Spearman(Numerical_list[i],Numerical_list[j],logger)))
    return  Pearson_list


def Anova_Correlation(Numerical_list,Categorical_list):
    Anova_list = []
    for i in range(0,len(Categorical_list)):
        for j in range(0,len(Numerical_list)):
            grouped_list=anova.data_groupby(Categorical_list[i],Numerical_list[j])
            Anova_list.append(categorical_cols[i]+" and "+Numerical_cols[j]+"     "+anova.anova_f_statistic(grouped_list))
    return Anova_list

def Categorical_Correlation(data):
    chi_square_list=[]
    Categorical_data=["ASIL","ObjType","VerifCritSW","Priority"]
    for i in range(0,len(Categorical_data)):
        for j in range(i+1,len(Categorical_data)):
            #print (Categorical_data[i],Categorical_data[j])
            chi_square_list.append(categorical_cols[i]+" and "+categorical_cols[j]+"  "+str(chi.chi_square_test(data,Categorical_data[i],Categorical_data[j])))
    return chi_square_list

def Draw_matrix_Numeric(statistic_list,name,rows,cols):
    table = PrettyTable(categorical_cols)
    print (table)

def print_results(lists):
    for each in lists:
        print (each)
