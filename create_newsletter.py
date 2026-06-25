import requests
import json
from bs4 import BeautifulSoup
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

geminiAPIKey = os.getenv("geminiAPIKey")

gemini = genai.Client(
  api_key=geminiAPIKey
)


def extract_article_text(url): # given a url, get the article's text as a string using BeautifulSoup API
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "nav", "footer"]):
        tag.decompose()
    paragraphs = soup.find_all("p")
    article_text = " ".join(p.get_text() for p in paragraphs)
    return article_text[:5000]

def summarize_article(article_text, title): # given the text from an article, create an entry for our newsletter in the form of a string
    prompt = f"""You are writing a technology newsletter.
Create a newsletter entry from this article.

Rules:
- Only use information from the article
- Don't use any vulgar language, and make sure entry-level devs can understand
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

    response = gemini.models.generate_content(model="gemini-3.1-flash-lite", contents=prompt)
    return json.loads(response.text)

def create_newsletter_entry(title, url): # given a title and url, create a string entry for a newsletter
    text = extract_article_text(url)
    entry = summarize_article(text, title)
    entry["url"] = url
    return entry

def assemble_newsletter(entries):  # given several newsletter entries, generate a full newsletter with title and intro
    if not entries:
        return "No articles available for this issue."

    sections = "\n\n".join(
        f"Headline: {e['headline']}\nSummary: {e['body']}\nLink: {e['url']}"
        for e in entries
    )

    prompt = f"""You are formatting a technology newsletter from pre-written entries below.
Rules:
- Do not invent facts or add new information
- Keep each entry's headline and summary content exactly as given
- Write a short, catchy newsletter title (not generic, related to the entries)
- Write a 2-3 sentence intro that previews what's in this issue
- Please don't do too much
- Return ONLY valid JSON, no markdown, no extra text

Return this format:
{{
    "title": "newsletter title",
    "intro": "2-3 sentence intro",
    "entries": [
        {{"headline": "...", "body": "...", "url": "..."}}
    ]
}}

Entries:
{sections}"""

    response = gemini.models.generate_content(model="gemini-3.1-flash-lite", contents=prompt)
    return json.loads(response.text)

if __name__ == "__main__":
    pass