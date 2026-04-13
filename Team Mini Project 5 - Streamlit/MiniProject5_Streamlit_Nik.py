# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 21:06:10 2026

@author: nikol
"""
#Imports
import streamlit as st
from streamlit_folium import folium_static
import folium
import requests
import pandas as pd
import matplotlib.pyplot as plt

#Reading wine csv files
red = pd.read_csv(r"C:\Users\nikol\Downloads\DS-450\MiniProject5\winequality-red.csv", sep = ';', header = 0)
white = pd.read_csv(r"C:\Users\nikol\Downloads\DS-450\MiniProject5\winequality-white.csv", sep = ';', header = 0)
red = pd.DataFrame(red)
white = pd.DataFrame(white)
#Concatenating the two datasets as one with the added 'Type' column
red['Type'] = 'red'
white['Type'] = 'white'
data = pd.concat([red, white], ignore_index = True)
data = data.reset_index()
data.rename(columns = {'index': 'Observation'}, inplace = True)

#Title and tabs
st.title('Mini Project 5: Wine Quality Viewer 🍷')
st.caption('DS-450: Samia, Sal, Nik')

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['MetaData', 'Data', 'Color', 'Quality', 'Scatter', 'Box', 'Classification'])
#Note to ourselves: Make sure to indent all content specific to a given tab.
with tab1:
    st.header('Meta Data')

with tab2:
    st.header('Dataset Viewer')
    st.caption('Note: Click through the column names to reorder by ascending/descending.')
    #First Creating a dictionary for the different columns for each radio button
    
    select1 = {
        'Chemical':['Type', 'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates'],
        'Alcohol': ['Type', 'alcohol'],
        'Quality': ['Type', 'quality'],
        'All': ['Type', 'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol', 'quality']
        }
    
    #Now establishing the button
    radio1 = st.radio('Chose dataset view:',select1.keys())
    columns = select1[radio1]
    df_view = data[columns]
    st.dataframe(df_view)
    
    #st.write(data[columns])
    #pd.set_option('display.max_columns', None)
        
    
    

with tab3:
    st.header('Color Distribution')
    bar = data['Type'].value_counts().plot(kind = 'bar')
    bar.bar_label(bar.containers[0])
    #plt.title('Count of Red vs White Wines')
    plt.xlabel('Type')
    plt.ylabel('Count')
    plt.xticks(rotation = 60)
    plt.yticks(rotation = 60)
    st.pyplot(plt)


with tab4:
    st.header('Quality Distribution')



with tab5:
    st.header('Scatter Plots')



with tab6:
    st.header('Box Plots')



with tab7:
    st.header('Classification Report')










