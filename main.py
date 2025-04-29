import logging
from news_fetcher import fetch_fox_news
from summarizer import summarize_text
from email_sender import send_email

# Configure logging to write to logs/app.log
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_daily_fox_news():
    try:
        logging.info("Fetching latest Fox News articles...")
        articles = fetch_fox_news()

        if not articles:
            logging.warning("No articles were retrieved.")
            return

        logging.info(f"Retrieved {len(articles)} articles. Summarizing them...")
        summaries = []
        for article in articles:
            try:
                summary = summarize_text(article.title, article.description)
                summaries.append(f"<b>{article.title}</b><br>{summary}<br><a href='{article.link}'>Read More</a>")
            except Exception as e:
                logging.error(f"Error summarizing article '{article.title}': {e}")

        formatted_news = "<br><br>".join(summaries)

        logging.info("Sending email with news summary...")
        send_email("Daily Fox News Update", formatted_news)

        logging.info("Email sent successfully. Process completed.")
    except Exception as e:
        logging.error(f"Critical error in execution: {e}")

if __name__ == "__main__":
    logging.info("Starting Fox News Aggregator script...")
    run_daily_fox_news()