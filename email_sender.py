import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config_settings import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECIPIENT

def send_email(subject, body):
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = ", ".join(EMAIL_RECIPIENT)

    html_content = f"""
    <html>
    <head>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                padding: 20px;
            }}
            .container {{
                max-width: 600px;
                margin: auto;
                background-color: #ffffff;
                border-radius: 8px;
                overflow: hidden;
                box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                background-color: #0046be;
                color: white;
                text-align: center;
                padding: 30px;
                font-size: 32px;
                font-weight: bold;
                text-transform: capitalize; /* Ensures title case formatting */
            }}
            .subheading {{
                font-size: 18px;
                font-weight: bold;
                color: #d71920;
                margin-top: 20px;
            }}
            .content {{
                padding: 25px;
                font-size: 16px;
                color: #333;
                line-height: 1.8;
            }}
            .footer {{
                text-align: center;
                font-size: 14px;
                color: #777;
                padding: 20px;
                border-top: 2px solid #ddd;
            }}
            a {{
                color: #0046be;
                text-decoration: none;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">📢 Fox News Update 📢</div>
            <div class="content">
                <p class="subheading">📢 Today's Top Stories</p>
                <p>{body}</p>
            </div>
            <div class="footer">
                <p>&copy; 2025 NewsBot | <a href="#">Unsubscribe</a></p>
            </div>
        </div>
    </body>
    </html>
    """

    msg.attach(MIMEText(html_content, "html"))
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECIPIENT, msg.as_string())

if __name__ == "__main__":
    send_email("Daily Fox News Update", "Here are the top stories of the day from Fox News.")