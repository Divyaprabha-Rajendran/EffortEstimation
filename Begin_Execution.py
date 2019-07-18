import Correlation_Matrix.Effort_Estimation as matrix
import Decision_Tree.Create_Excel as excel
import Decision_Tree.Decision_tree as tree


matrix_path_1="C:\\Users\\dia5cob\\Desktop\\EE\\matrix_data_1.xlsx"
matrix_path_2="C:\\Users\\dia5cob\\Desktop\\EE\\matrix_data_2.xlsx"
final_matrix="C:\\Users\\dia5cob\\Desktop\\EE\\matrix_data.xlsx"

"""
data_path_1="C:\\Users\\dia5cob\\Desktop\\EE\\Data\\Estimation\\EstimatiomSRScdd.xlsx"
All_data_list=matrix.Matrix_Execution(data_path_1)
excel.get_data(All_data_list,matrix_path_1)

data_path_2="C:\\Users\\dia5cob\\Desktop\\EE\\Data\\HMG\\Estimatiom_SRS.xlsx"
All_data_list=matrix.Matrix_Execution(data_path_2)
excel.get_data(All_data_list,matrix_path_2)
"""

tree.Run_decision_tree(matrix_path_1)