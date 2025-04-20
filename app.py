
import streamlit as st
import pandas as pd
# import joblib  # Uncomment when your model is available

st.set_page_config(page_title="AI Career Guidance", layout="centered")

st.title("🎯 AI-Enhanced Career Guidance System")
st.write("Upload your student data in CSV format and get personalized career path recommendations!")

uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    if 'higher' in df.columns:
        df['higher'] = df['higher'].map({'yes': 1, 'no': 0})

    features = ['G1', 'G2', 'studytime', 'absences', 'health', 'higher']

    if all(f in df.columns for f in features):
        input_data = df[features]

        # Dummy predictions (replace with your real model)
        # model = joblib.load("model.joblib")
        # predictions = model.predict(input_data)
        predictions = [f"Recommended Path for Record {i+1}: Data Science" for i in range(len(input_data))]

        st.success("Career Recommendations:")
        for prediction in predictions:
            st.write(f"✅ {prediction}")

    else:
        st.error("Your CSV is missing one of the required columns: G1, G2, studytime, absences, health, higher")

