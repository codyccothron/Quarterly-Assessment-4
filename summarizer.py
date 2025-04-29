import openai
from config_settings import OPENAI_API_KEY

# Set up OpenAI client with your API key
client = openai.Client(api_key=OPENAI_API_KEY)

def summarize_text(title, description):
    content = f"Title: {title}\nDescription: {description}"
    try:
        # Use the updated client.chat.completions.create method
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI assistant summarizing news articles concisely."},
                {"role": "user", "content": f"Summarize this article:\n{content}"}
            ]
        )
        # Extract the summarized response
        summary = response.choices[0].message.content
        return summary
    except openai.error.OpenAIError as e:
        return f"Error occurred: {e}"

if __name__ == "__main__":
    sample_title = "Breaking News: AI Revolutionizes Industries"
    sample_description = "AI technology is reshaping industries globally, introducing automation in ways never seen before."
    print(summarize_text(sample_title, sample_description))