import streamlit as st
import pickle
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# load model 
with open("log_model.pkl",'rb') as f:
    model = pickle.load(f)

# Load Encoder
with open("sex_encoder.pkl",'rb') as f:
    sex_enc = pickle.load(f)

with open("emb_encoder.pkl",'rb') as f:
    emb_enc = pickle.load(f)

# Set UI title
st.title("Titanic Survival Prediction")

sex_option = list(sex_enc.classes_)
emb_option = list(emb_enc.classes_)
psngr_class = [1,2,3]
# user input

Pclass = st.selectbox("Passenger Class",psngr_class)
sex  = st.selectbox("Passenger Sex",sex_option)
Age = st.slider("Passenger Age",min_value=0,max_value=80,)
SibSp = st.slider("SibSp",min_value=0,max_value=8)
Parch = st.slider("Parch",min_value = 0,max_value = 6)
Fare = st.number_input("Fair Paid",min_value=0,format="%0.2f")
Embarked = st.selectbox("Embarked",emb_option)


sex_encoder = sex_enc.transform([sex])[0]
emb_encoder = emb_enc.transform([Embarked])[0]


# Predict

if st.button("Predict"):
    input_data = np.array([[Pclass,sex_encoder,Age,SibSp,Parch,Fare,emb_encoder]])
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][prediction]

    if prediction == 1:
        st.success(f"Survived and probability {probability:2f}")
    else:
        st.error(f"Not Survived and probability {probability:2f}")