import streamlit as st
import joblib
import numpy as np

# Load your trained model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.set_page_config(page_title="Flipkart Review Sentiment", layout="centered")

st.markdown(
    "<h1 style='color:#2874f0; text-align:center;'>Flipkart Review Sentiment Analysis</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Enter your review and rating to check if it's positive or negative!</p>",
    unsafe_allow_html=True
)

with st.form("review_form"):
    review = st.text_area("Enter your review:", height=120)
    rating = st.slider("Rating (1-5):", 1, 5, 5)
    submitted = st.form_submit_button("Analyze Sentiment")

if submitted:
    # Combine review and rating if your model uses both
    # Example: X = vectorizer.transform([f"{review} Rating: {rating}"])
    # If only review is used:
    X = vectorizer.transform([review])
    pred = model.predict(X)[0]
    if pred == 1 or pred == "positive":
        st.success("😊 Positive Review")
    else:
        st.error("😞 Negative Review")