import streamlit as st

st.header("Motapa Calculator")
name = st.text_input("Enter your Name")
weight = st.number_input("Enter your Weight in kg")
height = st.number_input("Enter your Height in meters")
st.selectbox("Select Your Gender", ["Male", "Female"])

if st.button("Calculate BMI"):
    if height == 0:
        st.write("Please enter a valid height.")
    else:
        bmi = weight / (height ** 2)
        st.write("You BMI is: ", round(bmi, 1))
        if bmi < 18.5:
            st.write("You are Underweight")
        elif bmi < 25:
            st.write("You are Normal")
        elif bmi < 30:
            st.write("You are Overweight")
        else:
            st.write("You are Obese")