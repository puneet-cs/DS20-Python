# Libraries
import joblib  # to use the model and scaler
import pandas as pd  # receive user input in dataframe format
import streamlit as st   # to build frontend
from pathlib import Path   # help to access the files in a folder

# BASE  = DS20_ML_Project
BASE = Path(__file__).parent   # to get the path of parent folder

# download the model using joblib
model = joblib.load(BASE/"artifacts"/"model.joblib")

# download the scaler_data = scaler & cols_to_scale
scaler_data = joblib.load(BASE/"artifacts"/"scaler.joblib")

scaler = scaler_data["scaler"]
scale_cols = scaler_data["cols_to_scale"]

"""
cols_to_scale = ['Age', 'Region', 'Number Of Dependants', 'BMI_Category',
       'Income_Lakhs', 'Medical History', 'Insurance_Plan',
       'Gender_Male', 
       'Smoking_Status_Occasional', 'Smoking_Status_Regular',
       'Employment_Status_Salaried', 'Employment_Status_Self-Employed']

    Gender  :  ['Male' 'Female']
Region  :  ['Northwest' 'Southeast' 'Northeast' 'Southwest']
Marital_status  :  ['Unmarried' 'Married']
BMI_Category  :  ['Normal' 'Obesity' 'Overweight' 'Underweight']
Smoking_Status  :  ['No Smoking' 'Regular' 'Occasional' 'Smoking=0' 'Does Not Smoke'
 'Not Smoking']
Employment_Status  :  ['Salaried' 'Self-Employed' 'Freelancer']
Income_Level  :  ['<10L' '10L - 25L' '> 40L' '25L - 40L']
Medical History  :  ['Diabetes' 'High blood pressure' 'No Disease'
 'Diabetes & High blood pressure' 'Thyroid' 'Heart disease'
 'High blood pressure & Heart disease' 'Diabetes & Thyroid'
 'Diabetes & Heart disease']
Insurance_Plan  :  ['Bronze' 'Silver' 'Gold']
"""

categories = {
    "Insurance_Plan" : {'Bronze':0, 'Silver': 1, 'Gold' : 2},
    "Region" : {'Northwest': 1, 'Southeast': 2, 'Northeast' : 0, 'Southwest':3},
    "BMI_Category"  :  {'Normal':0, 'Obesity':1, 'Overweight':2, 'Underweight':3},
    'Medical History' : {
                'Diabetes' : 6,
                'High blood pressure' : 6,
                'Heart disease' : 8,
                'Thyroid' : 5,
                'No Disease' : 0,
                'Diabetes & High blood pressure' : 12,
                'High blood pressure & Heart disease' : 14,
                'Diabetes & Heart disease' : 14,
                'Diabetes & Thyroid' : 11
                    },
    "Gender" : {"Female" : 0, "Male":1},
    "Smoking_Status"  :  {'No Smoking' : (0,0), 'Regular' : (0,1), 'Occasional' : (1,0) },
    "Employment_Status"  :  {'Salaried':(1,0),  'Self-Employed':(0,1),  'Freelancer' : (0,0)}
}



