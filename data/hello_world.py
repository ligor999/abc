#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import streamlit as st
# import yfinance as yf

# # Create a dictionary of hardcoded username-password pairs
# credentials = {
#     "user1": "password1",
#     "user2": "password2",
#     "asd": "asd",
#     "123":"123"
# }

# # Define a SessionState class to manage app state
# class SessionState:
#     def __init__(self):
#         self.logged_in = False

# # Create a session state instance
# session_state = SessionState()

# # Add a title to your app
# st.title("Login Page")

# # Add input fields for username and password
# username = st.text_input("Username")
# password = st.text_input("Password", type="password")

# # Add a login button
# if st.button("Login"):
#     # Check if the entered credentials match
#     if username in credentials and password == credentials[username]:
#         session_state.logged_in = True
#         st.success("Logged in as {}".format(username))
#     else:
#         st.error("Invalid username or password")

# # Check if logged in
# if session_state.logged_in:
#     # Display stock price app page
#     st.title("Simple Stock Price App")
#     st.write("Shown are the stock closing price and volume of Apple!")

#     # Define the ticker symbol
#     tickerSymbol = 'AAPL'
#     # Get data on this ticker
#     tickerData = yf.Ticker(tickerSymbol)
#     # Get the historical prices for this ticker
#     tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2023-05-31')

#     # Display closing price
#     st.subheader("Closing Price")
#     st.line_chart(tickerDf.Close)

#     # Display volume
#     st.subheader("Volume")
#     st.line_chart(tickerDf.Volume)

#     # Add a logout button
#     if st.button("Logout"):
#         session_state.logged_in = False
#         st.info("Logged out")




# In[ ]:

import streamlit as st
import yfinance as yf

# Create a dictionary of hardcoded username-password pairs
credentials = {
    "user1": "password1",
    "user2": "password2",
    "asd": "asd",
    "123":"123"
}

# Define a SessionState class to manage app state
class SessionState:
    def __init__(self):
        self.logged_in = False

# Create a session state instance
session_state = SessionState()

# Add a title to your app
st.title("Login Page")

# Add input fields for username and password
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Add a login button
if st.button("Login"):
    # Check if the entered credentials match
    if username in credentials and password == credentials[username]:
        session_state.logged_in = True
        st.success("Logged in as {}".format(username))
    else:
        st.error("Invalid username or password")

# Check if logged in
if session_state.logged_in:
    # Display stock price app page
    st.title("Simple Stock Price App")
    st.write("Shown are the stock closing price and volume of Apple!")

    # Define the ticker symbol
    tickerSymbol = 'AAPL'
    # Get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    # Get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2023-05-31')

    # Display closing price
    st.subheader("Closing Price")
    st.line_chart(tickerDf.Close)

    # Display volume
    st.subheader("Volume")
    st.line_chart(tickerDf.Volume)


    st.title("Simple Stock Price App")
    st.write("Shown are the stock closing price and volume of Google!")

    # Define the ticker symbol
    tickerSymbol = 'GOOG'
    # Get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    # Get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2023-05-31')

    # Display closing price
    st.subheader("Closing Price")
    st.line_chart(tickerDf.Close)

    # Display volume
    st.subheader("Volume")
    st.line_chart(tickerDf.Volume)

    st.title("Simple Stock Price App")
    st.write("Shown are the stock closing price and volume of Amazon!")

    # Define the ticker symbol
    tickerSymbol = 'AMZN'
    # Get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    # Get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2023-05-31')

    # Display closing price
    st.subheader("Closing Price")
    st.line_chart(tickerDf.Close)

    # Display volume
    st.subheader("Volume")
    st.line_chart(tickerDf.Volume)

    # Add a logout button
    if st.button("Logout"):
        session_state.logged_in = False
        st.info("Logged out")




# In[ ]:





# In[ ]:




