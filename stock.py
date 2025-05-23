import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Title
st.title("📈 Stock Price Prediction: AAPL")

# Load saved predictions and actual values
predictions = np.load("predictions.npy")
actual_prices = np.load("actual_prices.npy")

# Plot
fig, ax = plt.subplots()
ax.plot(actual_prices, color='red', label='Actual Price') 
ax.plot(predictions, color='yellow', label='Predicted Price') 
ax.set_title('Stock Price Prediction')
ax.set_xlabel('Time')
ax.set_ylabel('Stock Price')
ax.legend()

st.pyplot(fig)
