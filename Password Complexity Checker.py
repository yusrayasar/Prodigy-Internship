# Create a file
nano password_checker.py

# Python code
import re
def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("❗ Password should be at least 8 characters long.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("❗ Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("❗ Add uppercase letters.")

    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("❗ Add numbers (0-9).")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("❗ Add special characters (e.g., !, @, #).")

    if strength == 5:
        return "✅ Strong password!", feedback
    elif strength >= 3:
        return "🟡 Moderate password.", feedback
    else:
        return "🔴 Weak password!", feedback


# === User Interaction ===
print("🔐 Password Strength Checker 🔐")
user_password = input("Enter a password to check: ")
strength_msg, tips = check_password_strength(user_password)

print("\nStrength:", strength_msg)
if tips:
    print("Suggestions:")
    for tip in tips:
        print("-", tip)

# Run the program
python3 password_checker.py

