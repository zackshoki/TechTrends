import requests
# CURRENTLY WORKING TO CORRECTLY HANDLE HOW MANY ARTICLES WILL PRINT OUT, HARDCODED FOR NOW

def Fetch_HackerNews_Top_Stories(limit=5): # are we taking in a certain amount of top stories? ex. top 10 stories
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


# work on how to fetch the repos given the user's request and interests, circle back to the hackernews api as well because I didn't account for this


def Fetch_GitHub_Trending_Repos(interest="python", limit=5):
    """
        Fetches the trending repositories from GitHub using the GitHub API.
    """
    trending_url = f"https://api.github.com/search/repositories?q=language:{interest}&sort=stars&order=desc&per_page={limit}"

    params = {
        "q": interest,        
        "sort": "stars",      
        "order": "desc",      
        "per_page": limit
    }

    try:
        response = requests.get(trending_url, params=params)
        
        if response.status_code != 200:
            print(f"Failed to fetch GitHub repos: {response.status_code}")
            return []
            
        raw_data = response.json()
        
        repo_list = raw_data.get("items", [])
        
        cleaned_projects = []
        
        for repo in repo_list:
            project = {
                "title": repo.get("name"),       
                "url": repo.get("html_url"),     
                "source": "GitHub"            
            }
            cleaned_projects.append(project)
            
        return cleaned_projects

    except requests.exceptions.RequestException as e:
        print(f"GitHub Network Error: {e}")
        return []

 # TESTING
if __name__ == "__main__":
    print("--- Testing w/ different interests ---")
    
    # Test 1
    ml_repos = Fetch_GitHub_Trending_Repos(interest="machine-learning", limit=3)
    print("\n🤖 Machine Learning Repos:")
    for repo in ml_repos:
        print(f"- {repo['title']}: {repo['url']}")
        
    # Test 2
    js_repos = Fetch_GitHub_Trending_Repos(interest="javascript", limit=2)
    print("\n🌐 JavaScript Repos:")
    for repo in js_repos:
        print(f"- {repo['title']}: {repo['url']}")