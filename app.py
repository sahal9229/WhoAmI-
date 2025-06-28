# app.py
from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
try:
    model = joblib.load('personality_model.pkl')
    print("Model loaded successfully!")
except:
    print("Warning: Model not found. Please run model.py first.")
    model = None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if model is None:
            return "Error: Model not loaded. Please train the model first by running model.py"
        
        # Get data from form
        time_alone = float(request.form['time_alone'])
        stage_fear = int(request.form['stage_fear'])
        social_events = float(request.form['social_events'])
        friends_size = float(request.form['friends_size'])
        post_freq = float(request.form['post_freq'])
        
        # Create DataFrame for prediction
        input_data = pd.DataFrame([[time_alone, stage_fear, social_events, friends_size, post_freq]],
                                 columns=['Time_spent_Alone', 'Stage_fear', 'Social_event_attendance',
                                          'Friends_circle_size', 'Post_frequency'])
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        result = "Extrovert" if prediction == 1 else "Introvert"
        
        # Return just the result text (the JavaScript will handle the display)
        return f"Result: {result}"
    
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
