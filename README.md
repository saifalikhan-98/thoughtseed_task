# Influencer Campaign Management Platform

## Overview

This project is an Influencer Campaign Management Platform built using FastAPI. The platform allows users to find influencers based on various criteria and manage influencer campaigns including contacting influencers, sending requirements, chatting, and tracking campaigns.

## Features

- Influencer search with multiple filters
- Integration with AWS Lambda for serverless deployment
- Docker support for containerization
- Detailed API documentation with Swagger

## Requirements

- Python 3.8+
- FastAPI
- Mangum
- Docker
- AWS CLI

## Installation

1. Clone the repository:

    ```sh git clone https://github.com/yourusername/influencer-platform.git

2. Go to the directory:

    ```sh cd influencer-platform 

3. Create and activate a virtual environment:
    ````sh python -m venv venv
   
4. Activate virtual env:
    ````sh source venv/bin/activate  
   
3. Install the dependencies:
    ````sh pip install -r requirements.txt

## Running the Application Locally 

1. To run application locally:
    ````sh uvicorn main:app --reload

## To check API documentation:
   Please go to <baseurl>/docs

## Docker Deployment

1. Build the Docker image
    ````sh docker build -t -f Dockerfile .
   
2. Run the Docker container
    ````docker run -p 8000:8000 influencer-platform

## AWS Deployment

#### Build and Push the Docker Image to AWS ECR:



1. Authenticate Docker with AWS ECR:
    ```sh aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<your-region>.amazonaws.com

2. Create an ECR Repository (if not already created):
    ````sh aws ecr create-repository --repository-name my-fastapi-app

3. Build the Docker Image:
    ````sh docker build -t -fDockerfile .

4. Tag the Docker Image:
    ````sh docker tag my-fastapi-app:latest <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/my-fastapi-app:latest

5. Push the Docker Image to ECR:
    ````sh docker push <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/my-fastapi-app:latest
   

6. Create an IAM Role for Lambda:

#### Create a file named trust-policy.json:

       {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "lambda.amazonaws.com"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
       }

7. Create an IAM Role:
    ````sh aws iam create-role --role-name lambda-ex --assume-role-policy-document file://trust-policy.json

8. Attach Policies to the Role:
    ````sh aws iam attach-role-policy --role-name lambda-ex --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole

9. Create Lambda Function:
    ````sh aws lambda create-function --function-name my-fastapi-function --package-type Image --code ImageUri=<your-account-id>.dkr.ecr.<your-region>.amazonaws.com/my-fastapi-app:latest --role arn:aws:iam::<your-account-id>:role/lambda-ex

10. Configure API Gateway:
    ```sh aws apigatewayv2 create-api --name 'My API' --protocol-type HTTP

#### Note the API ID from the response and use it in the following commands
API_ID=<api-id>

11. Create an Integration:
    ````sh aws apigatewayv2 create-integration --api-id $API_ID --integration-type AWS_PROXY --integration-uri arn:aws:apigateway:<your-region>:lambda:path/2015-03-31/functions/arn:aws:lambda:<your-region>:<your-account-id>:function:my-fastapi-function/invocations

#### Note the Integration ID from the response and use it in the following commands
INTEGRATION_ID=<integration-id>

12. Create a Route:
    ````sh aws apigatewayv2 create-route --api-id $API_ID --route-key 'ANY /{proxy+}' --target integrations/$INTEGRATION_ID

13. Deploy the API:
   ````shaws apigatewayv2 create-deployment --api-id $API_ID --stage-name prod