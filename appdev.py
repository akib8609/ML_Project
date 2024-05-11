import streamlit as st

def diabetic_risk_calculator(age, bmi, family_history, exercise_hours):
    # Simple logic for calculating risk score
    risk_score = 0
    if age >= 40:
        risk_score += 1
    if bmi >= 25:
        risk_score += 1
    if family_history:
        risk_score += 1
    if exercise_hours < 2:
        risk_score += 1

    return risk_score

def main():
    st.title("Diabetic Risk Calculator")

    # User input
    age = st.slider("Age", min_value=18, max_value=100, value=40)
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
    family_history = st.checkbox("Family history of diabetes")
    exercise_hours = st.slider("Hours of exercise per week", min_value=0, max_value=20, value=2)

    # Calculate risk
    risk_score = diabetic_risk_calculator(age, bmi, family_history, exercise_hours)

    # Display risk
    st.subheader("Diabetic Risk Score")
    st.write(f"Your risk score is: {risk_score}")

    if risk_score >= 3:
        st.write("You are at higher risk of developing diabetes. Please consult your healthcare provider.")
    else:
        st.write("You are at lower risk of developing diabetes. Keep up the good work!")

if __name__ == "__main__":
    main()
