# Flipkart Review Sentiment Analysis

This project provides a Streamlit web app for sentiment analysis of Flipkart product reviews.

## Requirements

- Docker

## Running the App

Build the Docker image:

```sh
docker build -t flipkart-sentiment-app .
```

Run the Streamlit app:

```sh
docker run -p 8501:8501 flipkart-sentiment-app
```

Or, run directly with Streamlit (if you have Python and dependencies installed):

```sh
streamlit run app.py --server.port=8501 --server.address=0.0.0.0
```

The app will be available at [http://localhost:8501](http://localhost:8501).