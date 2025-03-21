# Mood Matrix

Mood Matrix is a sentiment and emotion analysis tool that determines whether a customer review is positive or negative and identifies the underlying emotion.

## Dataset
- *Source*: Kaggle
- *Size*: 1,000 rows, 2 columns
  - *Review*: Customer review text
  - *Label*: 1 for positive, 0 for negative

## Model Implementation

### Sentiment Analysis
- *Algorithm*: Naïve Bayes
- *Training Accuracy*: 81.86%
- *Testing Accuracy*: 74.00%

### Emotion Detection
- *Model*: Pre-trained model from Hugging Face

## Tech Stack
- *Backend*: Flask API (Python)
- *Frontend*: React
- *Integration*: PyCharm (for API development)

## Features
- Users can enter a review
- The system classifies the review as positive or negative
- Identifies the emotion behind the review
