
import os


def exercise1_palindrome_checker():
    try:
        with open("input_words.txt", "r", encoding="utf-8") as infile:
            words = infile.read().splitlines()

        palindromes = [word.upper() for word in words if word.lower() == word.lower()[::-1]]

        with open("palindromes.txt", "w", encoding="utf-8") as outfile:
            outfile.write("\n".join(palindromes))

        print("✅ Palindromes written to 'palindromes.txt'.")

    except FileNotFoundError:
        print("❌ 'input_words.txt' not found.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")



def exercise2_temperature_converter():
    try:
        with open("celsius.txt", "r", encoding="utf-8") as infile:
            lines = infile.read().splitlines()

        results = []
        for line in lines:
            try:
                celsius = float(line.strip())
                fahrenheit = (celsius * 9 / 5) + 32
                results.append(f"{celsius:.2f}C = {fahrenheit:.2f}F")
            except ValueError:
                print(f"⚠️ Skipping invalid temperature: {line}")

        with open("fahrenheit.txt", "w", encoding="utf-8") as outfile:
            outfile.write("\n".join(results))

        print("✅ Converted temperatures written to 'fahrenheit.txt'.")

    except FileNotFoundError:
        print("❌ 'celsius.txt' not found.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")



class InvalidLengthError(Exception):
    pass

class InvalidCharacterError(Exception):
    pass

def exercise3_user_registration():
    try:
        username = input("Enter a username: ").strip()

        if not (5 <= len(username) <= 15):
            raise InvalidLengthError("Username must be 5–15 characters long.")
        if not username.isalnum():
            raise InvalidCharacterError("Username must be alphanumeric.")

        with open("users.txt", "a", encoding="utf-8") as file:
            file.write(username + "\n")

        print("✅ User registered successfully.")

    except InvalidLengthError as e:
        print(f"❌ {e}")
    except InvalidCharacterError as e:
        print(f"❌ {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
    finally:
        print("📌 Registration attempt complete.")



def exercise4_log_analyzer():
    try:
        with open("server.log", "r", encoding="utf-8") as logfile:
            lines = logfile.read().splitlines()

        status_counts = {200: 0, 404: 0, 500: 0}

        for line in lines:
            parts = line.split()
            if len(parts) >= 2:
                try:
                    status = int(parts[1])
                    if status in status_counts:
                        status_counts[status] += 1
                except ValueError:
                    continue

        with open("report.txt", "w", encoding="utf-8") as report:
            report.write(f"Successful (200): {status_counts[200]}\n")
            report.write(f"Not Found (404): {status_counts[404]}\n")
            report.write(f"Server Error (500): {status_counts[500]}\n")

        print("✅ Report written to 'report.txt'.")

    except FileNotFoundError:
        print("❌ 'server.log' not found.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")



def exercise5_password_checker():
    special_chars = "!@#$%^&*"

    def is_strong(password):
        return (
            len(password) >= 8 and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in special_chars for c in password)
        )

    try:
        with open("passwords.txt", "r", encoding="utf-8") as infile:
            passwords = infile.read().splitlines()

        strong_passwords = []
        for pwd in passwords:
            if is_strong(pwd):
                strong_passwords.append(pwd)
            else:
                print(f"⚠️ Weak password skipped: {pwd}")

        with open("strong_passwords.txt", "w", encoding="utf-8") as outfile:
            outfile.write("\n".join(strong_passwords))

        print("✅ Strong passwords written to 'strong_passwords.txt'.")

    except FileNotFoundError:
        print("❌ 'passwords.txt' not found.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")



if __name__ == "__main__":
    print("\nDay 6 Python Exercises")
    print("1 - Palindrome Checker")
    print("2 - Temperature Converter")
    print("3 - User Registration")
    print("4 - Log File Analyzer")
    print("5 - Password Strength Checker")

    choice = input("Choose exercise (1-5): ").strip()
    if choice == "1":
        exercise1_palindrome_checker()
    elif choice == "2":
        exercise2_temperature_converter()
    elif choice == "3":
        exercise3_user_registration()
    elif choice == "4":
        exercise4_log_analyzer()
    elif choice == "5":
        exercise5_password_checker()
    else:
        print("❌ Invalid choice.")
