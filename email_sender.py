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
    <body style="font-family:Arial; padding:20px;">
        <div style="max-width:600px; margin:auto; border:1px solid #ddd; box-shadow: 2px 2px 10px #ccc;">
            <h2 style="background-color:#0046be; color:white; padding:15px; text-align:center;">Fox News Update</h2>
            <div style="padding:20px;">
                <p>{body}</p>
            </div>
            <footer style="text-align:center; font-size:12px; color:#777; padding:10px;">
                <p>&copy; 2025 NewsBot | <a href="#">Unsubscribe</a></p>
            </footer>
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