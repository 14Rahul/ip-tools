# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the ip_tool.py script into the container
COPY ip_tool.py .

# Run the script when the container launches
ENTRYPOINT ["python", "ip_tool.py"]
