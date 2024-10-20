import streamlit as st


import numpy as np
import pandas as pd
import time
import matplotlib.pyplot as plt


st.markdown('<h1 class="center">WildFire Data Visualization</h1>', unsafe_allow_html=True)
st.write('<h6 class="center">Data is continuously updated based on sensor inputs.</h6>', unsafe_allow_html=True)


# Generate a date range starting from now with 100 points at 5-minute intervals
date_range = pd.date_range(start='2024-10-19 00:00', periods=50, freq='5T')


# Generate random temperatures between 70 and 90 degrees
temperatures = np.random.uniform(50, 100, size=50)
temperatures_s2 = np.random.uniform(50, 60, size=50)


# Create a DataFrame
#temperature_data_1 = pd.DataFrame({
#    'Time': date_range,
#    'Temperature (°F)': temperatures
#})
#temperature_data_2 = pd.DataFrame({ #second sensor's information
#    'Time': date_range,
#   'Temperature (°F)': temperatures_s2
#})
container = st.beta_container()
all = st.checkbox("Select all")
 
if all:
    selected_options = container.multiselect("Select one or more regions:",
         ['Region 1', 'Region 2'],['Region 1', 'Region 2'])
else:
    selected_options =  container.multiselect("Select one or more options:",
        ['Region 1', 'Region 2'])
   


col1, col2 = st.columns([1, 3]) #set columns for the sensors and data


with col1:
    st.markdown('<h4>Region Sensors</h4>', unsafe_allow_html=True)
    st.write("Region 1")
    st.write("Region 2")
with col2:
    #df = pd.DataFrame(temperature_data_1)
    #df.set_index("Time")
    #df['Temperature (°F)'].plot()




    plt.title("Temperature Over Time")
    plt.xlabel("Time (minutes)")
    plt.ylabel("Temperature (°F)")


    plt.plot(date_range, temperatures, label="sensor1")
    plt.plot(date_range, temperatures_s2, label="sensor2")
    plt.xticks(rotation = 35)
    #plt.legend()
    st.pyplot(plt)
print(date_range)
#st.dataframe(df)


# Centering title
st.markdown(
    """
    <style>
    .center {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)




