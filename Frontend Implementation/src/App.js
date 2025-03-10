

import React, { useState, useEffect } from "react";
import axios from "axios";
import './App.css'; 

function App() {
  const [review, setReview] = useState(""); 
  const [result, setResult] = useState(null); 
  const [error, setError] = useState(""); 
  const [loading, setLoading] = useState(true); 


  useEffect(() => {
    setTimeout(() => {
      setLoading(false); 
    }, 3000);
  }, []);

  const analyzeSentiment = async () => {
    setError(""); 
    try {
      // Make a POST request to the Flask API
      const response = await axios.post("http://127.0.0.1:5000/predict", { review });
      setResult({
        sentiment: response.data.sentiment,  // Set the sentiment result
        emotion: response.data.emotion      // Set the emotion result
      });
    } catch (err) {
      setError("Error analyzing sentiment. Please try again."); 
    }
  };

  return (
    <div>
      {loading ? (
   
        <div className="loading-screen">
          <img src="/mood matrix.jpg" alt="Mood Matrix Logo" className="loading-logo" />
          <h2 className="loading-text">Mood Matrix is loading...</h2>
        </div>
      ) : (
        
        <div className="app-content">
          {}
          <header>
            <img src="/mood matrix.jpg" alt="Mood Matrix Logo" />
            <h1>Mood Matrix</h1>
          </header>

          {}
          <div className="container">
            <textarea
              rows="6"
              cols="60"
              placeholder="Enter your review..."
              value={review}
              onChange={(e) => setReview(e.target.value)} 
            />
            <br />
            <button onClick={analyzeSentiment}>
              Analyze
            </button>

            {error && <p className="error">{error}</p>} {}
            {result && (
              <div>
                {}
                <div className="result">
                  <h3>
                    The sentiment is <span>{result.sentiment}</span> and the review is <span>{result.emotion}</span>.
                  </h3>
                </div>
              </div>
            )}
          </div>

          {}
          <footer>
            <p>&copy; 2025 Mood Matrix. All rights reserved.</p>
          </footer>
        </div>
      )}
    </div>
  );
}

export default App;