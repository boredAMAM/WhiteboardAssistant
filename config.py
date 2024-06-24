import os
from dotenv import load_dotenv

try:
    load_dotenv()
except Exception as e:
    print(f"Error loading the .env file: {e}")

class Config:
    try:
        DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///whiteboard_assistant.db')
        SECRET_KEY = os.getenv('SECRET_ptrKEY', 'your_secret_key_here')
        EMAIL_USER = os.getenv('EMAIL_USER', 'user@example.com')
        EMAIL_PASS = os.getenv('EMAIL_PASS', 'yourpassword')
    except Exception as config_error:
        print(f"An error occurred when accessing environment variables: {config_inforector}")