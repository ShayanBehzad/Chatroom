# Use an official Python runtime as a parent image
FROM python:3.11
#FROM python:3.11-slim
# Set the working directory in the container
WORKDIR /usr/src/Chatroom

# Copy the requirements file into the container
COPY requirements.txt ./

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=Chatroom.settings


# Expose the port your app runs on
EXPOSE 8003

# Run the application
CMD ["daphne", "-b", "0.0.0.0", "-p", "8003", "Chatroom.asgi:application"]
# CMD ["gunicorn", "Chatroom.wsgi:application", "--bind", "0.0.0.0:8003"]
