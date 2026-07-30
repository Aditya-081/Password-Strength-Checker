import re

def check_password(password):
    score = 0
    suggestions = []

    # Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Number
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number.")

    # Special Character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
    else:
        suggestions.append("Add at least one special character.")

    # Rating
    if score <= 2:
        rating = "Weak"
    elif score <= 4:
        rating = "Medium"
    elif score <= 6:
        rating = "Strong"
    else:
        rating = "Very Strong"

    return rating, score, suggestions


def main():
    print("=" * 50)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 50)

    password = input("Enter your password: ")

    rating, score, suggestions = check_password(password)

    print("\nResult")
    print("-" * 50)
    print(f"Strength : {rating}")
    print(f"Score    : {score}/7")

    if suggestions:
        print("\nSuggestions:")
        for item in suggestions:
            print(f"- {item}")
    else:
        print("\nExcellent! Your password follows good security practices.")


if __name__ == "__main__":
    main()