import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
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
    X = project_data.values[:, 0:6]
    Y = project_data.values[:, 7]
    Y = Y.astype('int')
    #print (X)
    #print (Y)
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.25, random_state=100)
    print ("Data sliced successfully")
    return X, Y, X_train, X_test, y_train, y_test

def train_using_gini(X_train, X_test, y_train):
    clf_gini = DecisionTreeClassifier(criterion="gini",
                                      random_state=100, max_depth=3, min_samples_leaf=5)
    clf_gini.fit(X_train, y_train)
    return clf_gini


def tarin_using_entropy(X_train, X_test, y_train):
    clf_entropy = DecisionTreeClassifier(
        criterion="entropy", random_state=100,
        max_depth=3, min_samples_leaf=5)

    clf_entropy.fit(X_train, y_train)
    return clf_entropy


def prediction(X_test, clf_object):
    #print ("inside prediction")
    y_pred = clf_object.predict(X_test)
    print("Predicted values:")
    print(y_pred)
    return y_pred


def cal_accuracy(y_test, y_pred):
    #print ("inside cal_accuracy")
    #print("Confusion Matrix: ",
    #      confusion_matrix(y_test, y_pred))

    print ("Accuracy : ",
           accuracy_score(y_test, y_pred) * 100)

    #print("Report : ",
    #      classification_report(y_test, y_pred))

def Run_decision_tree(final_matrix):
    project_data=importdata(final_matrix)
    X, Y, X_train, X_test, y_train, y_test=splitdataset(project_data)
    clf_gini = train_using_gini(X_train, X_test, y_train)
    clf_entropy = tarin_using_entropy(X_train, X_test, y_train)

    y_pred_gini = prediction(X_test, clf_gini)
    cal_accuracy(y_test, y_pred_gini)

    y_pred_entropy = prediction(X_test, clf_entropy)
    cal_accuracy(y_test, y_pred_entropy)

#project_data=importdata()
#Run_decision_tree()

