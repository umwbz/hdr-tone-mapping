import sys
import os
import torch
import numpy as np
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from PIL import Image
import io

# Tambahkan path ke folder model.py
sys.path.append(os.path.join(os.path.dirname(__file__), "Zero-DCE/Zero-DCE_code"))

# Import model
from model import enhance_net_nopool

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load pre-trained model
model = enhance_net_nopool().to(device)
checkpoint_path = os.path.join(os.path.dirname(__file__), "Zero-DCE/Zero-DCE_code/snapshots/Epoch99.pth")
checkpoint = torch.load(checkpoint_path, map_location=device)
model.load_state_dict(checkpoint)
model.eval()

# FastAPI app
app = FastAPI(title="Zero-DCE Low-Light Enhancer API")


@app.get("/")
def root():
    return {"message": "API running! Use POST /enhance to enhance images."}

# Fungsi enhance
def enhance_lowlight(input_image: Image.Image) -> Image.Image:
    img = np.array(input_image).astype(np.float32) / 255.0
    img = torch.from_numpy(img.transpose((2,0,1))).unsqueeze(0).to(device)
    with torch.no_grad():
        enhanced1, enhanced_final, _ = model(img)
    enhanced_np = enhanced_final.squeeze(0).cpu().numpy().transpose(1,2,0)
    enhanced_np = np.clip(enhanced_np*255.0, 0, 255).astype(np.uint8)
    return Image.fromarray(enhanced_np)

# Endpoint API
@app.post("/enhance")
async def enhance(file: UploadFile = File(...)):
    input_image = Image.open(io.BytesIO(await file.read())).convert("RGB")
    output_image = enhance_lowlight(input_image)
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")
