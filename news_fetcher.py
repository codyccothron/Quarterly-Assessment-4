import feedparser

def fetch_fox_news():
    URL = "https://feeds.foxnews.com/foxnews/latest"
    feed = feedparser.parse(URL)
    articles = feed.entries[:5]  # Fetch top 5 articles
    return articles

if __name__ == "__main__":
    news = fetch_fox_news()
    for i, article in enumerate(news):
        print(f"{i+1}. {article.title} - {article.link}")