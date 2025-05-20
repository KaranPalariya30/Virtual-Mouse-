# 🖱️ AI Virtual Mouse with Hand Gestures

A gesture-controlled virtual mouse built using **CNN**, **MediaPipe**, **OpenCV**, and **Flask**. This project allows users to control their mouse cursor using hand gestures captured from a webcam in real-time.


## 🚀 Features

- 🖐️ Hand gesture recognition using a custom-trained CNN model
- 📷 Real-time webcam input using OpenCV
- 🤖 Hand landmark tracking via MediaPipe
- 🧠 Gesture-based mouse control actions (click, scroll, drag, etc.)
- 🌐 Flask-based web interface to stream the webcam feed and display gesture info
- 🔍 Supports 5 custom gestures: `fist`, `peace`, `okay`, `stop`, `thumb down`



## 🧠 Gesture Classes

| Gesture     | Action               |
|-------------|----------------------|
| `stop`      | Left mouse click     |
| `thumb down`| Scroll down          |
| `fist`      | Mouse button down    |
| `peace`     | Mouse button up      |
| `okay`      | Can be customized    |



## 📁 Project Structure
```
gesture-virtual-mouse/
├── app.py # Flask backend
├── models/
│ └── gesture_model.h5 # Trained CNN model
├── templates/
│ └── index.html # Frontend UI
├── static/ # (Optional for CSS/JS files)
├── dataset/ # Collected gesture image dataset
├── requirements.txt # Required Python packages
└── README.md # Project documentation
```


## 🛠️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/KaranPalariya30/virtual-mouse.git
cd virtual-mouse
```
## Create a virtual environment (recommended)
```
python -m venv venv
source venv/bin/activate      # On Linux/macOS
venv\Scripts\activate         # On Windows
```

## Install the dependencies
```
pip install -r requirements.txt
```
##Run the Flask app
```
python app.py
```
## Open in browser

Go to http://127.0.0.1:5000/ in your browser.



