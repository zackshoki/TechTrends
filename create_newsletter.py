import requests
from google import genai

geminiAPIKey = "AQ.Ab8RN6IMqa05vGVB7tEhpfi682XxEmKJyM9zn4QPicKCC9MtXA"

gemini = genai.Client(
  api_key=geminiAPIKey
)
