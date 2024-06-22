import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///whiteboard_assistant.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'your_secret_key_here')
    EMAIL_USER = os.getenv('EMAIL_USER', 'user@example.com')
    EMAIL_PASS = os.getenv('EMAIL_PASS', 'yourpassword')