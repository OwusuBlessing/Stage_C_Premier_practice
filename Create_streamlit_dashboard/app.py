# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:51:32 2022"""
import streamlit as st
import pandas as pd

st.title("My Custom streamlit dashboard")
df= pd.read_csv("C:/Users/user/Desktop/DATA_SCIENCE/HamoyeInternship/StageC_premier/UK_Traffic_Accidents_2015.csv",low_memory=False)
st.write(df.head())
g = df["Accident_Severity"].value_counts()
st.pyplot(g)