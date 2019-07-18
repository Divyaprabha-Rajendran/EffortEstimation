import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from os import listdir as list

file_list= (list("C:\\Users\\dia5cob\\Desktop\\NAP\\NAP-Forms"))

df = pd.DataFrame(file_list)
writer = ExcelWriter("C:\\Users\\dia5cob\\Desktop\\NAP\\NAP_Forms_list.xlsx")
df.to_excel(writer, 'Sheet1', index=False)
writer.save()
writer.close()

