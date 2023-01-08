# Machine-Learning-Heart-Disease-Prediction
Predicting if a person has heart disease or not using different features
dataset: https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset/download?datasetVersionNumber=2
This data set dates from 1988 and consists of four databases: Cleveland, Hungary, Switzerland, and Long Beach V.
It contains 76 attributes, including the predicted attribute, but all published experiments refer to using a subset of 14 of them.
The "target" field refers to the presence of heart disease in the patient. It is integer valued 0 = no disease and 1 = disease.
Deployment done through Streamlit, the deployment code file hdpred.py will be better to open in Pycharm and in the terminal please give the below command
streamlit run 'path of .py file'
About Dataset Columns:
1.	age
2.	sex
3.	chest pain type (4 values) [TA: Typical Angina, ATA: Atypical Angina, NAP: Non-Anginal Pain, ASY: Asymptomatic]
4.	resting blood pressure
5.	serum cholestoral in mg/dl
6.	fasting blood sugar > 120 mg/dl
7.	resting electrocardiographic results (values 0,1,2)0: Normal  1: Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of >0.05 mV) 2: Showing probable or definite left ventricular hypertrophy
8.	maximum heart rate achieved
9.	exercise induced angina
10.	oldpeak = ST depression induced by exercise relative to rest
11.	the slope of the peak exercise ST segment  ['Down','Flat','Up' ]
12.	number of major vessels (0-3) colored by flourosopy
13.	thal: 0 = normal; 1 = fixed defect; 2 = reversable defect
The Jupyter notebook gives the EDA, preprocessing and model building details. Different Algorithms were compared and voting done to get the best model.
