# WhoAmI-
personality_predictor
# 🧠 Personality Predictor Web App

A simple web application that predicts whether a person is an **Introvert** or an **Extrovert** based on five input traits using a trained machine learning model. Built with **Python**, **Flask**, and **HTML/CSS**, and styled for an elegant user experience.

---

## 🌐 Live Demo

> No live link available yet. Run locally using the instructions below.

---

## 📸 App Interface

### 🎯 Home Page (`index.html`)

* Presents a clean form interface with five input fields:

  * **Time Spent Alone** (hours per day)
  * **Stage Fear** (Yes/No)
  * **Social Event Attendance** (per month)
  * **Friends Circle Size**
  * **Social Media Post Frequency** (per week)
* Includes animations, gradients, and validation.

"C:\Users\sahal\OneDrive\Pictures\Screenshots 1\Screenshot 2025-06-28 142704.png"

### 📊 Result Page (`result.html`)

* Displays prediction as either **Extrovert** or **Introvert** with distinct styles:

  * **Extrovert** → pink gradient background
  * **Introvert** → blue/green gradient background

![Result UI Example](https://via.placeholder.com/600x300?text=Result+UI+Screenshot)

---

## 🧩 Core Features

* **Frontend**: Beautiful, animated form built using HTML and CSS
* **Backend**: Flask app (`application.py`) with a `/predict` route
* **Model**: Trained `RandomForestClassifier` on `personality_dataset.csv`
* **Prediction Output**: Introvert or Extrovert based on numerical + binary inputs

---

## 🛠️ Installation & Setup

### 1. Clone the Repo

```bash
https://github.com/yourusername/personality-predictor.git
cd personality-predictor
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Train the Model

```bash
python model.py
```

> This will generate `personality_model.pkl`

### 4. Run the Web App

```bash
python application.py
```

> Visit `http://127.0.0.1:5000/` in your browser.

---

## 📁 Project Structure

```
├── application.py          # Flask backend
├── model.py                # Model training script
├── personality_model.pkl   # Trained ML model
├── personality_dataset.csv # Training dataset
├── index.html              # Frontend form UI
├── result.html             # Result display template
├── requirements.txt        # Dependencies
```

---

## 🧠 Model Details

* **Algorithm**: Random Forest Classifier
* **Features Used**:

  * Time\_spent\_Alone
  * Stage\_fear (binary)
  * Social\_event\_attendance
  * Friends\_circle\_size
  * Post\_frequency
* **Label**: Personality (Introvert=0, Extrovert=1)
* **Accuracy**: Printed after training in `model.py`

---

## 🧪 Example Inputs

| Time Alone | Stage Fear | Events/Month | Friends | Posts/Week | Prediction |
| ---------- | ---------- | ------------ | ------- | ---------- | ---------- |
| 6          | Yes        | 2            | 3       | 0          | Introvert  |
| 1          | No         | 15           | 30      | 10         | Extrovert  |

---

## ⚠️ Troubleshooting

* "Model not found" → Run `model.py` first.
* CORS or fetch errors → Ensure Flask is running on the correct port (usually 5000).

---

## 🧾 License

This project is open-source and free to use under the MIT License.

---

## 🙌 Acknowledgements

* Inspired by basic behavioral psychology traits
* UI influenced by modern web form aesthetics

---

> Created with 💙 by \[Your Name / Team Name]
