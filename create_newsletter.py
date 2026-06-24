import requests
from google import genai

geminiAPIKey = ""

gemini = genai.Client(
  api_key=geminiAPIKey
)

import requests
import json
from bs4 import BeautifulSoup

def extract_article_text(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()
    paragraphs = soup.find_all("p")
    article_text = " ".join(p.get_text() for p in paragraphs)
    return article_text[:5000]

def summarize_article(article_text, title):
    prompt = f"""You are writing a technology newsletter.
Create a newsletter entry from this article.

Rules:
- Only use information from the article
- Do not invent facts
- Return ONLY valid JSON
- No markdown
- No extra text

Return this format:
{{
    "headline": "short catchy headline",
    "body": "3-5 sentence newsletter summary"
}}

Article title:
{title}

Article text:
{article_text}"""

    response = client.models.generate_content(model="gemini-2.0-flash", contents=prompt)
    return json.loads(response.text)

def create_newsletter_entry(title, url):
    text = extract_article_text(url)
    return summarize_article(text, title)

if __name__ == "__main__":
    pass