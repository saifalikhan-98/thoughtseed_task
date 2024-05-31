# Use an official Python runtime as a parent image
FROM public.ecr.aws/lambda/python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Command to run the Lambda function
CMD ["lambda_handler.handler"]
