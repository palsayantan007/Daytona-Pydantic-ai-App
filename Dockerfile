FROM python:3.10-slim

# Set workdir
WORKDIR /app

# Copy requirements and install
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app

# Expose the default Flask port
EXPOSE 8080

# Start the application using gunicorn (production-like)
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]

