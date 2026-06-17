# HDR Tone Mapping using Zero-DCE

A web-based image enhancement application that improves low-light images using the Zero-DCE (Zero-Reference Deep Curve Estimation) model. The application provides an interactive interface built with Gradio and a deployed API for real-time image enhancement.

---

## 🌐 Live API Endpoint (HuggingFace Space)

You can directly use the deployed model via API:

### 🔗 Enhance Endpoint

POST https://umscorleonis-hdr-tone-mapping-space.hf.space/enhance

---

## 🚀 Features

- Low-light image enhancement
- HDR-like tone mapping
- Deep learning-based image processing using Zero-DCE
- Gradio interactive interface
- FastAPI / API-based inference support
- Real-time image enhancement

---

## 📦 Project Structure

.
├── app.py
├── model.py
├── requirements.txt
├── README.md
└── snapshots/
    └── Epoch99.pth

---

## ⚙️ Requirements

- Python 3.9+
- PyTorch
- Torchvision
- OpenCV
- NumPy
- Pillow
- Gradio

---

## 📥 Installation

Clone the repository:

git clone https://github.com/your-username/hdr-tone-mapping.git
cd hdr-tone-mapping

---

Install dependencies:

pip install -r requirements.txt

---

## 🧠 Model Weights

Download pretrained Zero-DCE model:

snapshots/Epoch99.pth

---

## ▶️ Run Application

python app.py

After running, a Gradio interface will open where you can upload images and get enhanced results.

---

## 🔌 API Endpoint Usage (HuggingFace)

### 📤 Request Example (Python)

import requests

url = "https://umscorleonis-hdr-tone-mapping-space.hf.space/enhance"

files = {
    "file": open("image.png", "rb")
}

response = requests.post(url, files=files)

with open("output.png", "wb") as f:
    f.write(response.content)

---

## 🧠 Method

This project uses Zero-DCE (Zero-Reference Deep Curve Estimation), a deep learning model for low-light image enhancement that does not require paired training data. It learns image enhancement curves directly from input images.

---

## 🛠 Technology Stack

- Python
- PyTorch
- Zero-DCE Model
- OpenCV
- NumPy
- Pillow
- Gradio
- FastAPI (deployment API)

---

## 👩‍💻 Author

Sukma Wati

---

## 📄 License

This project is intended for educational and research purposes only.
