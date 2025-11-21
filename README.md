# Hearing Hand – Real-Time Indian Sign Language (ISL) Detection

A real-time **Indian Sign Language gesture detection system** built using **YOLOv8**, **MediaPipe Holistic**, and **OpenCV**, capable of recognizing ISL alphabet signs live from the webcam and converting gestures into on-screen text.  
This project is designed to help bridge the communication gap for individuals who use sign language.

---

## 🚀 Features

- Real-time ISL gesture recognition  
- YOLOv8-based detection trained on **3,000+ images**
- MediaPipe Holistic for highly accurate **hand + pose landmark extraction**
- Combines **YOLO predictions + landmark signals** for robust accuracy
- Live webcam inference using OpenCV
- 90%+ accuracy on commonly used signs
- Modular and clean architecture

---

## 🧠 Tech Stack

| Component | Technologies |
|----------|--------------|
| **Model** | YOLOv8 (Ultralytics) |
| **Landmark Tracking** | MediaPipe Holistic |
| **Computer Vision** | OpenCV |
| **Scripting** | Python |
| **Data Handling** | NumPy |
| **Deployment Ready** | Flask (optional) |

---

## 📂 Project Structure
Hearing_Hand_Project/
│── app.py # Main webcam inference app
│── body.py # Stores ASL/ISL dataset labels
│── config.py # Reserved for future configs
│── models/
│ └── NEW_FINAL.pt # Trained YOLOv8 model
│── README.md # Project documentation


## 🖥 How It Works (Architecture)

### 1. **MediaPipe Holistic** identifies hand + pose landmarks  
Used to highlight the hands even when environment lighting is poor.

### 2. **Image converted to landmark-mask (black background)**  
YOLO sees only the extracted landmark drawing → makes detection more stable.

### 3. **YOLOv8 model** predicts the gesture from the mask image  
(Uses `NEW_FINAL.pt` model)

### 4. **Final prediction shown on the screen**  
Bounding box + label + real-time FPS.

---

## 🧪 Example Code (Look inside `app.py`)

The core pipeline (from your file) includes:

- MediaPipe for landmark extraction
- YOLOv8 inference on processed image  
- Post-processing + cropping + class extraction  

Reference code extracted from `app.py` → :contentReference[oaicite:1]{index=1}

---

## 🧩 Dataset Labels

The system supports A–Z alphabet gestures:  
(From your `body.py`) → :contentReference[oaicite:2]{index=2}

```python
dataset = ["A","B","C","D","E","F","G","H","I","J",
           "K","L","M","N","O","P","Q","R","S","T",
           "U","V","W","X","Y","Z"]


🛠 Setup Instructions
1. Clone the Repository
git clone https://github.com/MahisagarKadam/hearing-hand-real-time-isl-detection.git
cd hearing-hand-real-time-isl-detection

2. Install Dependencies
pip install -r requirements.txt


If you don’t have a requirements file, install manually:

pip install opencv-python mediapipe ultralytics numpy

3. Add Your YOLO Model

Place the file:

NEW_FINAL.pt


inside models/ (or update the path in app.py).

4. Run the App
python app.py


