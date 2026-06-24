import requests
# CURRENTLY WORKING TO CORRECTLY HANDLE HOW MANY ARTICLES WILL PRINT OUT, HARDCODED FOR NOW

def Fetch_HackerNews_Top_Stories(limit=10): # are we taking in a certain amount of top stories? ex. top 10 stories
    """
        Fetches the top stories from Hacker News using the HackerNews API.
    """
    
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"

    response = requests.get(top_stories_url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch top stories: {response.status_code}") # maybe try another convention here, print statement?

    story_IDs = response.json()[:10]  # maybe make this a parameter to allow for more flexibility in the number of stories fetched
    articles = []


    for story_ID in story_IDs:
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_ID}.json?print=pretty"
        story_response = requests.get(story_url)

        if story_response.status_code != 200:
            print(f"Failed to fetch story {story_ID}: {story_response.status_code}")
            continue

        story_data = story_response.json()
        articles.append(story_data)

    return articles


    # TESTING 

if __name__ == "__main__":
    print("Testing HackerNews API Fetching...")
    results = Fetch_HackerNews_Top_Stories(limit=1)
    print("Top Stories:\n")
    for article in results:
        print(f"Title: {article.get('title')}")
        print(f"URL: {article.get('url')}")
        print(f"Score: {article.get('score')}")
        print(f"By: {article.get('by')}")
        print(f"Time: {article.get('time')}")
        print("-" * 40)
        print()

