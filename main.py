#!/usr/bin/env python3
import requests
import database
import users
import sqlite3

database.initialize_database()


username = input("Enter your username: ")
id = users.create_user(username)
interests = input("Enter your interests (comma-separated): ")
users.save_user_interest_database(id, interests)
print(f"Hi {username}. Welcome to TechTrends newsletter")


