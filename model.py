# model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def train_model():
    # Load and preprocess data (similar to your notebook)
    data = pd.read_csv(r"C:\Users\sahal\OneDrive\Desktop\python\project\personality_predictor\personality_dataset.csv")
    
    # Clean and preprocess data
    data['Stage_fear'] = data['Stage_fear'].map({'Yes': 1, 'No': 0})
    data['Drained_after_socializing'] = data['Drained_after_socializing'].map({'Yes': 1, 'No': 0})
    data['Personality'] = data['Personality'].map({'Introvert': 0, 'Extrovert': 1})
    data = data.dropna()
    
    # Select features and target
    X = data[['Time_spent_Alone', 'Stage_fear', 'Social_event_attendance', 
              'Friends_circle_size', 'Post_frequency']]
    y = data['Personality']
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
    
    # Save model
    joblib.dump(model, 'personality_model.pkl')
    
    return model

if __name__ == "__main__":
    train_model()
