# Base image

FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements.txt to the container
COPY requirements.txt ./

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the Python application code
COPY . .

# Expose the application port (8000 in this case)
EXPOSE 8000

# Run the Python application
CMD ["python", "app.py"]
