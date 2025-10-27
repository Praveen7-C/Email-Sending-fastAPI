import smtplib
from fastapi import FastAPI, HTTPException
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pydantic import BaseModel
import os
from mangum import Mangum
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Define a model to parse the incoming request
class EmailRequest(BaseModel):
    receiver_email: str
    subject: str
    body_text: str

# Initialize FastAPI app
app = FastAPI()

@app.post("/send-email")
async def send_email(email_request: EmailRequest):
    # Gmail SMTP settings
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  # Use 465 for SSL, but 587 is for STARTTLS
    sender_email = os.getenv('GMAIL_USER')  # Your Gmail address (from environment variable)
    app_password = os.getenv('GMAIL_APP_PASSWORD')  # App password from environment variable

    # Check if environment variables are set
    if not sender_email or not app_password:
        raise HTTPException(
            status_code=500,
            detail="Missing environment variables. Make sure GMAIL_USER and GMAIL_APP_PASSWORD are set in .env file"
        )

    # Prepare the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email_request.receiver_email
    msg['Subject'] = email_request.subject

    # Attach the body text to the email
    msg.attach(MIMEText(email_request.body_text, 'plain'))

    try:
        # Connect to Gmail's SMTP server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection with TLS
        server.login(sender_email, app_password)
        server.sendmail(sender_email, email_request.receiver_email, msg.as_string())
        server.quit()  # Close the connection

        return {"message": "Email sent successfully!"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error sending email: {str(e)}")

# Create a Lambda handler using Mangum to adapt FastAPI for Lambda
handler = Mangum(app)
