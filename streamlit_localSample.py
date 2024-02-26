import streamlit as st
import pandas as pd

st.title("RCM session")

# Local student data
training_data= pd.read_csv(r"C:\Users\quadi\OneDrive\Documents\Desktop\DataScienceRCM\2-PythonAndRbyVenktesan\1-assn-pythonWebAppSample\RCMsession.csv")

# Streamlit app
st.title('Student Training App')

# Display the training data
st.header('Training Data')
st.table(training_data)

# Filter data based on completion status
status_filter = st.selectbox('Filter by Completion Status:', ['All', 'Completed', 'Incomplete'])
filtered_data = training_data if status_filter == 'All' else training_data[training_data['Status'] == status_filter]

# Display filtered data
st.header('Filtered Training Data')
st.table(filtered_data)

# Summary statistics
st.header('Summary Statistics')
st.write(f"Total Courses: {len(training_data)}")
st.write(f"Total Completed Courses: {len(training_data[training_data['Status'] == 'Completed'])}")
st.write(f"Total Incomplete Courses: {len(training_data[training_data['Status'] == 'Incomplete'])}")
