import streamlit as st
import pandas as pd
import joblib

# Load model, label encoder, and data
try:
    model = joblib.load('tourist_model.pkl')
    label_encoder = joblib.load('label_encoder.pkl')
    # Try reading CSV with a different encoding (ISO-8859-1)
    df = pd.read_csv('destination_data_india.csv', encoding='ISO-8859-1')  # or use 'utf-16' or 'cp1252'
except FileNotFoundError:
    st.error("Model or data files not found. Please ensure they are in the correct directory.")
    st.stop()
except UnicodeDecodeError:
    st.error("There was an encoding issue with the CSV file. Try using a different encoding.")
    st.stop()

# Add missing columns during prediction (if they don't exist in the dataset)
if 'Season' not in df.columns:
    df['Season'] = 'summer'  # Default to 'summer' or any value used during training
if 'Trip_Duration' not in df.columns:
    df['Trip_Duration'] = 'medium'  # Default to 'medium'

# Title
st.title("🌍 Tourist Destination Recommendation App")

# --- User Inputs ---
budget = st.selectbox("Select Budget", ['low', 'medium', 'high'])
weather = st.selectbox("Select Weather", ['sunny', 'rainy', 'cold'])
region = st.selectbox("Select Region", ['North', 'South', 'East', 'West', 'Central'])
trip_duration = st.selectbox("Select Trip Duration", ['short', 'medium', 'long'])

# Predict button
if st.button("Find Destinations"):
    # Create input DataFrame (add default 'Season' column)
    user_input = pd.DataFrame([{
        'Budget': budget,
        'Weather': weather,
        'Region': region,
        'Trip_Duration': trip_duration,
        'Season': 'summer'  # Add a default 'Season' column here
    }])

    # One-hot encode user input to match training data
    X_user = pd.get_dummies(user_input)

    # Make sure columns match the model input (including the dummy 'Season' and 'Trip_Duration')
    X_model_cols = pd.get_dummies(df[['Budget', 'Weather', 'Region', 'Trip_Duration', 'Season']]).columns
    X_user = X_user.reindex(columns=X_model_cols, fill_value=0)

    # Predict
    prediction = model.predict(X_user)[0]
    predicted_category = label_encoder.inverse_transform([prediction])[0]

    st.subheader("🧭 Recommended Destination Category:")
    st.success(predicted_category)

    # Filter destinations from the same category and user-selected filters
    filtered_df = df[
        (df['Category'].str.lower() == predicted_category.lower()) &  # Case-insensitive comparison
        (df['Budget'].str.lower() == budget.lower()) & 
        (df['Weather'].str.lower() == weather.lower()) & 
        (df['Region'].str.lower() == region.lower())
    ]

    # Display results
    if not filtered_df.empty:
        st.subheader("📌 Matching Destinations:")
        for _, row in filtered_df.iterrows():
            st.markdown(f"### {row['Destination Name']}")
            st.markdown(f"**Category:** {row['Category']}")
            st.markdown(f"**Description:** {row['Description']}")
            st.markdown("---")
    else:
        st.warning("No exact matches found! Try changing the filters.")
