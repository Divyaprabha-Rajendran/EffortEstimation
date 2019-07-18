import os
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

def get_data(All_data_list,matrix_path):
    #print (All_data_list)
    #print (os.getcwd())
    df = pd.DataFrame({'ASIL': All_data_list[0],
                       'ObjType': All_data_list[1],
                       'VerifCritSW':All_data_list[2],
                       'Priority':All_data_list[3],
                       'Estimate':All_data_list[4],
                       'StoryPoints':All_data_list[6],
                       'Links':All_data_list[7],
                       'TimeSpent': All_data_list[5]})

    writer = ExcelWriter(matrix_path)
    df.to_excel(writer, 'Sheet1', index=False)
    writer.save()
    writer.close()

def random_data(matrix_path_1,matrix_path_2):
    pass