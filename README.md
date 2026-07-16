# 🛡️ AegisIDS: Machine Learning-Based Intrusion Detection System with Real-Time Threat Monitoring

AegisIDS is a Machine Learning-powered Intrusion Detection System (IDS) designed to identify malicious network traffic and classify cyber attacks in real time. The system leverages supervised machine learning techniques trained on the UNSW-NB15 dataset and provides an intuitive web interface for threat detection.

---

## 🚀 Features

- 🔍 Detects malicious and benign network traffic
- 🤖 Machine Learning-based intrusion classification
- 📊 Real-time threat prediction through a web interface
- ⚡ Fast preprocessing using a saved scaler
- 🧠 Pre-trained model for instant predictions
- 💻 Simple Flask web application

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Framework
- Flask

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Model Persistence
- Joblib / Pickle

### Dataset
- UNSW-NB15 Dataset

### Development Tools
- Jupyter Notebook
- VS Code
- Git & GitHub

---

## 📂 Project Structure

```
AegisIDS/
│
├── app.py                  # Flask application
├── model_training.ipynb    # Model training notebook
├── features.pt             # Feature list
├── scaler.pt               # Saved scaler
├── requirements.txt        # Project dependencies
├── .gitignore
└── README.md
```

---

## 📊 Dataset

This project is trained using the **UNSW-NB15 Network Intrusion Detection Dataset**.

Due to GitHub's file size limitations, the dataset is **not included** in this repository.

You can download it from:

https://research.unsw.edu.au/projects/unsw-nb15-dataset

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/sumanthx73/AgeisIDS-Machine-Learning-Based-Intrusion-Detection-System-with-Real-Time-Threat-Monitoring.git
```

```bash
cd AgeisIDS-Machine-Learning-Based-Intrusion-Detection-System-with-Real-Time-Threat-Monitoring
```

### Create Virtual Environment (Optional)

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 🧠 Machine Learning Workflow

1. Load the UNSW-NB15 dataset
2. Perform data preprocessing
3. Feature engineering
4. Scale numerical features
5. Train the classification model
6. Save the trained model and scaler
7. Predict incoming network traffic
8. Display prediction through the Flask application

---

## 📈 Future Improvements

- Deep Learning models (LSTM/CNN)
- Real-time packet capture using Scapy
- Network traffic visualization dashboard
- User authentication
- Docker deployment
- Cloud deployment
- Live attack alerts via Email or SMS

---

## 📸 Screenshots

Add screenshots of:

- Home Page
- Prediction Page
- Detection Results

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 👨‍💻 Author

**Sumanth Kumar**

B.Tech Computer Science Graduate

GitHub: https://github.com/sumanthx73

LinkedIn: https://www.linkedin.com/in/sumanth73/

---

⭐ If you found this project useful, consider giving it a star!
