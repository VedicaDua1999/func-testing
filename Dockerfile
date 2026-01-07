FROM python:3.11-slim

WORKDIR /app

# Copy requirements first (better for Docker layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

EXPOSE 8080

CMD ["python", "test.py"]
