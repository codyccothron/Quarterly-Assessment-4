import openai
from config_settings import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def summarize_text(title, description):
    content = f"Title: {title}\nDescription: {description}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI assistant summarizing news articles concisely."},
            {"role": "user", "content": f"Summarize this article:\n{content}"}
        ]
    )
    summary = response["choices"][0]["message"]["content"]
    return summary

if __name__ == "__main__":
    sample_title = "Breaking News: AI Revolutionizes Industries"
    sample_description = "AI technology is reshaping industries globally, introducing automation in ways never seen before."
    print(summarize_text(sample_title, sample_description))