#!/usr/bin/env python3
# import requests
import database
import users
import sqlite3
import api_handlers




# start database
database.initialize_database()

# check if the user exists in the database
while True:
    username = input("Enter your username: ")
    user_exist = users.get_user(username)
    # if input is empty ask again
    if not username:
        print("Username cannot be empty.")
        continue
    # get user's username
    if users.get_user(username):
        # if exist output that its taken and ask again
        print(f"{username} is already taken. Please choose another one")
    else:
        break

#  create a new user in the database
user_id = users.create_user(username)
interests = input("Enter your interests (comma-separated): ")
# if interests is empty
while not interests:
    interests = input("Interests cannot be empty. Please enter your interests (comma-separated): ") 
# save users interest 
users.save_user_interest_database(user_id, interests)
# print welcome message
print(f"\nHi {username}. Welcome to TechTrends newsletter\n")

# MENU
def menu():
    print("\n --- MENU ---")
    print("1. View latest tech trends")
    print("2. View your interests")
    print("3. Exit\n")

def source_menu():
    print("\n --- SOURCES ---")
    print("1. HackerNews")
    print("2. New York Times")



while True:
    menu()
    choice = input("Enter your choice: ")
    # check if the choice is valid
    while choice not in ["1", "2", "3"]:
        choice = input("Invalid choice. Please enter 1, 2, or 3: ")
    # IF USERS CHOICE 1 - FETCH ARTICLES
    if choice == "1":
        # import gemini
        import create_newsletter
            #  user inputs a number of articles
        while True:
            source_menu()
            source_choice = input("\nEnter your choice: ")
            while source_choice not in ["1", "2"]:
                source_choice = input("Invalid choice. Please enter 1 or 2: ")
            number_of_articles = int(input("How many articles would you want: "))
            # if invalid number of articles ask to enter valid
            while number_of_articles <= 0:
                number_of_articles = int(input("Invalid choice. Please enter the number of articles: ")) 
            # IF SOURCE CHOICE 1 - FETCH HACKERNEWS ARTICLES
            if source_choice == "1":
                # get the latest tech trends from HackerNews API limit amout to the user number
                stories = api_handlers.Fetch_HackerNews_Top_Stories(limit=number_of_articles)
            # OTHERWISE- FETCH NYT articles
            elif source_choice == "2":
                stories = api_handlers.Fetch_NYT_Top_Stories(interest="technology", limit=number_of_articles)
            entries = []
            for i in range(number_of_articles):
                entries.append(create_newsletter.create_newsletter_entry(stories[i]["title"], stories[i]["url"]))
            newsletter = create_newsletter.assemble_newsletter(entries)
            print()
            for i in range(number_of_articles):
                print(str(i+1) + ". " + newsletter["entries"][i]["headline"])
                print(newsletter["entries"][i]["url"])
                print()
            choice3 = input("Choose an article to summarize (Enter a number): ")
            print()
            print("\n", newsletter["entries"][int(choice3)-1]["body"]) 
            #  keep asking if they want more articles until they want to go back to the
            if input("\nDo you want to go back to the main menu? (y/n): ").lower() == "y" :
                break
        
        
    
    elif choice == "2":
        # output user interests
        user_interests = users.get_user_interests(user_id)
        print(f"\nYour interests are: {user_interests}\n")
        # implement a function to add or remove interests
        # print("If you want to add to your interest type 'add' or if you want to remove an interest type 'remove' or type 'back' to go back to the main menu")
    elif choice == "3":
        break














