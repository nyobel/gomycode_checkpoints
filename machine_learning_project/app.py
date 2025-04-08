# app.py
import streamlit as st
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the trained model
try:
    model = joblib.load('student_pass_predictor.joblib')
except FileNotFoundError:
    st.error("Model file not found. Please make sure 'student_pass_predictor.joblib' is in the same directory.")
    st.stop()

# App title and description
st.title("🎓 Student Performance Predictor")
st.markdown("""
Predict whether a student will pass or fail based on their demographics and preparation.
The model considers math, reading, and writing scores along with other student characteristics.
""")

# Sidebar with user inputs
with st.sidebar:
    st.header("📝 Student Information")
    
    # Demographic information
    gender = st.radio("Gender", ["Female", "Male"])
    lunch = st.selectbox("Lunch Type", ["Standard", "Free/Reduced"])
    test_prep = st.checkbox("Completed Test Preparation Course")
    
    # Academic scores
    st.subheader("Academic Scores")
    math_score = st.slider("Math Score", 0, 100, 70)
    reading_score = st.slider("Reading Score", 0, 100, 75)
    writing_score = st.slider("Writing Score", 0, 100, 73)
    
    # Categorical features
    ethnicity = st.selectbox(
        "Race/Ethnicity Group",
        ["Group A", "Group B", "Group C", "Group D", "Group E"]
    )
    
    parental_edu = st.selectbox(
        "Parental Education Level",
        ["Some High School", "High School", "Some College", 
         "Associate's Degree", "Bachelor's Degree", "Master's Degree"]
    )

# Create input dataframe
def create_input_df():
    return pd.DataFrame([{
        'gender': 0 if gender == "Female" else 1,
        'lunch': 1 if lunch == "Standard" else 0,
        'test preparation course': 1 if test_prep else 0,
        'math score': math_score,
        'reading score': reading_score,
        'writing score': writing_score,
        f'race/ethnicity_{ethnicity.lower().replace(" ", "_")}': 1,
        f'parental level of education_{parental_edu.lower().replace(" ", "_").replace("'", "")}': 1
    }])

# Main prediction logic
if st.button("Predict Student Outcome"):
    try:
        # Create input data
        input_df = create_input_df()
        
        # Reindex to match training columns
        input_df = input_df.reindex(columns=model.feature_names_in_, fill_value=0)
        
        # Make prediction
        prediction = model.predict(input_df)
        probability = model.predict_proba(input_df)[0][1]
        
        # Display results
        st.subheader("Prediction Results")
        result_col = st.columns(2)
        
        with result_col[0]:
            st.metric("Predicted Outcome", 
                     "PASS ✅" if prediction[0] == 1 else "FAIL ❌")
            
        with result_col[1]:
            st.metric("Confidence Level", f"{probability:.0%}")
        
        # Show feature importance
        st.subheader("Key Factors in Prediction")
        feature_importance = pd.Series(model.feature_importances_, 
                                      index=model.feature_names_in_)
        top_features = feature_importance.sort_values(ascending=False).head(5)
        
        fig, ax = plt.subplots()
        sns.barplot(x=top_features.values, y=top_features.index, palette="viridis")
        plt.title("Top 5 Influential Features")
        st.pyplot(fig)
        
    except Exception as e:
        st.error(f"Error making prediction: {str(e)}")
