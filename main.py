#!/usr/bin/env python3
# import requests
import database
import users
import sqlite3
import api_handlers


if __name__ == "__main__":

    # start database
    database.initialize_database()

    # check if the user exists in the database
    while True:
        username = input("Enter your username: ")
        # user_exist = users.get_user(username)
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
    print("3. Edit your interests")
    print("4. Exit\n")

def source_menu():
    print("\n --- SOURCES ---")
    print("1. HackerNews")
    print("2. New York Times")



while True:
    menu()
    choice = input("Enter your choice: ")
    # check if the choice is valid
    while choice not in ["1", "2", "3", "4"]:
        choice = input("Invalid choice. Please enter 1, 2, 3, or 4: ")
    # IF USERS CHOICE 1 - FETCH ARTICLES
    if choice == "1":
        # import gemini
        import create_newsletter
            #  user inputs a number of articles
        # print("Searching...\n")
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
            ask_go_back_to_manu = input("\nDo you want to see more articles? (y/n): ").lower()
            while ask_go_back_to_manu not in ["y", "n"]:
                ask_go_back_to_manu = input("Invalid choice. Please enter 'y' or 'n': ").lower()
            if ask_go_back_to_manu == "n":
                break
    # IF USERS CHOICE 2 - PRINT USER INTERESTS
    elif choice == "2":
        # output user interests
        user_interests = users.get_user_interests(user_id)
        print(f"\nYour interests are: {user_interests}\n")
    # IF USERS CHOICE 3 - EDIT USER INTERESTS
    elif choice == "3":
        user_interests = users.get_user_interests(user_id)
        print(f"\nYour interests are: {user_interests}\n")
        print(f"\n Type 'add' to add to your interests \n Type 'remove' to remove an interest \n Type 'back' to go back to the main menu\n")
        choice_to_edit_interests = input("Enter your choice: ").lower()
        while choice_to_edit_interests not in ["add", "remove", "back"]:
            choice_to_edit_interests = input("Invalid choice. Please enter 'add', 'remove', or 'back': ").lower()
        if choice_to_edit_interests == "add": 
                new_interest = input("Enter the interest you want to add: ")
                # get current interests and append new interest
                current_interests = users.get_user_interests(user_id)
                updated_interests = current_interests + ", " + new_interest
                users.save_user_interest_database(user_id, updated_interests)
                print(f"\nYour interests now are: {updated_interests}\n") 
        elif choice_to_edit_interests == "remove":
                current_interests = users.get_user_interests(user_id)
                print(f"\nYour current interests are: {current_interests}\n")
                interest_to_remove = input("Enter the interest you want to remove: ")
                # remove interest from current interests
                updated_interests = ", ".join([interest.strip() for interest in current_interests.split(",") if interest.strip().lower() != interest_to_remove.lower()])
                if updated_interests == current_interests:
                    print(f"\n{interest_to_remove} is not in your interests.\n") 
                else:
                    users.save_user_interest_database(user_id, updated_interests)
                    print(f"\nYour interests now are: {updated_interests}\n")
    elif choice == "4":
        break
    














