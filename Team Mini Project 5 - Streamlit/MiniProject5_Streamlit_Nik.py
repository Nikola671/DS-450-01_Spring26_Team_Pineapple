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

# Imports for classification model
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

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
    st.subheader('Dataset Shape')
    st.write(f'Rows: {data.shape[0]}')
    st.write(f'Columns: {data.shape[1]}')

    st.subheader('Column Names')
    col_df = pd.DataFrame({'Column': data.columns})
    st.dataframe(col_df, use_container_width = True)

    st.subheader('Data Types')
    dtype_df = data.dtypes.reset_index()
    dtype_df.columns = ['Column', 'Data Type']
    st.dataframe(dtype_df, use_container_width = True)

    st.subheader('Missing Values')
    missing_df = data.isnull().sum().reset_index()
    missing_df.columns = ['Column', 'Missing Values']
    st.dataframe(missing_df, use_container_width = True)

    st.subheader('Summary Statistics')
    st.dataframe(data.describe(include = 'all'), use_container_width = True)


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


with tab4: # samia code
    st.header('Quality Distribution')

    # Count wines by quality
    quality_counts = data['quality'].value_counts().sort_index()

    # Create bar plot
    fig, ax = plt.subplots()
    quality_counts.plot(kind='bar', ax=ax)

    # Labels and formatting
    ax.set_xlabel('Quality Score')
    ax.set_ylabel('Number of Wines')
    ax.set_title('Distribution of Wine Quality Scores')

    # Add labels on top of bars
    for container in ax.containers:
        ax.bar_label(container)

    # Display in Streamlit
    st.pyplot(fig)



with tab5: # samia code
    st.header('Scatter Plots')
    st.caption('Choose two features to compare with a scatterplot')

    # Get numeric columns only (important for scatterplots)
    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns.tolist()

    st.write("Select exactly TWO features:")

    # Store selected features
    selected_features = []

    # Create checkboxes
    # get the columns from the list of numeric columns
    for col in numeric_cols:
        # create checkboxes using these columns and appending to the selected features list
        if st.checkbox(col):
            selected_features.append(col)

    # Logic for scatterplot
    # if two boxes (features) are selected from the selected features list
    if len(selected_features) == 2:
        x_feature = selected_features[0] # the first feature selected is assigned to the x-axis
        y_feature = selected_features[1] # the second feature selected is assigned to the y-axis

        # create scatterplot
        fig, ax = plt.subplots()
        ax.scatter(data[x_feature], data[y_feature], alpha=0.5)

        # set the axis labels and title
        ax.set_xlabel(x_feature)
        ax.set_ylabel(y_feature)
        ax.set_title(f'{y_feature} vs {x_feature}')

        # show the scatterplot
        st.pyplot(fig)

    # If more than 2 features are selected, tell user to select only two features
    elif len(selected_features) > 2:
        st.warning("Please select only TWO features.")

    # If no features are selected, tell user to select two features 
    else:
        st.info("Select two features to display the scatterplot.")



with tab6:
    st.header('Box Plots')

    select2 = {
        'Fixed Acidity': 'fixed acidity',
        'Volatile Acidity': 'volatile acidity',
        'Citric Acid': 'citric acid',
        'Residual Sugar': 'residual sugar',
        'Chlorides': 'chlorides',
        'Free Sulfur Dioxide': 'free sulfur dioxide',
        'Total Sulfur Dioxide': 'total sulfur dioxide',
        'Density': 'density',
        'pH': 'pH',
        'Sulphates': 'sulphates',
        'Alcohol': 'alcohol',
        'Quality': 'quality'
        }

    radio2 = st.radio('Chose boxplot to view:', list(select2.keys()))
    columns2 = select2[radio2]

    fig, ax = plt.subplots()
    ax.boxplot(data[columns2])

    ax.set_title(f'Box Plot of {columns2}')
    ax.set_ylabel(columns2)
    st.pyplot(fig)


with tab7:
    st.header('Classification Report')

    # Step 1: Prepare data
    df = data.copy()

    # Step 2: Features (X) and target (y)
    X = df.drop(['quality', 'Type'], axis=1) # features
    y = df['quality'] # target

    # Step 3: Train-test split (80/20)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Step 4: Train the Random Forest model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Step 5: Predictions
    y_pred = model.predict(X_test)

    # Step 6: Classification report
    st.subheader("Classification Report")
    report = classification_report(y_test, y_pred, output_dict=True)
    st.dataframe(pd.DataFrame(report).transpose().round(2), use_container_width=True)

    # Step 7: Feature importance
    st.subheader("Feature Importance")

    importance = pd.Series(model.feature_importances_, index=X.columns)
    importance = importance.sort_values(ascending=False)

    # Step 8: Plot the feature importance bar chart
    fig, ax = plt.subplots(figsize=(12, 8))
    importance.plot(kind='bar', ax=ax)

    # Add the title and axis labels
    ax.set_xlabel("Features", fontsize=15.5, labelpad=10)
    ax.set_ylabel("Importance Score", fontsize=15.5, labelpad=10)

    # Bigger tick labels
    ax.tick_params(axis='x', labelsize=13)
    ax.tick_params(axis='y', labelsize=13)

    # Add labels on top of bars
    for container in ax.containers:
        ax.bar_label(container, fmt='%.2f', fontsize=15)
    
    st.pyplot(fig)










