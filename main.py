#!/usr/bin/env python3
import requests
import database
import users
import sqlite3
import create_newsletter
import api_handlers


database.initialize_database()


username = input("Enter your username: ")
id = users.create_user(username)
interests = input("Enter your interests (comma-separated): ")
users.save_user_interest_database(id, interests)
print(f"Hi {username}. Welcome to TechTrends newsletter")

stories = api_handlers.Fetch_HackerNews_Top_Stories(limit=3)
entries = []
for i in range(3):
    entries.append(create_newsletter.create_newsletter_entry(stories[i]["title"], stories[i]["url"]))

newsletter = create_newsletter.assemble_newsletter(entries)
print(newsletter["title"])
print(newsletter["intro"])
print()
print(newsletter["entries"][0]["headline"])
print(newsletter["entries"][0]["body"])
print()
print(newsletter["entries"][1]["headline"])
print(newsletter["entries"][1]["body"])
print()
print(newsletter["entries"][2]["headline"])
print(newsletter["entries"][2]["body"])


