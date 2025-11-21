# Hearing Hand – Real-Time Indian Sign Language (ISL) Detection

A real-time Indian Sign Language gesture detection system built using **YOLOv8**, **MediaPipe Holistic**, and **OpenCV**, capable of recognizing ISL alphabet signs live from the webcam and converting gestures into on-screen text.  
This project is designed to help bridge the communication gap for individuals who use sign language.

---

## 🚀 Features
- Real-time ISL gesture recognition  
- YOLOv8-based detection trained on **3,000+ images**  
- MediaPipe Holistic for accurate **hand + pose landmark extraction**  
- Combines YOLO predictions + landmark signals for robust accuracy  
- Live webcam inference using OpenCV  
- **90%+ accuracy** on commonly used signs  
- Modular and clean architecture  

---

## 🧠 Tech Stack

| Component | Technologies |
|----------|--------------|
| Model | YOLOv8 (Ultralytics) |
| Landmark Tracking | MediaPipe Holistic |
| Computer Vision | OpenCV |
| Scripting | Python |
| Data Handling | NumPy |
| Deployment Ready | Flask (optional) |

---

## 📂 Project Structure
```
Hearing_Hand_Project/
│── app.py                # Main webcam inference app
│── body.py               # Stores ISL dataset labels
│── config.py             # Reserved for future configs
│── models/
│     └── NEW_FINAL.pt    # Trained YOLOv8 model
│── README.md             # Project documentation
```

---

## 🖥 How It Works (Architecture)

### 1. MediaPipe Holistic extracts hand + pose landmarks  
It isolates the hands even in low-light conditions.

### 2. Generated landmark mask (black background)  
YOLO sees only clean landmark drawings → better accuracy.

### 3. YOLOv8 model predicts the gesture  
Uses `NEW_FINAL.pt`.

### 4. Final prediction shown on screen  
Bounding box + label + FPS counter.

---

## 🧩 Dataset Labels (A–Z)

```python
dataset = [
"A","B","C","D","E","F","G","H","I","J",
"K","L","M","N","O","P","Q","R","S","T",
"U","V","W","X","Y","Z"
]
```

---

# 🛠 Setup Instructions  
Follow these steps to run the project.

---

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/MahisagarKadam/hearing-hand-real-time-isl-detection.git
cd hearing-hand-real-time-isl-detection
```

---

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing:
```bash
pip install opencv-python mediapipe ultralytics numpy
```

---

### 3️⃣ Add the YOLOv8 Model  
Place your trained model in the `models/` directory:

```
models/
└── NEW_FINAL.pt
```

(If the model filename is different, update its path inside `app.py`.)

---

### 4️⃣ Run the Application
```bash
python app.py
```

This will open your webcam & start real-time sign prediction.

---

### 5️⃣ Camera Troubleshooting
If the webcam doesn’t open, try changing the index inside `app.py`:

```python
cv2.VideoCapture(0)
cv2.VideoCapture(1)
cv2.VideoCapture(2)
```

---

## ✔ You’re All Set!
The system will now:  
- Read webcam input  
- Extract hand + pose landmarks  
- Run YOLOv8 predictions  
- Display recognized ISL signs in real-time  

---
