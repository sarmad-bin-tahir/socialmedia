# Use an official Python runtime as the base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the Django project code into the container
COPY . .


COPY ./entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r//' /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Set the entrypoint to execute Django commands
ENTRYPOINT ["/entrypoint.sh"]
