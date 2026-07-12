import google.generativeai as genai
from dotenv import load_dotenv
import os


# load .env
load_dotenv()


# get api key
api_key = os.getenv("GEMINI_API_KEY")


genai.configure(
    api_key=api_key
)


# CREATE MODEL (you were missing this)
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


response = model.generate_content(
    "Say hello from Prepo AI"
)


print(response.text)