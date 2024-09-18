# Use Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install the dependencies
RUN pip install -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Run the application
CMD ["python", "app.py"]
