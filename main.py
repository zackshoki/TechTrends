#!/usr/bin/env python3
import requests
import database
import users
import sqlite3
import create_newsletter
import api_handlers




# start database
database.initialize_database()

# check if the user exists in the database
while True:
    username = input("Enter your username: ")
    user_exist = users.get_user(username)
    if user_exist:
        # if exist output that its taken and ask again
        print(f"The username {username} is already taken. Please choose another one")
    else:
        break

#  create a new user in the database
id = users.create_user(username)
interests = input("Enter your interests (comma-separated): ")
# save users interest 
users.save_user_interest_database(id, interests)
print(f"Hi {username}. Welcome to TechTrends newsletter")


def menu():
    print("1. View latest tech trends")
    print("2. View your interests")
    print("3. Exit")

while True:
    menu()
    choice = input("Enter your choice: ")
    # check if the choice is valid
    while choice not in ["1", "2", "3"]:
        choice = input("Invalid choice. Please enter a valid number: ")
    if choice == "1":
        #  user inputs a number of articles
        number_of_articles = int(input("Enter the number of articles you want to see (default is 3): "))
        # if invalid number of articles ask to enter valid
        while number_of_articles <= 0:
            number_of_articles = int(input("Please enter the number of articles greater than 0: "))
        # get the latest tech trends from HackerNews API limit amout to the user number
        stories = api_handlers.Fetch_HackerNews_Top_Stories(limit=number_of_articles)
        entries = []
        for i in range(number_of_articles):
            entries.append(create_newsletter.create_newsletter_entry(stories[i]["title"], stories[i]["url"]))

        newsletter = create_newsletter.assemble_newsletter(entries)
        print(newsletter["title"])
        print()
        for i in range(number_of_articles):
            print(str(i+1) + ". " + newsletter["entries"][i]["headline"])
            print(newsletter["entries"][i]["url"])
            print()
        print()   
        choice2 = input("Summary? (Y/N): ")
        if choice2 == "N" or choice2 == "n":
            pass
        elif choice2 == "Y" or choice2 == "y": 
            choice3 = input("Choose which article (Enter a number): ")
            print(newsletter["entries"][int(choice3)-1]["body"])
        else:
            while choice2 not in ["Y", "N", "y", "n"]:
                choice2 = input("Invalid. Please enter Y or N: ")
       
    elif choice == "2":
        # output user interests
        user_interests = users.get_user_interests(id)
        print(f"\nYour interests are: {user_interests}\n")
        # implement a function to add or remove interests
        # print("If you want to add to your interest type 'add' or if you want to remove an interest type 'remove' or type 'back' to go back to the main menu")
    elif choice == "3":
        break
















