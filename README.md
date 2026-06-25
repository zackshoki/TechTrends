## README file

TechTrends


TechTrends is a CLI application that fetches newest tech trends from few different sources. A user creates a profile with a list of interests. After that user is able to pick article of interests and request a summary. Articles are tracked in the database to avoid showing the same articles multiple times. 

<!-- add a sentence if feature implememnted - user can see the articles he already viewed -->

Who is it for:
    developers, student, anyone who is interested in tech and want quick way to catch up on tech news without searching throught multiple websites and full-size articles
How it's used: 
    It is a command-line interface, so everything is done in the terminal
ARIs used:


Inputs:
    • Username - entered once, and a way to identify the user in the database
    • interests - comma-separated input entered once in the beginning of the session and with an ability to rewrite it later
    • Menu selection - a number chosen from the printed menu to make a choice
Outputs:
    • Initial Welcome message 
    • Menu with choice selection
    • List of articles to choose
    • Printed summary of the article user selects

Step-by-Step Flow
    1. Program starts; database tables are created
    2. 