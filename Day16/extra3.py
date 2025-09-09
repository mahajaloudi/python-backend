
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


WEATHER_KEY = "your_weather_api_key"
CITY = "Amman"
WEATHER_URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={WEATHER_KEY}&units=metric"

NEWS_KEY = "your_news_api_key"
NEWS_URL = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_KEY}"

FACT_URL = "https://uselessfacts.jsph.pl/random.json?language=en"

weather_data = requests.get(WEATHER_URL).json()
weather = f"{weather_data['main']['temp']}°C, {weather_data['weather'][0]['description']}"


news_data = requests.get(NEWS_URL).json()
news_headlines = "".join([f"<li>{a['title']}</li>" for a in news_data["articles"][:3]])


fact_data = requests.get(FACT_URL).json()
fun_fact = fact_data["text"]


newsletter = f"""
<html>
<body>
<h2>🌦 Weather Update</h2>
<p>{CITY}: {weather}</p>

<h2>📰 Top News</h2>
<ul>{news_headlines}</ul>

<h2>🤓 Fun Fact</h2>
<p>{fun_fact}</p>
</body>
</html>
"""


sender = "your_email@gmail.com"
receiver_list = ["subscriber1@gmail.com", "subscriber2@gmail.com"]
password = "your_app_password_here"

msg = MIMEMultipart("alternative")
msg["From"] = sender
msg["To"] = ", ".join(receiver_list)
msg["Subject"] = "Daily Newsletter"

msg.attach(MIMEText(newsletter, "html"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)
    server.quit()
    print("✅ Newsletter sent successfully!")
except Exception as e:
    print("❌ Failed to send newsletter:", e)
