# Taxi-Trip-Price-Prediction-Using-Linear-Regression-and-Streamlit

This project involves cleaning a dataset, building a linear regression model to predict taxi trip prices, and creating a user interface using Streamlit to interact with the model and make predictions on new data.

## Table of Contents

- [Description](#description)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Description

This project was assigned as part of a learning assignment to practice data cleaning, model building, and UI creation. The task involved:
1. Cleaning the `taxi_trip_pricing.csv` dataset.
2. Building a linear regression model to predict taxi trip prices.
3. Saving the model.
4. Creating a Streamlit UI to load the saved model and make predictions on new data inputs.

## Dataset

The dataset, `taxi_trip_pricing.csv`, contains the following features:
- **Trip_Distance_km**: Distance of the trip in kilometers.
- **Time_of_Day**: Time of the day the trip started (e.g., Morning, Afternoon).
- **Day_of_Week**: Day of the week the trip took place.
- **Passenger_Count**: Number of passengers in the trip.
- **Traffic_Conditions**: Traffic conditions during the trip (e.g., Low, Moderate, High).
- **Weather**: Weather conditions during the trip (e.g., Clear, Rainy).
- **Base_Fare**: The base fare for the trip.
- **Per_Km_Rate**: Rate per kilometer.
- **Per_Minute_Rate**: Rate per minute.
- **Trip_Duration_Minutes**: Duration of the trip in minutes.
- **Trip_Price**: The total price of the trip (target variable).

## Project Structure

- `taxi_trip_pricing.csv`: The dataset used for training the model.
- `LR.ipynb`: Jupyter notebook containing the data cleaning, model training, and evaluation.
- `streamlit_app.py`: Streamlit application to interact with the trained model.
- `linear_regression_model.pkl`: Saved linear regression model.
- `requirements.txt`: List of dependencies to run the project.
- `README.md`: Documentation for the project.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jojojoester/taxi-trip-price-prediction.git
   ```

2. Navigate to the project directory:
   ```bash
   cd taxi-trip-price-prediction
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

2. Open the application in your browser and input the trip details to get a predicted trip price.

## Features

- Data cleaning and preprocessing.
- Linear regression model training and evaluation.
- Interactive user interface with Streamlit.
- Real-time predictions based on user inputs.


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Thanks to [Programiz](https://www.programiz.com) for the intermediate Python course.
- Dataset sourced from [Kaggle](https://www.kaggle.com).
- Special thanks to my instructor for assigning this project.
