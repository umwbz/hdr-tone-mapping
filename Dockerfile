# Base image
FROM python:3.8-slim

# Install git & system deps
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements & install
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Clone Zero-DCE repo langsung
RUN git clone https://github.com/Li-Chongyi/Zero-DCE.git Zero-DCE

# Expose port HF Spaces
EXPOSE 7860

# Copy main.py (FastAPI server)
COPY app/main.py /app/main.py

# Start FastAPI server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]

