# HDR Tone Mapping using Zero-DCE

A web-based image enhancement application that improves low-light images using the Zero-DCE (Zero-Reference Deep Curve Estimation) model. The application provides an interactive interface built with Gradio, allowing users to upload images and obtain enhanced HDR-like results.

## Features

* Low-light image enhancement
* HDR-like tone mapping
* Deep learning-based image processing using Zero-DCE
* User-friendly Gradio interface
* Real-time image enhancement

## Project Structure

```text
.
├── app.py
├── model.py
├── requirements.txt
├── README.md
└── snapshots/
    └── Epoch99.pth
```

## Requirements

* Python 3.9+
* PyTorch
* Torchvision
* OpenCV
* NumPy
* Pillow
* Gradio

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/hdr-tone-mapping.git
cd hdr-tone-mapping
```

Install dependencies:

```bash
pip install -r requirements.txt
```

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
