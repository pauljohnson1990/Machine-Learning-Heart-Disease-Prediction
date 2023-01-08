
import streamlit as st
import pickle
import numpy as np

load_model = pickle.load(open('heart_pred.sav', 'rb'))
scaler_age = pickle.load(open('scaler_age.sav', 'rb'))
scaler_trestbps = pickle.load(open('scaler_trestbps.sav', 'rb'))
scaler_chol = pickle.load(open('scaler_chol.sav', 'rb'))
scaler_thalach = pickle.load(open('scaler_thalach.sav', 'rb'))
scaler_oldpeak = pickle.load(open('scaler_oldpeak.sav', 'rb'))


def heart_disease_prediction(input_data):
    input_data = np.array(input_data)
    input_data[0] = scaler_age.transform(input_data[0].reshape(1, -1))
    input_data[3] = scaler_trestbps.transform(input_data[3].reshape(1, -1))
    input_data[4] = scaler_chol.transform(input_data[4].reshape(1, -1))
    input_data[7] = scaler_thalach.transform(input_data[7].reshape(1, -1))
    input_data[9] = scaler_oldpeak.transform(input_data[9].reshape(1, -1))
    input_pred = load_model.predict(input_data.reshape(1, -1))
    if input_pred == 1:
        return ("The person has possibilities of Heart Disease")
    else:
        return ("The person has less possibility of having a heart disease")


def main():
    st.title('Heart Disease Predictor')

    def str_to_int(h):
        d=1
        if '.' in h:
            d=10**(len(h)-(h.index('.')+1))
            h=h.replace('.','')
        s=0
        for a in h:
            s= int(h)
        return (s/d)

    Age = st.text_input('Enter Age:')
    Age = str_to_int(Age)

    Sex_M = 0
    Sex = st.radio('Select Sex:', ['M', 'F'])
    if Sex == 'M':
        Sex_M = 1

    Chest_Pain = 0
    Chest_Pain_Type = st.radio("Select Type of Chest Pain : ",
                               ['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'])
    if Chest_Pain_Type == 'Typical Angina':
        Chest_Pain = 0
    elif Chest_Pain_Type == 'Atypical Angina':
        Chest_Pain = 1
    elif Chest_Pain_Type == 'Non-Anginal Pain':
        Chest_Pain = 2
    elif Chest_Pain_Type == 'Asymptomatic':
        Chest_Pain = 3

    RestingBP = st.text_input('Enter Resting BP: ')
    RestingBP = str_to_int(RestingBP)

    Cholesterol = st.text_input('Enter Cholesterol Level:')
    Cholesterol = str_to_int(Cholesterol)

    Fasting_BS = 0
    FastingBS_level = st.radio("If Fasting Blood Sugar > 120mg/dl", ["Yes", 'NO'])
    if FastingBS_level == 'Yes':
        Fasting_BS = 1

    resting_ecg = 0
    resting_ecg_res = st.radio("Select Resting Electro Cardiograph Results :", ['Normal',
                                                                                'Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of >0.05 mV',
                                                                                'Showing probable or definite left ventricular hypertrophy'])
    if resting_ecg_res == 'Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of >0.05 mV':
        resting_ecg = 1
    elif resting_ecg_res == 'Showing probable or definite left ventricular hypertrophy':
        resting_ecg = 2

    Max_HR_Ach = st.text_input("Enter Maximum Heartrate Achieved")
    Max_HR_Ach = str_to_int(Max_HR_Ach)

    E_I_A = 0
    EIA = st.radio("Exercise Induced angina : ", ["Yes", "No"])
    if EIA == "Yes":
        E_I_A = 1

    oldpeak = st.text_input('ST depression induced by exercise relative to rest:')
    oldpeak = str_to_int(oldpeak)

    slope = 0
    slope_pe = st.radio("the slope of the peak exercise ST segment: ", ['Down', 'Flat', 'Up'])
    if slope_pe == 'Down':
        slope = 0
    elif slope_pe == "Flat":
        slope = 1
    elif slope_pe == "Up":
        slope = 2

    major_vessels = st.radio("Number of major vessels (0-3) colored by flourosopy", ['0', '1', '2', '3'])
    major_vessels = str_to_int(major_vessels)

    thal = 0
    Thalassemia = st.radio("Enter Thalassemia :", ["Normal", "Fixed Defect", "Reversable Defect"])
    if Thalassemia == "Normal":
        thal = 0
    elif Thalassemia == "Fixed Defect":
        thal = 1
    elif Thalassemia == "Reversable Defect":
        thal = 2

    diagnosis = ''
    input_data=[Age, Sex_M, Chest_Pain, RestingBP, Cholesterol, Fasting_BS, resting_ecg,
                                              Max_HR_Ach, E_I_A, oldpeak, slope, major_vessels, thal]
    if st.button("Click for Results"):
        diagnosis = heart_disease_prediction(input_data)
        st.success(input_data)
        st.success(diagnosis)


if __name__ == '__main__':
    main()