import numpy as np
import pandas as pd
import pickle

import streamlit as st

def app():
    st.title('Heart Disease  Checkup')
    name = st.text_input("Name:")
    age = st.number_input("Age:", min_value=0, step=1)
    sex = st.text_input("Sex - Male/ Female:")
    cp =  st.number_input("Chest Pain type: ", min_value=0, max_value=3, step=1)
    restbps = st.number_input("Resting blood pressure:", min_value=0, step=1)
    cholestrol = st.number_input("Serum cholestoral in mg/dl:", min_value=0, step=1)
    fbs = st.number_input("Fasting blood sugar > 120 mg/dl", min_value=0, max_value=1, step=1)
    rest_ecg = st.number_input("Resting electrocardiographic results (values 0,1,2):", min_value=0, max_value=1, step=1)
    max_hr = st.number_input("maximum heart rate", min_value=0, step=1)
    angina = st.number_input("exercise induced angina", min_value=0, max_value=1, step=1)
    oldpeak = st.number_input("ST depression induced by exercise relative to rest")
    slope = st.number_input("Slope of the peak exercise ST segment", min_value=0, max_value=2, step=1)
    ca = st.number_input("Number of major vessels (0-3) colored by flourosopy", min_value=0, max_value=2, step=1)
    thal = st.number_input("thal: 3 = normal; 6 = fixed defect; 7 = reversable defect", min_value=1, max_value=3, step=1)
    
    submit = st.button('Predict')

    patient_data = pd.DataFrame([[age, sex, cp, restbps, cholestrol, fbs, rest_ecg, max_hr, angina, oldpeak, slope, ca, thal]], columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'])

    pickle_in = open('Heart_model', 'rb')
    classifier = pickle.load(pickle_in)

    result = classifier.predict(patient_data)

    if result == 0:
        st.write('Congratulations ' , name, ', You do not have any type of heart disease.')

    else :
        st.write(name, 'We are really sorry, you seem to have a heart disease, you must consult your doctor.')
