import numpy as np
import pandas as pd
import pickle

import streamlit as st

def app():
    st.title('Liver Disease  Checkup')
    name = st.text_input("Name:")
    age = st.number_input("Age:", min_value=0, step=1)
    gender = st.text_input("Sex - Male/ Female")
    total_bilirubin =  st.number_input("Total Bilirubin:")
    direct_bilirubin = st.number_input("Direct Bilirubin:")
    ak = st.number_input("Alkaline Phosphotase:", min_value=0, step=1)
    alamine_atf = st.number_input("Alamine Aminotransferase:", min_value=0, step=1)
    aspartate_atf = st.number_input("Aspartate Aminotransferase:", min_value=0, step=1)
    total_proteins = st.number_input("Total Protiens:")
    albumin = st.number_input('Albumin:')
    a_g_ratio = st.number_input('Ablumin & Globulin ratio:')
    

    submit = st.button('Predict')

    patient_data = pd.DataFrame([[age, gender, total_bilirubin, direct_bilirubin, ak, alamine, aspartate_atf, total_proteins, albumin, a_g_ratio]], columns=['Age', 'Gender', 'Total_Bilirubin', 'Direct_Bilirubin', 'Alkaline_Phosphotase', 'Alamine_Aminotransferase', 'Aspartate_Aminotransferase', 'Total_Proteins', 'Albumin', 'Albumin_and_Globulin_Ratio'])

    pickle_in = open('Liver_model', 'rb')
    classifier = pickle.load(pickle_in)

    result = classifier.predict(patient_data)

    if result == 0:
        st.write('Congratulations ' , name, ', You are not have any kind of liver disease.')

    else :
        st.write(name, 'We are really sorry, you seem to have some kind of liver disease, you must consult your doctor.')

