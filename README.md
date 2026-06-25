## README file

# TechTrends

TechTrends is a CLI application that fetches the newest tech trends from a few different sources. A user creates a profile with a list of interests. After that, the user is able to pick an article of interest and request a summary. Articles are tracked in the database to avoid showing the same article multiple times.

<!-- add a sentence if feature implemented: user can see the articles he already viewed -->

## Who is it for

Developers, students, and anyone interested in tech who wants a quick way to catch up on tech news without searching through multiple websites and full length articles.

## How it's used

It is a command-line interface, so everything is done in the terminal.

## APIs used

- Hacker News
- Google Gemini API for article summarization
- Beautiful Soup

## Inputs

- Username: entered once, and a way to identify the user in the database
- Interests: comma-separated input entered once at the beginning of the session, with the ability to rewrite it later
- Menu selection: a number chosen from the printed menu to make a choice

## Outputs

- Initial welcome message
- Menu with choice selection
- List of articles to choose from
- Printed summary of the article the user selects

## Step-by-Step Flow

1. Program starts;
2. User enters a username; if it already exists, they are asked to choose another
3. New users enter their interests, which are saved to the database
4. Main menu is shown with the available choices
5. On "view latest tech trends," the program fetches articles from the connected sources and shows a list of titles and links
6. User picks an article
7. The selected article is sent to the Gemini API and using a Beautiful API a summary is printed
8. The article is marked as read so it will not be shown again
9. On "view interests," the user's saved interests are shown, with the option to update them
10. User can return to the menu or exit the program

## How the Data Is Stored

A local SQLite database holds two main tables:

- users: user_id, username, interests, created_at
- articles: article_id, title, url, source, publication_date, and a read status used to avoid repeating articles

## Tech Stack

- SQLite
- Hacker News API
- Google Gemini API

## Team

- Tanya
- Zack
- Tola

