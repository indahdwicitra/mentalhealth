# __Mental Health Support App REST API Documentation__

## Overview
This documentation provides an overview of the REST API for Login and Register, including the setup, structure, and available endpoints. This API is designed to handle the Login and Register processes in the application and store user data in the MongoDB database.

## Project Structure
mental-health-login/
├── src/
│   └── config/
|       └──database.js
|   └── controllers/
|       └── authController.js
|   └── middleware/
|       └──authMiddleware.js
|   └── models/
|       └── User.js
|   └── routes/
|       └── auth.js
|   └── server.js
├── node_modules/
├── Dockerfile
├── package.json
├── package-lock.json

## File Descriptions

- database.js: Configures the connection to the database (MongoDB).
- authController.js: Handles the logic for the login and registration processes.
- authMiddleware.js: Middleware to check user authentication before accessing certain routes.
- User.js: Defines the schema and model for user data stored in the database.
- auth.js: Defines routes for authentication operations, such as login and registration.
- server.js: Starts the Express server and configures routes and middleware.
- Dockerfile: Defines the instructions for building the Docker image for the application.
- package.json: Stores project metadata and a list of npm dependencies.
- package-lock.json: Records the exact versions of installed dependencies to maintain consistency.

## Setting Up the API
### Prerequisites
Node.js (version 16 or higher)
Docker (optional, for containerization)

## Installation

```
### Install dependencies:
```
npm install
```
### Run the server:
```
npm start
The server will start on port 8080 by default.
```
## Docker Setup

### Build the Docker image:
```
docker build -t h-mental-health-login .
```
### Run the Docker container:
```
docker run -p 8080:8080 mental-health-login
```

## API Endpoint
###Get Articles
- URL: api/auth/register
- Method: POST
- Description: To perform registration.
- Deployed URL: https://mental-health-login-599630883190.asia-southeast2.run.app

## Request
No request body or parameters are needed for this endpoint.

## Response
Status: 200 OK
Content-Type: application/json
Body: 
```
{
    "message": "Registrasi berhasil",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY3NTUwNTJmZWUxOTc4NWE5MzAxYzcwYSIsImlhdCI6MTczMzYyNTEzNSwiZXhwIjoxNzMzNjI4NzM1fQ.zGKZTVd6NDEsbdEYSkf9DQJ4IpYYuH1QjzY6IN-bvKo",
    "user": {
        "id": "6755052fee19785a9301c70a",
        "username": "indahdc",
        "email": "indahdc@gmail.com"
    }
}
