import logging
import os
import pandas as pd

import Matrix_Generation as cm
import Data_Visualization as dv
import Data_Preparation as dp


def Read_Data(path):
    data = pd.read_excel(path)
    data_required=data[['ASIL','ObjType','VerifCritSW','Priority','StoryPoints','Estimate','TimeSpent','Links','Parentpriority']]
    return data,data_required

def Prepare_Data(data_required):
    All_data_list=[]
    ASIL_list=dp.check_data(list(data_required['ASIL']),"DEF")
    All_data_list.append(ASIL_list)
    ObjType_list=dp.check_data(list(data_required['ObjType']),"default")
    All_data_list.append(ObjType_list)
    VerifCritSW_list=dp.check_data(list(data_required['VerifCritSW']),"default")
    All_data_list.append(VerifCritSW_list)
    Priority_list=dp.check_priority(list(data_required['Priority']),"default",list(data_required['Parentpriority']))
    All_data_list.append(Priority_list)
    Estimate_list=dp.convert_to_hours(list(data_required['Estimate']))
    All_data_list.append(Estimate_list)
    TimeSpent_list=dp.convert_to_hours(list(data_required['TimeSpent']))
    All_data_list.append(TimeSpent_list)
    StoryPoints_list=dp.check_story_pts(list(data_required['StoryPoints']),TimeSpent_list,8.5)
    All_data_list.append(StoryPoints_list)
    Links_list=list(data_required['Links'])
    All_data_list.append(Links_list)
    return All_data_list

def Generate_Correlation(Numerical_list,Categorical_list,data,logger):
    Pearson_statistic = cm.Numerical_Correlation(Numerical_list, logger)
    Anova_ststistic = cm.Anova_Correlation(Numerical_list, Categorical_list)
    #Chi_square_statistic = cm.Categorical_Correlation(data)
    cm.print_results(Pearson_statistic)
    print ("********************************************************************************")
    cm.print_results(Anova_ststistic)
    print ("********************************************************************************")
    #cm.print_results(Chi_square_statistic)
    #print ("********************************************************************************")


def Matrix_Execution(data_path):
    logging.basicConfig(filename=os.getcwd()+"Effort_Estimation.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
    logger=logging.getLogger()
    logger.setLevel(logging.DEBUG)


    #data_path=""
    data,data_required=Read_Data(data_path)

    All_data_list=Prepare_Data(data_required)

    Attributes_list = ['ASIL', 'ObjType', 'VerifCritSW', 'Priority', 'StoryPoints', 'Estimate', 'TimeSpent', 'Links']
    #dv.Univariate_Numerical_Plot(Attributes_list,All_data_list[4:8])
    dv.Univariate_Categorical_Plot(data_required)


    Numerical_list=[]
    Categorical_list=[]

    for each in All_data_list:
        if 'str' in str(type(each[0])):
            Categorical_list.append(each)
        else:
            Numerical_list.append(each)

    #Generate_Correlation(Numerical_list,Categorical_list,data,logger)
    return All_data_list


Matrix_Execution("path/to/data/file")
# Generate_univariate_graph(data_required,Attributes_list)
#dv.Univariate_Numerical_Plot(Attributes_list,Numerical_list)
#dv.Univariate_Categorical_Plot(data_required)
#dv.Bivariate_Categorical_plot(data_required,"VerifCritSW","Priority")
#dv.Bivariate_Numerical_plot(All_data_list,"StoryPoints","Links")
#dv.Univariate_scatter_plot(All_data_list)
#dv.Categorical_scatter_plot(data_required,"ASIL","Links")
