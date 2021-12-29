import numpy as np
import pandas as pd
import pickle

import streamlit as st

def app():
    st.title('Diabetes  Checkup')
    name = st.text_input("Name:")
    pregnancy = st.number_input("No. of times pregnant:", min_value=0, step=1)
    glucose = st.number_input("Plasma Glucose Concentration :", min_value=0, step=1)
    bp =  st.number_input("Diastolic blood pressure (mm Hg):", min_value=0, step=1)
    skin = st.number_input("Skin fold thickness (mm):", min_value=0, step=1)
    insulin = st.number_input("Insulin (mu U/ml):", min_value=0, step=1)
    bmi = st.number_input("Body mass index:")
    dpf = st.number_input("Diabetes Pedigree Function:")
    age = st.number_input("Age:", min_value=0, step=1)

    submit = st.button('Predict')

    patient_data = pd.DataFrame([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]], columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

    pickle_in = open('Diabetes_model.pkl', 'rb')
    classifier = pickle.load(pickle_in)

    result = classifier.predict(patient_data)

    if result == 0:
        st.write('Congratulations ' , name, ', You are not diabetic.')

    else :
        st.write(name, 'We are really sorry, you seem to be diabetic, you must consult your doctor.')
