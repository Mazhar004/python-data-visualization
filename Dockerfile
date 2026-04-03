FROM python:3.12-slim

WORKDIR /app

# System dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        default-jre-headless \
    && rm -rf /var/lib/apt/lists/*

# Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

EXPOSE 8501 8502 8503 8888

# Default command (overridden by docker-compose)
CMD ["streamlit", "run", "Streamlit/CallLogAnalysis/app.py", "--server.port=8501"]
