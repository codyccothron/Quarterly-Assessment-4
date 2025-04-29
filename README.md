# Quarterly-Assessment-4
AI Powered Newsletter that will generate summarized news from your daily Fox News websites

# Fox News Aggregator
This project automates the process of **fetching, summarizing, and delivering daily Fox News updates via email** using Python, OpenAI, and Windows Task Scheduler.

## **Features**
- **Automatically fetches the latest Fox News articles** via RSS.
- **Uses OpenAI API** to generate concise summaries.
- **Formats news & sends a daily email report**.
- **Runs automatically at 8:00 AM** using Windows Task Scheduler.

---

## **Prerequisites**
Before setting up the project, ensure you have:
- **Python 3.11+** installed.
- Dependencies installed via `requirements.txt`.
- **Gmail account** with App Password enabled (for SMTP).
- OpenAI API Key for summarization.

---

## Setup Guide
Follow these steps to set up your automated Fox News aggregator.

### Step 1: Clone the Repository
git clone https://github.com/codyccothron/Quarterly-Assessment-4.git
cd Quarterly-Assessment-4

### Step 2: Install requirements
 pip install -r requirements.txt

### **Step 3: Configure Environment Variables**
Create a `.env` file inside the project folder with the following content:

API Configuration:
NEWS_API_KEY=your_news_api_key_here
OPENAI_API_KEY=your_openai_api_key_here

Email Configuration:
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password_here
EMAIL_RECIPIENT=recipient@example.com


**Important Notes:
- Use a Google App Password instead of your actual email password for security.
- Replace your_news_api_key_here and your_openai_api_key_here with valid API keys.
- Ensure .env is added to .gitignore to prevent exposing sensitive credentials.

### Step 4: Test Each Component

Run each .py file to insure output is working, they should be, contact user if not.

### Step 5: Run Full Automation
Run main.py to run the code and send an email with a news summary from Fox News
-Run main.py through Windows Task Scheduler to automate this process




