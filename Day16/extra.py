
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

API_KEY = "your_api_key_here"
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

base_currency = "USD"
target_currency = "EUR"
amount = 100


url = BASE_URL + base_currency
response = requests.get(url)
data = response.json()

if response.status_code == 200 and data["result"] == "success":
    rate = data["conversion_rates"][target_currency]
    converted_amount = amount * rate
    result = f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}"
else:
    result = "Error fetching currency data!"

print(result)


sender = "your_email@gmail.com"
receiver = "receiver_email@gmail.com"
password = "your_app_password_here"

msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = "Currency Conversion Result"
msg.attach(MIMEText(result, "plain"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)
    server.quit()
    print("✅ Email sent with conversion result!")
except Exception as e:
    print("❌ Email failed:", e)
