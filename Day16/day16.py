
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


API_KEY = "your_api_key_here"  
CITY = "Amman"  
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()

    
    city = data["name"]
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]

   
    report = f"""
    تقرير الطقس لليوم:
    ---------------------
    المدينة: {city}
    درجة الحرارة: {temp}°C
    الحالة الجوية: {weather}
    """
else:
    report = "حدث خطأ أثناء جلب بيانات الطقس!"

print(report)


sender_email = "your_email@gmail.com"       
receiver_email = "receiver_email@gmail.com" 
password = "your_email_password_or_app_key" 

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "تقرير الطقس اليومي"


msg.attach(MIMEText(report, "plain"))


try:
    server = smtplib.SMTP("smtp.gmail.com", 587)  
    server.starttls()
    server.login(sender_email, password)
    server.send_message(msg)
    server.quit()
    print("تم إرسال البريد الإلكتروني بنجاح ✅")
except Exception as e:
    print("فشل في إرسال البريد:", e)
