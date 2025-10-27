# Email API FastAPI with Serverless

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![AWS Lambda](https://img.shields.io/badge/AWS_Lambda-FF9900?style=for-the-badge&logo=aws-lambda&logoColor=white)](https://aws.amazon.com/lambda/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](https://gmail.com)

A production-ready serverless **Email API** built with **FastAPI** and deployed on **AWS Lambda**. Send emails securely using Gmail's SMTP server with modern authentication. Perfect for adding email functionality to your applications without managing email servers.

## Quick Start

```bash
# Clone the repository
git clone https://github.com/Praveen7-C/Email-Sending-fastAPI.git
cd Email-Sending-fastAPI

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Set up environment variables (see Configuration section)
cp .env  # Then edit .env with your credentials

# Run the application
uvicorn app:app --reload
```

## Key Features

- **FastAPI** - Modern, fast web framework for building APIs
- **Gmail SMTP** - Reliable email delivery using Gmail's SMTP server
- **Serverless** - Deploy to AWS Lambda with zero server management
- **Swagger UI** - Interactive API documentation and testing
- **Secure** - Environment-based configuration and app password authentication

## Features
- **FastAPI** for API development.
- **Gmail SMTP** to send emails.
- **Serverless Framework** for deployment to AWS Lambda.
- **Swagger UI** for interactive API documentation and testing.

## Project Structure
```
Email-Sending-fastAPI/
├── app.py              # Main FastAPI application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (create this, not in git)
├── serverless.yml     # Serverless Framework configuration
└── README.md          # Project documentation
```

## Prerequisites

- Python 3.8 or above
- AWS Account with Lambda and API Gateway access
- Serverless Framework installed
- Gmail Account with 2-step verification enabled

## Setup

1. **Install Dependencies**:
   First, install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. **Gmail Setup and Environment Variables**:

   a. **Create Gmail App Password**:
   1. Go to your [Google Account Security Settings](https://myaccount.google.com/security)
   2. Enable 2-Step Verification if not already enabled
   3. Search for "App passwords" or scroll down to find it
   4. Click on "App passwords" (you might need to enter your password)
   5. Under "Select app", choose "Other (Custom name)"
   6. Enter a name for the app (e.g., "FastAPI Email Service")
   7. Click "Generate"
   8. Google will generate a 16-character password - **COPY THIS PASSWORD**
   9. Click "Done"

   b. **Set Up Environment Variables**:
   Create a `.env` file in the project root directory with the following content:
   ```
   GMAIL_USER=your-email@gmail.com
   GMAIL_APP_PASSWORD=your-16-character-app-password
   ```
   Replace with your actual values:
   - `your-email@gmail.com`: Your full Gmail address
   - `your-16-character-app-password`: The 16-character app password you just generated

   Important Notes:
   - Never share or commit your `.env` file to version control
   - The app password is different from your regular Gmail password
   - Make sure there are no spaces or quotes around the values
   - Don't use the `export` keyword in the `.env` file

3. **Install Serverless Framework**:
   If you haven't installed Serverless Framework, you can do so globally with:
   ```bash
   npm install -g serverless
   ```

4. **Run Locally**:
   There are two ways to run the application locally:

   a. **Using Uvicorn (Recommended for Development)**:
   ```bash
   uvicorn app:app --reload
   ```
   This will start the server at `http://localhost:8000` with auto-reload enabled.

   b. **Using Serverless Offline** (For testing serverless setup):
   First, install the serverless-offline plugin:
   ```bash
   npm install serverless-offline --save-dev
   ```
   Then, start the server:
   ```bash
   serverless offline start
   ```
   This will run the API locally at `http://localhost:3000`.

   You can access Swagger UI by adding `/docs` to either URL to interact with the API.

5. **Deploy to AWS**:
   When you're ready to deploy your API, use the following command:
   ```bash
   serverless deploy
   ```
   After deployment, you will receive a URL to access your API via AWS API Gateway.

## Testing the API

### Using Swagger UI
1. Open your browser to `/docs` endpoint:
   - Local: http://localhost:8000/docs
   - Production: https://your-api-gateway-url/docs

2. Click on the POST `/send-email` endpoint
3. Click "Try it out"
4. Use the example payload:

```json
{
  "receiver_email": "your-target-email@example.com",
  "subject": "Test Email",
  "body_text": "This is a test email sent via FastAPI and Serverless."
}
```

### Using cURL
```bash
curl -X POST "http://localhost:8000/send-email" \
     -H "Content-Type: application/json" \
     -d '{
       "receiver_email": "receiver@example.com",
       "subject": "Test Email",
       "body_text": "This is a test email sent via FastAPI and Serverless."
     }'
```

### Using Python
```python
import requests
import json

url = "http://localhost:8000/send-email"
payload = {
    "receiver_email": "receiver@example.com",
    "subject": "Test Email",
    "body_text": "This is a test email sent via FastAPI and Serverless."
}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.json())

## API Documentation

Once the server is running locally, you can access the interactive API documentation at:
- **Swagger UI**: `http://localhost:3000/docs`

### API Endpoint
- **POST** `/send-email`: Sends an email via Gmail SMTP.

**Request Body:**
```json
{
  "receiver_email": "receiver@example.com",
  "subject": "Subject of the Email",
  "body_text": "Body text of the email"
}
```

**Response:**
```json
{
  "message": "Email sent successfully!"
}
```

## Development vs Production

### Development Mode
When developing locally using `uvicorn`, you get these benefits:
- Fast reload on code changes
- Direct access to logs in the terminal
- Easier debugging capabilities
- Swagger UI at `http://localhost:8000/docs`

### Production/Serverless Mode
When deployed to AWS Lambda:
- Serverless architecture with auto-scaling
- Pay-per-use pricing
- Integrated with AWS services
- Swagger UI available at your API Gateway URL + `/docs`

## Security Best Practices

### Environment Variables
- Never commit `.env` to version control
- Add `.env` to `.gitignore`
- Rotate app passwords regularly
- Use secure password storage in production

### Production Security
- Use AWS Secrets Manager for credentials
- Configure CORS in `serverless.yml`
- Implement rate limiting
- Monitor email sending patterns
- Set up logging and alerting
- Use HTTPS endpoints only

### Gmail Account Security
- Enable 2-Step Verification
- Regular security audits
- Monitor app password usage
- Remove unused passwords
- Use organizational email for production

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Serverless Framework](https://www.serverless.com/)
- [Gmail SMTP Settings](https://support.google.com/mail/answer/7126229)
- [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/)

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Authors

- C. Praveen  - [GitHub Profile](https://github.com/Praveen7-C)

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the amazing framework
- [Serverless Framework](https://www.serverless.com/) for deployment tools
- [Gmail](https://gmail.com) for email services

## License
This project is licensed under the MIT License.
