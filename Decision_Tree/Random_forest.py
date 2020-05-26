import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.metrics import explained_variance_score
from sklearn import preprocessing

def importdata(final_matrix):
    project_data=pd.read_excel(final_matrix)
    #print ("Dataset Lenght: ", len(project_data))
    #print ("Dataset Shape: ", project_data.shape)
    #print ("Dataset: ", project_data.head())
    print ("Data imported successfully")
    label_encoder = preprocessing.LabelEncoder()
    for column_name in project_data.columns:
        if project_data[column_name].dtype == object:
            project_data[column_name] = label_encoder.fit_transform(project_data[column_name])
            print (column_name+"  done")
    #for column_name in project_data.columns:
    #    print (project_data[column_name].dtype)
    return project_data

def splitdataset(project_data):
    X = project_data.values[:, 0:5]
    Y = project_data.values[:, 6]
    Y = Y.astype('int')
    #print (X)
    #print (Y)
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.25, random_state=0)
    print ("Data sliced successfully")
    return X, Y, X_train, X_test, y_train, y_test

def feature_scaling(X_train, X_test):
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    print ("Feature scaling done")
    return X_train, X_test

def Algo_train(X_train, X_test,y_train):
    regressor = RandomForestRegressor(n_estimators=20, random_state=0)
    regressor.fit(X_train, y_train)
    y_pred = regressor.predict(X_test)
    #print (y_pred)
    return y_pred

def Evaluation(y_test,y_pred):
    #print(confusion_matrix(y_test, y_pred))
    #print(classification_report(y_test, y_pred))
    #print(accuracy_score(y_test, y_pred))
    print("Accuracy :")
    print (explained_variance_score(y_test, y_pred, multioutput='uniform_average')* 100)

def print_values(y_test,y_pred):
    print ("Actual value     Predicted value")
    for each in range(0,len(y_pred)-1):
        print (str(y_test[each])+"              "+str(y_pred[each]))

def Run_random_forest(final_matrix):
    project_data=importdata(final_matrix)
    X, Y, X_train, X_test, y_train, y_test=splitdataset(project_data)
    X_train, X_test=feature_scaling(X_train, X_test)
    y_pred=Algo_train(X_train, X_test,y_train)
    Evaluation(y_test,y_pred)
    print_values(y_test,y_pred)


Run_random_forest("path/to/data/file")




