# Database_Gossip
This is a AWS Cloud-based application that seamlessly captures and stores user-submitted names using cutting-edge AWS technologies. This project leverages the power of **AWS Amplify** for frontend development and deployment, creating a responsive and user-friendly interface

The application's architecture is built on a serverless foundation, utilizing **AWS Lambda functions** to process incoming requests efficiently. These functions are triggered through **API Gateway**, which acts as a secure front door for the application's API

At the heart of Database_Gossip lies **Amazon DynamoDB**, a fast and flexible NoSQL database service perfectly suited for storing and retrieving name entries at scale. The project implements robust security measures through **AWS Identity and Access Management (IAM)**, ensuring that only authorized entities can access and manipulate the stored data

# Key features of Database_Gossip include:
1: Real-time data synchronization
2: Offline data access capabilities
3: Seamless integration with various frontend frameworks
4: Automatic scaling to handle high traffic loads


## Image As shown Below as Data or values being updated FROM UI
![image](https://github.com/user-attachments/assets/c702a90e-5b16-4e8c-8f0c-a1c6b0d00a74)


## Image as shown below vis API GATEWAY updated TO Dynamo DB Database
![image](https://github.com/user-attachments/assets/98b2ca5e-3e7d-44fd-8bbb-2bb11856f075)


# User Interface Description: 
The project features a simple and intuitive web-based user interface designed for efficient name submission. The UI consists of the following elements:

1: Input Fields:
  -> A text input for entering the user's First Name
  -> A text input for entering the user's Last Name

2: Submit Button: 

  -> A button labeled "Submit" that allows users to send their entered name information

This clean and straightforward interface allows users to easily input and submit their full names. The design focuses on simplicity, making it accessible for users of all technical levels. When the submit button is clicked, the entered first and last names are likely processed and stored in the backend DynamoDB database through the AWS services infrastructure.

The UI serves as the entry point for the Database_Gossip application, providing a user-friendly way to interact with the underlying AWS services, including Lambda functions, **API Gateway**, and DynamoDB. Its minimalist design ensures fast loading times and compatibility across various devices and browsers.


# Lambda Handler Function Description

The lambda_handler function is the core component of the serverless application, responsible for processing incoming events and interacting with the DynamoDB database. Here's a detailed breakdown of its functionality:

1: Time Retrieval and Formatting:
  -> The function retrieves the current Greenwich Mean Time (GMT) using Python's time module.
  -> It then formats this time into a human-readable string format.

2: Event Data Extraction:
  -> The function extracts the firstName and lastName from the incoming event object, which is typically triggered by an API Gateway request.
  -> It combines these values to form a full name.

3: Database Interaction:
  -> Using the AWS SDK for Python (boto3), the function interacts with a DynamoDB table named 'mydatabaseapp'.
  ->It writes an item to this table, consisting of the full name as the ID and the formatted current time as LatestGreetingTime.

4:Response Generation:
  -> The function returns a JSON object containing an HTTP status code and a message that greets the user by their full name.

This Lambda function efficiently handles incoming data, stores it in DynamoDB, and provides a response, demonstrating the seamless integration of AWS services in a serverless architecture.

