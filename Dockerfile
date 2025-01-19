# docker build -t mentalassess .
# docker run -d -p 988:988 --env-file .env --name mentalassess mentalassess

# Use Ubuntu 22.04 as base image
FROM ubuntu:22.04

# Set environment variables to avoid prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Install Python and pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && apt-get clean

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Copy the .env file (for environment variables)
COPY .env /app/.env

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 988

# Set environment variable for Flask
ENV FLASK_APP=run.py
ENV FLASK_ENV=production

# Run the application with Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=988"]
