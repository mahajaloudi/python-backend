
import re
from datetime import datetime, timedelta
import pytz



def validate_email(email):
    """
    Validate an email address.
    Pattern:
    - username: letters, numbers, dots, underscores, hyphens
    - domain: letters, numbers, hyphens
    - extension: 2-4 letters
    """
    pattern = r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}$'
    return bool(re.match(pattern, email))



def extract_dates(text):
    """
    Extract dates in DD-MM-YYYY or DD/MM/YYYY format.
    """
    pattern = r'\b\d{2}[-/]\d{2}[-/]\d{4}\b'
    return re.findall(pattern, text)



def time_until_birthday(birthdate_str):
    """
    Calculate days, hours, minutes until the next birthday.
    User input format: YYYY-MM-DD
    """
    today = datetime.now()
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

   
    next_birthday = datetime(today.year, birthdate.month, birthdate.day)

   
    if next_birthday < today:
        next_birthday = datetime(today.year + 1, birthdate.month, birthdate.day)

    delta = next_birthday - today
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, _ = divmod(remainder, 60)

    return days, hours, minutes



def convert_timezone(time_str, from_tz, to_tz):
    """
    Convert a time string from one timezone to another.
    Example time_str: "2023-10-05 14:30:00"
    """
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)

   
    naive_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")

  
    from_time = from_zone.localize(naive_time)

  
    to_time = from_time.astimezone(to_zone)

    return to_time.strftime("%Y-%m-%d %H:%M:%S")



def parse_log_timestamps(log):
    """
    Extract timestamps from log format:
    [DD/Mon/YYYY:HH:MM:SS +0000]
    Convert to: YYYY-MM-DD HH:MM:SS (UTC)
    """
    pattern = r'\[(\d{2})/([A-Za-z]{3})/(\d{4}):(\d{2}):(\d{2}):(\d{2}) \+0000\]'
    matches = re.findall(pattern, log)

    month_map = {
        "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
        "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
        "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
    }

    results = []
    for day, mon, year, hour, minute, sec in matches:
        dt = datetime(
            int(year), month_map[mon], int(day),
            int(hour), int(minute), int(sec), tzinfo=pytz.utc
        )
        results.append(dt.strftime("%Y-%m-%d %H:%M:%S"))
    return results



if __name__ == "__main__":
    print("=== Exercise 1: Email Validation ===")
    print(validate_email("user.name-1@example.com"))  
    print(validate_email("wrong_email@com")) 

    print("\n=== Exercise 2: Extract Dates ===")
    text = "Meeting on 21-08-2025 and another on 05/09/2025."
    print(extract_dates(text))

    print("\n=== Exercise 3: Time Until Next Birthday ===")
    birthdate_input = "2000-12-25"  
    days, hours, minutes = time_until_birthday(birthdate_input)
    print(f"Time until next birthday: {days} days, {hours} hours, {minutes} minutes")

    print("\n=== Exercise 4: Timezone Converter ===")
    time_str = "2025-08-21 14:30:00"
    print("US/Eastern -> UTC:", convert_timezone(time_str, "US/Eastern", "UTC"))
    print("Asia/Amman -> Asia/Tokyo:", convert_timezone(time_str, "Asia/Amman", "Asia/Tokyo"))

    print("\n=== Exercise 5: Log Timestamp Extraction ===")
    log_data = """
    192.168.0.1 - - [21/Aug/2025:13:45:30 +0000] "GET /index.html HTTP/1.1" 200 1024
    192.168.0.2 - - [22/Aug/2025:14:55:40 +0000] "POST /login HTTP/1.1" 302 2048
    """
    print(parse_log_timestamps(log_data))
