# Import necessary libraries
import streamlit as st
import pandas as pd
import joblib

# Load the saved Linear Regression model
loaded_model = joblib.load(r'C:\Users\sugar\OneDrive\Desktop\Acc_performance\linear_regression_model.joblib')

# Streamlit app
def main():
    st.title("Student Performance Prediction")

    # Collect user input
    sex = st.selectbox("Sex (0 for female, 1 for male):", [0, 1])
    age = st.slider("Age:", 15,19)
    traveltime = st.number_input("How many time does student needs to travel from school to home:\
                                 (1=> less than 15 min., 2=> 15 to 30 min., 3=> 30 min. to 1 hour, 4=> >1 hour)")
    studytime = st.number_input("Enter the student's study time:\
                                (1=> <2 hours, 2=> 2 to 5 hours, 3=> 5 to 10 hours, or 4=> >10 hours)")
    failures = st.selectbox("Number of past subject failures:",("0","1","2"))
    schoolsup = st.selectbox("Any Extra Educational Support:",("No","Yes"))
    famsup = st.selectbox("Family Educational Support:",("No","Yes"))
    paid   =  st.selectbox("Extra paid classes within the course subject:",("No","Yes"))
    activities =  st.selectbox("Extra-curricular activities:",("No","Yes"))
    nursery   = st.selectbox("Attended nursery school?:",("No","Yes"))
    higher   = st.selectbox("Wants to take higher education:",("No","Yes"))
    internet  =  st.selectbox("Internet access at home:",("No","Yes"))
    romantic  =  st.selectbox("In a romantic relationship:",("No","Yes"))
    health  =  st.selectbox("Current health status(1-least to 5-highest):",("1","2","3","4","5"))
    absences  = st.number_input("Number of school absences (numeric: from 0 to 93)")
    G1    =   st.number_input("Enter Second last Tests Mark(0 to 20):")
    G2    =    st.number_input("Enter latest Tests Mark:(0 to 20)")


    # Convert string inputs to integers
    schoolsup = 1 if schoolsup == "Yes" else 0
    famsup = 1 if famsup == "Yes" else 0
    paid = 1 if paid == "Yes" else 0
    activities = 1 if activities == "Yes" else 0
    nursery = 1 if nursery == "Yes" else 0
    higher = 1 if higher == "Yes" else 0
    internet = 1 if internet == "Yes" else 0
    romantic = 1 if romantic == "Yes" else 0


    # Create a DataFrame with the user input
    user_input = pd.DataFrame({
        'sex': [sex],
        'age': [age],
        'traveltime':[traveltime],
        'studytime' : [studytime],
        'failures':[failures],
        'schoolsup':[schoolsup],
        'famsup':[famsup],
        'paid':[paid],
        'activities':[activities],
        'nursery':[nursery],
        'higher':[higher],
        'internet':[internet],
        'romantic':[romantic],
        'health':health,
        'absences':[absences],
        'G1':[G1],
        'G2':[G2]
    })

    # Display user input
    st.subheader("User Input:")
    st.write(user_input)

    # Make predictions
    if st.button("Predict"):
        prediction = loaded_model.predict(user_input)

        performance_category = ""
        predicted_value = int(prediction[0])

        if 0 <= predicted_value <= 6:
            performance_category = "## Low Performance"
        elif 7 <= predicted_value <= 12:
            performance_category = "## Medium Performance"
        elif 13 <= predicted_value <= 20:
            performance_category = "## High Performance"

        # Display performance category
        st.subheader("Student Performance Category:")
        st.markdown(performance_category)

if __name__ == "__main__":
    main()