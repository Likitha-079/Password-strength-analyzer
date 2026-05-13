import re
import random
import string

common_passwords = ["password", "123456", "qwerty", "abc123"]


# ---------------- PASSWORD ANALYZER ---------------- #

def analyze_password(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short")

    # Complexity checks
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers")

    if re.search(r"[^\w]", password):
        score += 1
    else:
        feedback.append("Add special characters")

    # Common password check
    if password.lower() in common_passwords:
        feedback.append("Avoid common passwords")
        score = 0

    # Strength level
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, feedback


# ---------------- PASSWORD GENERATOR ---------------- #

def generate_strong_password(length=12):

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*"

    # Ensure all character types exist
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill remaining characters
    all_chars = lowercase + uppercase + digits + symbols

    password += random.choices(all_chars, k=length - 4)

    # Shuffle password
    random.shuffle(password)

    return ''.join(password)


# ---------------- MAIN PROGRAM ---------------- #

pwd = input("Enter your password: ")

strength, feedback = analyze_password(pwd)

print("\nPassword Strength:", strength)

if feedback:
    print("\nSuggestions:")
    for item in feedback:
        print("-", item)

# Suggest stronger passwords if weak/moderate
if strength != "Strong":
    print("\nSuggested Strong Passwords:")
    
    for i in range(3):
        print(f"{i+1}.", generate_strong_password())