# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 17:18:34 2023

@author: Ehsan
"""

from aisp.NSA import RNSA

# Importing other packages. 
import numpy as np
import seaborn as sns
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from vdk.api.job_input import IJobInput

def AIS(train_x, test_x, train_y, accuracy_list):
    
    number_of_antibodies = input("Enter the number of antibodies: ")
    print("You entered:", number_of_antibodies)

    self_radius = input("Enter the radius of antibodies: ")
    print("Antibodies radius:", self_radius)

    self_antigens_radius = input("Enter the radius of self-antigens: ")
    print("Self antigens radius:", self_antigens_radius)

    nsa = RNSA(N = int(number_of_antibodies), r = float(self_antigens_radius), r_s = float(self_radius), algorithm='V-detector')

    for i in range(0, 100):
    
        # Split the training set, setting aside 1/10 of the data for validation.
        train_model_x, valid_x, train__model_y, valid_y = train_test_split(train_x, train_y, test_size=0.1)

        # Fit the model using the other 90% of the data
        nsa.fit(train_model_x, train__model_y.values, verbose=True)

        # Accuracy calculation for validation set:
        prev_y = nsa.predict(valid_x)
        accuracy_list.append(accuracy_score(prev_y, valid_y))

        # Display the mean accuracy and its standard deviation
        print(f"The average accuracy is: {np.average(np.array(accuracy_list)):.6f}")
        print(f"Standard deviation of accuracies: {np.std(np.array(accuracy_list)):.6f}")

        # Creating the model with all data separated for training.
        nsa.fit(train_x, train_y.values)
        print('Model Total Adjusted!')

        # Previewing classes with test samples.
        prev_y = nsa.predict(test_x)

    return accuracy_list, train_x, train_y, prev_y, nsa

def DT(train_x, test_x, train_y, random_state, accuracy_list):
   
     # Split the dataset into training and testing sets
    train_model_x, valid_x, train__model_y, valid_y = train_test_split(train_x, train_y, test_size=0.2, random_state = int(random_state))

    # Create a decision tree classifier
    clf = DecisionTreeClassifier(random_state = int(random_state))

    clf.fit(train_model_x, train__model_y.values)

    # Accuracy calculation for validation set:
    prev_y = clf.predict(valid_x)
    accuracy_list.append(accuracy_score(prev_y, valid_y))

    # Previewing classes with test samples.
    prev_y = clf.predict(test_x)
   
    return accuracy_list, train_x, train_y, prev_y, clf

def RF(train_x, test_x, train_y, random_state, accuracy_list):
   
     # Split the dataset into training and testing sets
    train_model_x, valid_x, train__model_y, valid_y = train_test_split(train_x, train_y, test_size=0.2, random_state = int(random_state))

    # Create a decision tree classifier
    clf =  RandomForestClassifier(random_state = int(random_state))

    clf.fit(train_model_x, train__model_y.values)

    # Accuracy calculation for validation set:
    prev_y = clf.predict(valid_x)
    accuracy_list.append(accuracy_score(prev_y, valid_y))

    # Previewing classes with test samples.
    prev_y = clf.predict(test_x)
   
    return accuracy_list, train_x, train_y, prev_y, clf


def run(job_input: IJobInput) -> None:

    # Specify the path to the csv file
    # csv_file_path = 'beta.csv'

    # Read the CSV file into a DataFrame
    #data = pd.read_csv(csv_file_path)
    
    # read sqlite query results into a pandas Dataframe

    con = sqlite3.connect("beta.db")
    data = pd.read_sql_query("SELECT * from m1;", con)

    #if isinstance(data, pd.Series):
    #     data = data.to_frame()

    features = data.iloc[:,:-1]
    classes = data.iloc[:,-1]
    
    # PCA adoption

    components = input("Enter the number of PCA components, your number must be between zero and " + str(features.shape[1]) + " : ")
    print("You entered:", components)
    pca = PCA(n_components= int(components))
    features = pca.fit_transform(features) 

    # Generating the training and testing sets.
    train_x, test_x, train_y, test_y = train_test_split(features, classes, test_size=0.30)

    accuracy_list = list()

    # Model Initialization
    which_method = input("Tell me which methodology do you want to choose for your discrimination task?\n Type 1 for Artificial Immune System \n Type 2 for Decision Tree\n Type 3 for Random Forests --> ")
    print("You have entered:", which_method)

    # condition 
    if which_method == '1':
        
        accuracy_list, train_x, train_y, prev_y, nsa = AIS(train_x, test_x, train_y, accuracy_list)
        # Showing the accuracy of predictions for actual data.
        print("The accuracy is {accuracy_score(prev_y, test_y.values)}")
        print(classification_report(test_y.values, prev_y))

        ft = nsa 


    elif which_method == '2':
        random_state = input("Please input random state size: ")

        # default value is 42
        print("Entered random state size is : ", random_state)
        accuracy_list, train_x, train_y, prev_y, clf = DT(train_x, test_x, train_y, random_state, accuracy_list)    
    
        # Showing the accuracy of predictions for actual data.
        print("The accuracy is {accuracy_score(prev_y, test_y.values)}")
        print(classification_report(test_y, prev_y))

        ft = clf

    elif which_method == '3':
        random_state = input("Please input random state size: ")


        print("Entered random state size is : ", random_state)
        accuracy_list, train_x, train_y, prev_y, clf = RF(train_x, test_x, train_y, random_state, accuracy_list)    
    
        # Showing the accuracy of predictions for actual data.
        print("The accuracy is {accuracy_score(prev_y, test_y.values)}")
        print(classification_report(test_y, prev_y))

        ft = clf


    # Generating the confusion matrix and plotting it graphically.
    mat = confusion_matrix(y_true=test_y.values, y_pred=prev_y)
    ar = list(set(classes))
    ar.reverse()
    sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False, xticklabels=ar, yticklabels=ar)
    plt.xlabel('Real')
    plt.ylabel('Estimated')
    plt.show()