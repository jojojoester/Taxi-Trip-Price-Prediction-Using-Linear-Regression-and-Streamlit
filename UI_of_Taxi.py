import streamlit as st
import pandas as pd
import joblib  # Assuming you saved your model using joblib
from sklearn.linear_model import LinearRegression

# Load the model (Make sure to save your trained model as 'linear_regression_model.pkl' in the same directory)
model = joblib.load('regression.pkl')

# Define the input fields
st.title('Taxi Trip Price Prediction')
st.header('Input the features to predict the trip price')

Trip_Distance_km = st.number_input('Trip Distance (km)', min_value=0.0, step=0.1)
Time_of_Day = st.selectbox('Time of Day', ['Morning', 'Afternoon', 'Evening', 'Night'])
Day_of_Week = st.selectbox('Day of the Week', ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
Passenger_Count = st.number_input('Passenger Count', min_value=1, max_value=6, step=1)
Traffic_Conditions = st.selectbox('Traffic Conditions', ['Low', 'Moderate', 'High'])
Weather = st.selectbox('Weather', ['Clear', 'Rainy', 'Snowy'])
Base_Fare = st.number_input('Base Fare', min_value=0.0, step=0.1)
Per_Km_Rate = st.number_input('Per Km Rate', min_value=0.0, step=0.01)
Per_Minute_Rate = st.number_input('Per Minute Rate', min_value=0.0, step=0.01)
Trip_Duration_Minutes = st.number_input('Trip Duration (Minutes)', min_value=0.0, step=1.0)

# Map categorical inputs to numerical values (use the same encoding as used in your training)
time_of_day_map = {'Morning': 0, 'Afternoon': 1, 'Evening': 2, 'Night': 3}
day_of_week_map = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
traffic_conditions_map = {'Low': 0, 'Moderate': 1, 'High': 2}
weather_map = {'Clear': 0, 'Rainy': 1, 'Snowy': 2}

# Convert input data to DataFrame
input_data = pd.DataFrame({
    'Trip_Distance_km': [Trip_Distance_km],
    'Time_of_Day': [time_of_day_map[Time_of_Day]],
    'Day_of_Week': [day_of_week_map[Day_of_Week]],
    'Passenger_Count': [Passenger_Count],
    'Traffic_Conditions': [traffic_conditions_map[Traffic_Conditions]],
    'Weather': [weather_map[Weather]],
    'Base_Fare': [Base_Fare],
    'Per_Km_Rate': [Per_Km_Rate],
    'Per_Minute_Rate': [Per_Minute_Rate],
    'Trip_Duration_Minutes': [Trip_Duration_Minutes]
})

# Prediction
if st.button('Predict Trip Price'):
    prediction = model.predict(input_data)
    st.success(f'Predicted Trip Price: ${prediction[0]:.2f}')
