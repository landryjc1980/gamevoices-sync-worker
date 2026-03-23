FROM runpod/base:0.4.0-cuda11.8.0

# Install system audio tools
RUN apt-get update && apt-get install -y ffmpeg

WORKDIR /
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY handler.py .

# Run the handler
CMD [ "python", "-u", "/handler.py" ]
