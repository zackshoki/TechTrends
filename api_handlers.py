import requests
import time         # NYTIMES limit tracking
import os
from dotenv import load_dotenv




def Fetch_HackerNews_Top_Stories(limit=5):
    """
        Fetches the top stories from Hacker News using the HackerNews API.
    """
    
    top_stories_url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"


    response = requests.get(top_stories_url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch top stories: {response.status_code}") # maybe try another convention here, print statement?

    story_IDs = response.json()  # maybe make this a parameter to allow for more flexibility in the number of stories fetched
    articles = []


    for story_ID in story_IDs:
        if len(articles) == limit:
            break
        story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_ID}.json?print=pretty"
        story_response = requests.get(story_url)

        if story_response.status_code != 200:
            print(f"Failed to fetch story {story_ID}: {story_response.status_code}")
            continue

        story_data = story_response.json()
        if not story_data.get("url"):
            # If the story doesn't have a URL, we skip it
            continue
        articles.append(story_data)

    return articles

    # TESTING 

if __name__ == "__main__":
    print("Testing HackerNews API Fetching...\n")
    results = Fetch_HackerNews_Top_Stories(limit=1)
    print("Top Stories:")
    for article in results:
        print(f"Title: {article.get('title')}")
        print(f"URL: {article.get('url')}")
        print(f"Score: {article.get('score')}")
        print(f"By: {article.get('by')}")
        print(f"Time: {article.get('time')}")
        print("-" * 40)
        print()






#######################







load_dotenv()

def Fetch_NYT_Top_Stories(interest="technology", limit=5):
    """
        Fetches the top stories from The New York Times using the NYT API.
    """

    url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

    api_key = os.getenv("NY_TIMES_API_KEY")  # Ensure you have set your NYT API key in the environment variables

    cleaned_articles = []
    current_page = 0

    while len(cleaned_articles) < limit:
        params = {

            "q" : interest,
            "api-key" : api_key,
            "page": current_page
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad responses

            data = response.json()

            if response.status_code != 200:
                print(f"Failed to fetch NYTimes data: {response.status_code}")
                break


            raw_data = response.json()
            articles_list = raw_data.get("response", {}).get("docs", [])
            
            if not articles_list:
                break
                
            for article in articles_list:
                headline_dict = article.get("headline", {})
                title = headline_dict.get("main", "No Title Available")
                # create variable url to check if link for the article exist
                web_url = article.get("web_url")
                if not web_url:
                    # skip an article if no links
                    continue
                project_article = {
                    "title": title,
                    "url": web_url,
                    "source": "New York Times"
                }
                cleaned_articles.append(project_article)
                
                if len(cleaned_articles) == limit:
                    break
            
            current_page += 1
            time.sleep(1)
            
        except requests.exceptions.RequestException as e:
            print(f"NYTimes Network Error: {e}")
            break

    return cleaned_articles


# TESTING

if __name__ == "__main__":
    print("🚀 Starting API Handler Tests...\n")
    
    # Test 1: Let's try fetching 3 articles about 'artificial intelligence'
    test_interest = "SpaceX IPO"
    test_limit = 3
    
    print(f"📡 Testing NYTimes API with interest: '{test_interest}' (Limit: {test_limit})...")
    
    results = Fetch_NYT_Top_Stories(interest=test_interest, limit=test_limit)
    
    print(f"📊 Received {len(results)} articles back.\n")
    
    # Loop through our results and print them nicely to the terminal
    for index, article in enumerate(results, 1):
        print(f"--- Article #{index} ---")
        print(f"Title : {article.get('title')}")
        print(f"URL   : {article.get('url')}")
        print(f"Source: {article.get('source')}")
        print()
        
    print("🏁 Testing complete!")