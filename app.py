# Demo code

import streamlit as st

# streamlit UI
st.title("Power Calculator")
st.write("Enter a number to calculate its square, cube and fourth power.")

# Get user input
number = st.number_input("Enter a number:", value=1, step=1)

# Calculate powers
square = number ** 2
cube = number ** 3
fourth_power = number ** 4

# Display results
st.write(f"Square of {number} is: {square}")
st.write(f"Cube of {number} is: {cube}")
st.write(f"Fourth power of {number} is: {fourth_power}")