import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model and preprocessing artifacts
model = joblib.load("model.pkl")
preprocess = joblib.load("preprocessing_artifacts.pkl")


st.title("Financial Inclusion In Africa")
st.divider()
st.write("This app uses machine learning to predict individual who are most likely to have or use a bank account. ")
st.divider()



# widgets
# -----------------------------------------------------------------
country = st.selectbox("Country", ["Kenya", "Rwanda", "Tanzania", "Uganda"])
year = st.radio("Year", options=[2016, 2017, 2018])  # Fixed 2028 → 2018
location_type = st.selectbox("Location Type", ["Rural", "Urban"])
cellphone_access = st.radio("Cellphone Access", ["Yes", "No"])
household_size = st.slider("Household Size", 1, 20)
age_of_respondent = st.slider("Age of Respondent", 16, 100)
gender_of_respondent = st.radio("Gender", ["Female", "Male"])
education_level = st.selectbox("Education Level", [
    "No formal education", 
    "Primary education",
    "Secondary education",
    "Vocational/Specialised training",
    "Tertiary education",
    "Other/Dont know/RTA"
])
relationship_with_head = st.selectbox("Relationship with Head", [
    "Head of Household", 
    "Spouse", 
    "Child", 
    "Parent", 
    "Other relative", 
    "Other non-relatives"
])
marital_status = st.selectbox("Marital Status", [  # Fixed comma-separated option
    "Single/Never Married",
    "Married/Living together",
    "Widowed",
    "Divorced/Seperated",
    "Dont know"
])
job_type = st.selectbox("Job Type", [
    "Self employed", 
    "Formally employed Private",
    "Formally employed Government", 
    "Informally employed",
    "Government Dependent",
    "Farming and Fishing", 
    "Remittance Dependent",
    "Other Income", 
    "No Income"
])

# -----------------------------------------------------------------
st.divider()
# -----------------------------------------------------------------


if st.button("Predict"):
    # Create input DataFrame with correct column order
    input_data = pd.DataFrame([{
        'country': country,
        'year': year,
        'location_type': location_type,
        'cellphone_access': cellphone_access,
        'household_size': household_size,
        'age_of_respondent': age_of_respondent,
        'gender_of_respondent': gender_of_respondent,
        'relationship_with_head': relationship_with_head,
        'marital_status': marital_status,
        'education_level': education_level,
        'job_type': job_type
    }])

    # Apply preprocessing
    # 1. Label encode binary features
    for col in ['cellphone_access', 'gender_of_respondent']:
        le = preprocess['label_encoders'][col]
        input_data[col] = le.transform(input_data[col])

    # 2. Map education level
    input_data['education_level'] = input_data['education_level'].map(
        preprocess['education_mapping']
    )

    # 3. One-hot encode nominal features
    nominal_features = ['country', 'location_type', 
                       'relationship_with_head', 
                       'marital_status', 'job_type']
    encoded_nominal = preprocess['onehot_encoder'].transform(
        input_data[nominal_features]
    )
    encoded_df = pd.DataFrame(
        encoded_nominal,
        columns=preprocess['onehot_encoder'].get_feature_names_out(nominal_features)
    )

    # 4. Combine all features
    final_input = pd.concat([
            input_data.drop(columns=nominal_features), 
            encoded_df
        ], axis=1)

    # 5. Ensure correct feature order
    final_input = final_input[preprocess['feature_names']]

    # Make prediction
    try:
        proba = model.predict_proba(final_input)[0][1]
        st.success(f"Probability of having a bank account: {proba:.2%}")
    except Exception as e:
        st.error(f"Prediction failed: {str(e)}")
else:
    st.write("Please fill all values before using the predict button.")