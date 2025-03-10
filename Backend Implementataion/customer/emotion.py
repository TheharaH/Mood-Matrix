from transformers import pipeline

# Load the emotion classification model
emotion_classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

# Save it locally in the project directory
emotion_classifier.save_pretrained("emotion_model")
