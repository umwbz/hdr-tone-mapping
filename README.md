# HDR Tone Mapping using Zero-DCE

A web-based image enhancement system that improves low-light images using the Zero-DCE (Zero-Reference Deep Curve Estimation) model. The system provides HDR-like tone mapping results through a Gradio interface and a REST API endpoint deployed on HuggingFace Spaces.

---

## 🚀 Features

- Low-light image enhancement
- HDR-like tone mapping effect
- Deep learning-based Zero-DCE model
- Real-time processing
- REST API support
- Gradio interactive UI
- Web demo integration (HTML frontend)

---

## 📦 Project Structure

.
├── app.py
├── model.py
├── requirements.txt
├── snapshots/
│   └── Epoch99.pth
├── README.md
└── web_demo.html

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

### Clone Repository

git clone https://github.com/your-username/hdr-tone-mapping.git
cd hdr-tone-mapping

---

### Install Dependencies

pip install -r requirements.txt

---

## 📦 Model Weights

Download pretrained Zero-DCE model and place it here:

snapshots/Epoch99.pth

---

## ▶️ Run Locally

python app.py

After running, Gradio interface will be available for image upload and enhancement.

---

## 🔌 API Endpoint

You can directly use the deployed model without running locally:

### 🔗 Enhance Endpoint

POST https://umscorleonis-hdr-tone-mapping-space.hf.space/enhance

---

POST /enhance

### 📤 Example Request (Python)

import requests

url = "https://umscorleonis-hdr-tone-mapping-space.hf.space/enhance"

files = {
    "file": open("image.jpg", "rb")
}

response = requests.post(url, files=files)

with open("result.png", "wb") as f:
    f.write(response.content)

---

## 📥 Response Types

The API supports two types of responses:

### 1. Binary Image (Recommended)
- Returns PNG image directly

### 2. JSON Response (Optional)
```json
{
  "result_base64": "iVBORw0KGgoAAAANSUhEUg..."
}

## Model Weights

Download the pretrained Zero-DCE model (`Epoch99.pth`) and place it inside the `snapshots` folder:

```text
snapshots/Epoch99.pth
```

## Run the Application

```bash
python app.py
```

After running the script, a Gradio interface will be launched locally. You can upload an image and obtain the enhanced result directly through the web interface.

## Method

This project utilizes the Zero-DCE model, a deep learning approach for low-light image enhancement that learns pixel-wise enhancement curves without requiring paired training data.

## Author

Sukma Wati

## License

This project is intended for educational and research purposes.
