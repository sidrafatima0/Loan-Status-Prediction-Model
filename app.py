import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("loan_status_predict")

# Streamlit UI
def main():
    st.title("Loan Status Prediction")
    st.write("Enter details to predict loan approval status")
    
    # User input fields
    gender = st.selectbox("Gender", [1, 0], format_func=lambda x: "Male" if x == 1 else "Female")
    married = st.selectbox("Married", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
    dependents = st.number_input("Dependents", min_value=0, max_value=10, step=1)
    education = st.selectbox("Education", [1, 0], format_func=lambda x: "Graduate" if x == 1 else "Not Graduate")
    self_employed = st.selectbox("Self Employed", [1, 0], format_func=lambda x: "Yes" if x == 1 else "No")
    applicant_income = st.number_input("Applicant Income", min_value=0.0, step=100.0)
    coapplicant_income = st.number_input("Coapplicant Income", min_value=0.0, step=100.0)
    loan_amount = st.number_input("Loan Amount", min_value=0.0, step=1.0)
    loan_term = st.number_input("Loan Amount Term (in days)", min_value=0.0, step=1.0)
    credit_history = st.selectbox("Credit History", [1, 0], format_func=lambda x: "Good" if x == 1 else "Bad")
    property_area = st.selectbox("Property Area", [0, 1, 2], format_func=lambda x: ["Rural", "Semiurban", "Urban"][x])
    
    if st.button("Predict"):
        input_data = pd.DataFrame({
            "Gender": [gender],
            "Married": [married],
            "Dependents": [dependents],
            "Education": [education],
            "Self_Employed": [self_employed],
            "ApplicantIncome": [applicant_income],
            "CoapplicantIncome": [coapplicant_income],
            "LoanAmount": [loan_amount],
            "Loan_Amount_Term": [loan_term],
            "Credit_History": [credit_history],
            "Property_Area": [property_area]
        })
        
        result = model.predict(input_data)
        if result[0] == 1:
            st.success("Loan Approved ✅")
        else:
            st.error("Loan Not Approved ❌")

if __name__ == "__main__":
    main()
