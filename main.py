from news_fetcher import fetch_fox_news
from summarizer import summarize_text
from email_sender import send_email

def run_daily_fox_news():
    articles = fetch_fox_news()
    summaries = []
    for article in articles:
        summary = summarize_text(article.title, article.description)
        summaries.append(f"<b>{article.title}</b><br>{summary}<br><a href='{article.link}'>Read More</a>")

    formatted_news = "<br><br>".join(summaries)
    send_email("Daily Fox News Update", formatted_news)

if __name__ == "__main__":
    run_daily_fox_news()