# My AWS Cloud Resume Challenge

This repository contains all the code for my submission to the [Cloud Resume Challenge](https://cloudresumechallenge.dev/docs/the-challenge/aws/), a hands-on project designed to build and showcase foundational cloud engineering skills.

## Project Architecture

This project is a static resume website hosted on AWS, featuring a dynamic visitor counter powered by a serverless backend. The entire infrastructure is defined as code and deployed automatically via CI/CD pipelines.

![Architecture Diagram](https://your-link-to-architecture-diagram.com/diagram.png) 
*(Note: You can create a diagram using a tool like diagrams.net and link it here later if you wish!)*

### Frontend
- **Hosting:** The static website (HTML, CSS, JavaScript) is hosted in an **Amazon S3** bucket.
- **Content Delivery Network (CDN):** **Amazon CloudFront** serves the website content globally, providing low-latency access and a secure HTTPS connection via **AWS Certificate Manager (ACM)**.
- **DNS:** **Amazon Route 53** manages the DNS for my custom domain (`muhammadarsalan.site`), pointing it to the CloudFront distribution.

### Backend (Visitor Counter)
- **API:** A RESTful API created with **Amazon API Gateway** provides a public endpoint for the visitor counter.
- **Compute:** An **AWS Lambda** function, written in Python, processes the API requests. It retrieves the current count, increments it, and updates the database.
- **Database:** **Amazon DynamoDB**, a NoSQL database, stores the visitor count.

### CI/CD - Automation
- **Infrastructure as Code (IaC):** The entire backend (Lambda, DynamoDB, API Gateway, IAM Roles) is defined in an **AWS SAM** `template.yaml` file, making the infrastructure repeatable and version-controlled.
- **Continuous Integration & Deployment:** Two separate **GitHub Actions** workflows automate the deployment process:
    1.  **Backend Workflow:** Triggers on changes to the `backend/` folder. It automatically builds and deploys the SAM application to AWS.
    2.  **Frontend Workflow:** Triggers on changes to the `frontend/` folder. It automatically syncs the website files to the S3 bucket and creates a CloudFront invalidation to ensure changes are live immediately.

## What I Learned
Through this challenge, I gained hands-on experience with core AWS services and DevOps principles. The most challenging part was debugging the IAM permissions and the regional mismatch between my API Gateway and Lambda function, which taught me the importance of meticulous configuration and using CloudWatch logs effectively. This project solidified my understanding of serverless architecture, IaC, and the power of CI/CD for building reliable applications.