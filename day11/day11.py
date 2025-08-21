


import re
from datetime import datetime
import pytz


def validate_email(email):
    """Validate an email using regex"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}$'
    if re.match(pattern, email):
        return True
    return False


def extract_numbers(text):
    """Extract numbers from a string"""
    numbers = re.findall(r'\d+', text)
    return numbers


def show_time_in_timezones():
    """Show current time in multiple timezones"""
    utc_now = datetime.now(pytz.utc)

    timezones = ["UTC", "Asia/Amman", "Europe/London", "America/New_York", "Asia/Tokyo"]

    result = {}
    for tz in timezones:
        zone = pytz.timezone(tz)
        result[tz] = utc_now.astimezone(zone).strftime("%Y-%m-%d %H:%M:%S")
    return result



if __name__ == "__main__":
    print("=== Regular Expressions ===")
    test_email = "example.user@test.com"
    print(f"Validating email '{test_email}': {validate_email(test_email)}")

    invalid_email = "user@@wrong..com"
    print(f"Validating email '{invalid_email}': {validate_email(invalid_email)}")

    text = "Order123 contains 45 items, total price is 678 dollars."
    print(f"Extracted numbers from text: {extract_numbers(text)}")

    print("\n=== Date & Time with Timezones ===")
    times = show_time_in_timezones()
    for tz, t in times.items():
        print(f"{tz}: {t}")
