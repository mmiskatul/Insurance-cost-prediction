import streamlit as st 
import pandas as pd 
import numpy as np 
import joblib 


scaler =joblib.load("scaler.pkl") 
le_gender =joblib.load("label_encoder_gender.pkl") 
le_diabetic =joblib.load("label_encoder_diabetic.pkl") 
le_smoker =joblib.load("label_encoder_smoker.pkl") 
model =joblib.load("Best model.pkl")
