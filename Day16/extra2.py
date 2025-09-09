
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import schedule
import time

NEWS_API_KEY = "your_api_key_here"
NEWS_URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"

def send_news_email():
    response = requests.get(NEWS_URL)
    data = response.json()

    headlines = []
    if response.status_code == 200:
        for article in data["articles"][:5]:  
            headlines.append(f"- {article['title']}")
    else:
        headlines.append("Error fetching news.")

    digest = "Daily News Digest:\n\n" + "\n".join(headlines)

    
    sender = "your_email@gmail.com"
    receiver = "receiver_email@gmail.com"
    password = "your_app_password_here"

    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = "Daily News Digest"
    msg.attach(MIMEText(digest, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.send_message(msg)
        server.quit()
        print("✅ News Digest sent!")
    except Exception as e:
        print("❌ Failed to send news:", e)


schedule.every().day.at("09:00").do(send_news_email)

print("⏳ Waiting for schedule...")
while True:
    schedule.run_pending()
    time.sleep(60)
