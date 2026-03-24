FROM runpod/base:0.4.0-cuda11.8.0

# Install system audio tools
RUN apt-get update && apt-get install -y ffmpeg

WORKDIR /
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy everything from your repo into the container
COPY . .

# Force the command to look at the root handler
CMD [ "python", "-u", "/handler.py" ]
