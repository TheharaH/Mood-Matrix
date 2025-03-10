'''from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (React will call this API)

# Load trained model and vectorizer
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        review = data.get("review", "")
        if not review:
            return jsonify({"error": "Empty review"}), 400

        transformed_review = vectorizer.transform([review])  # Convert to numerical form
        prediction = model.predict(transformed_review)[0]  # Predict sentiment

        result = "Positive" if prediction == 1 else "Negative"
        return jsonify({"review": review, "sentiment": result})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
'''


from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (React will call this API)

# Load trained model and vectorizer for sentiment analysis
model = joblib.load("sentiment_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

# Load Hugging Face emotion model locally
emotion_classifier = pipeline("text-classification", model="emotion_model")  # Load locally saved model


'''@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        review = data.get("review", "")

        if not review:
            return jsonify({"error": "Empty review"}), 400

        # Sentiment Prediction
        transformed_review = vectorizer.transform([review])  # Convert to numerical form
        sentiment_prediction = model.predict(transformed_review)[0]  # Predict sentiment
        sentiment_result = "Positive" if sentiment_prediction == 1 else "Negative"

        # Emotion Prediction using Hugging Face model
        emotion_result = emotion_classifier(review)[0]["label"]  # Get the emotion label

        return jsonify({
            "review": review,
            "sentiment": sentiment_result,
            "emotion": emotion_result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500
'''
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        review = data.get("review", "")

        if not review:
            return jsonify({"error": "Empty review"}), 400

        # Sentiment Prediction
        transformed_review = vectorizer.transform([review])  # Convert to numerical form
        sentiment_prediction = model.predict(transformed_review)[0]  # Predict sentiment
        sentiment_result = "Positive" if sentiment_prediction == 1 else "Negative"

        # Emotion Prediction using Hugging Face model
        emotion_result = emotion_classifier(review)[0]["label"]  # Get the emotion label

        return jsonify({
            "review": review,
            "sentiment": sentiment_result,
            "emotion": emotion_result
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
