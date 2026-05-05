import streamlit as st
import requests

st.title("Mental Health Risk Predictor")


gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=15, max_value=40, value=20)
cgpa = st.number_input("CGPA", min_value=0.0, max_value=4.0, value=3.0)

academic_pressure = st.slider("Academic Pressure", 1, 5, 3)
financial_concerns = st.slider("Financial Concerns", 1, 5, 3)
social_relationships = st.slider("Social Relationships", 1, 5, 3)
study_satisfaction = st.slider("Study Satisfaction", 1, 5, 3)


gender_encoded = 1 if gender == "Male" else 0


if st.button("Predict Risk"):
    
    input_data = {
        'gender': gender_encoded,
        'age': age,
        'cgpa': cgpa,
        'academic_pressure': academic_pressure,
        'financial_concerns': financial_concerns,
        'social_relationships': social_relationships,
        'study_satisfaction': study_satisfaction
    }

    try:
        response = requests.post(
            "http://127.0.0.1:5000/predict",
            json=input_data
        )

        if response.status_code == 200:
            result = response.json()

            if "Risk_Level" in result:
                st.success(f"Predicted Risk Level: {result['Risk_Level']}")
            else:
                st.error(result)

        else:
            st.error("API request failed")

    except Exception as e:
        st.error(f"Connection error: {e}")