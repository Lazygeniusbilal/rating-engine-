# using base image
FROM python:3.11-slim

# Install system dependencies required by lightgbm
RUN apt-get update && apt-get install -y \
    build-essential \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# set working directory
WORKDIR /app

# copy all the code inside
COPY . /app/

# install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# expose port
EXPOSE 8000

# health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/health', timeout=5)"

# run app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
