# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir fastapi uvicorn opentelemetry-api opentelemetry-sdk opentelemetry-exporter-otlp opentelemetry-instrumentation-fastapi

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV OTLP_ENDPOINT 'otel-collector:4318'
ENV OTEL_RESOURCE_ATTRIBUTES='service.name=fastapiApp'
ENV OTEL_EXPORTER_OTLP_PROTOCOL='http'

# Run app.py when the container launches
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
# CMD ["sh", "-c", "opentelemetry-instrument", "python", "-m", "app:app", "--host", "0.0.0.0", "--port", "80"]
# CMD ["sh", "-c", "opentelemetry-instrument python -m app -- --host 0.0.0.0 --port 80"]
# CMD ["sh", "-c", "opentelemetry-instrument python -m app:app -- --host 0.0.0.0 --port 80"]
