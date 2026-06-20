import streamlit as st

st.set_page_config(page_title="Motapa Calculator", page_icon="⚖️")

st.title("⚖️ Motapa Calculator")
st.caption("Weighing in on your life choices since today.")

name = st.text_input("Enter your Name")
gender = st.selectbox("Select Your Gender", ["Male", "Female"])
weight = st.number_input("Weight (kg)", min_value=0.0, step=0.5)
height_cm = st.number_input("Height (cm)", min_value=0.0, step=0.5)

if st.button("Calculate BMI"):
    if not name.strip():
        st.warning("We need a name — even calculators like to be personal.")
    elif height_cm == 0:
        st.warning("Height can't be zero — unless you're a Roomba.")
    elif weight == 0:
        st.warning("Weight can't be zero — gravity disagrees with that.")
    else:
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        bmi_rounded = round(bmi, 1)

        st.write("Your BMI is:", bmi_rounded)

        if bmi < 18.5:
            st.write("Underweight — looks like you're skipping more than just the gym!")
        elif bmi < 25:
            st.write("Normal — balanced like a true equilibrium.")
        elif bmi < 30:
            st.write("Overweight — a little extra to love, but your knees are filing a complaint.")
        else:
            st.write("Obese — your BMI called, it wants a gym membership as a gift.")