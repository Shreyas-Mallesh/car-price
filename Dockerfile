# Base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /main

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the necessary packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the entire current directory to the working directory
COPY . .

# Expose port 8501 for Streamlit
EXPOSE 8501

# Start Streamlit app
CMD ["streamlit", "run", "--server.port", "8501", "main.py"]
