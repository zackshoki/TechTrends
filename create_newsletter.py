import requests
from google import genai

geminiAPIKey = ""

gemini = genai.Client(
  api_key=geminiAPIKey
)
