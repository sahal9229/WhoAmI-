# WhoAmI-
personality_predictor
🧠 Personality Predictor Web App

A simple and elegant web application that predicts whether a person is an Introvert or an Extrovert based on user input. Built with Python (Flask) for the backend and HTML/CSS/JavaScript for the frontend.

📌 Features

Clean and animated frontend UI

User inputs personality-related data (e.g., time spent alone, social events attended, etc.)

Predicts personality type using a trained Random Forest model

Displays results with dynamic styling and explanations

🖥️ UI Preview

Homepage



Users can fill in:

Time spent alone daily

Stage fear (Yes/No)

Social event attendance per month

Size of friends circle

Frequency of social media posts

Result Display



Shows if the user is an Extrovert or Introvert with detailed feedback and styling

⚙️ Tech Stack

Frontend: HTML, CSS, JavaScript

Backend: Flask (Python)

Machine Learning: scikit-learn (RandomForestClassifier)

Model Serialization: joblib

🧪 Dataset

Stored in personality_dataset.csv, containing features such as:

Time_spent_Alone

Stage_fear

Social_event_attendance

Friends_circle_size

Post_frequency

Personality (target: Introvert/Extrovert)

🧠 Model Training (in model.py)

Preprocessing includes encoding categorical features

Model: Random Forest Classifier

Accuracy printed during training

Final model saved as personality_model.pkl

🚀 How to Run

1. Clone the repository

git clone <repo-url>
cd personality-predictor

2. Install requirements

pip install -r requirements.txt

3. Train the model (if not already trained)

python model.py

4. Run the Flask app

python application.py

5. Open your browser

Go to http://127.0.0.1:5000

📂 Project Structure

.
├── application.py           # Flask backend
├── index.html               # Main UI page
├── result.html              # Result display
├── model.py                 # ML model training
├── personality_model.pkl    # Trained ML model
├── personality_dataset.csv  # Dataset used
├── requirements.txt         # All dependencies

📬 Contact

For feedback or questions, feel free to reach out!

Happy Predicting! 🎉

