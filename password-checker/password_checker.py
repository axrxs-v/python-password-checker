import re

def check_password_strength(password: str) -> dict:
    """Return password strength analysis as a dictionary."""

    result = {
        "length_ok": False,
        "has_upper": False,
        "has_lower": False,
        "has_digit": False,
        "has_symbol": False,
        "not_common": False,
        "no_sequences": False,
        "no_repeats": False,
        "score": 0,
        "rating": "",
        "suggestions": []
    }

    # 1. Length check
    if len(password) >= 12:
        result["length_ok"] = True
        result["score"] += 1
    else:
        result["suggestions"].append("Use at least 12 characters")

    # 2. Uppercase
    if re.search(r"[A-Z]", password):
        result["has_upper"] = True
        result["score"] += 1
    else:
        result["suggestions"].append("Add uppercase letters")

    # 3. Lowercase
    if re.search(r"[a-z]", password):
        result["has_lower"] = True
        result["score"] += 1
    else:
        result["suggestions"].append("Add lowercase letters")

    # 4. Digit
    if re.search(r"[0-9]", password):
        result["has_digit"] = True
        result["score"] += 1
    else:
        result["suggestions"].append("Add digits")

    # 5. Symbol
    if re.search(r"[^A-Za-z0-9]", password):
        result["has_symbol"] = True
        result["score"] += 1
    else:
        result["suggestions"].append("Add special characters")

    # 6. Common passwords check
    common = ["password", "123456", "qwerty", "admin", "letmein"]
    if password.lower() not in common:
        result["not_common"] = True
        result["score"] += 1
    else:
        result["suggestions"].append("Avoid common passwords")

    # 7. Sequence check
    sequences = ["123", "abc", "qwe"]
    if not any(seq in password.lower() for seq in sequences):
        result["no_sequences"] = True
        result["score"] += 1
    else:
        result["suggestions"].append("Avoid sequences like 123 or abc")

    # 8. Repeated characters
    if not re.search(r"(.)\1\1", password):
        result["no_repeats"] = True
        result["score"] += 1
    else:
        result["suggestions"].append("Avoid repeating characters")

    # Final rating
    if result["score"] >= 7:
        result["rating"] = "Strong"
    elif result["score"] >= 4:
        result["rating"] = "Medium"
    else:
        result["rating"] = "Weak"

    return result

if __name__ == "__main__":
    pwd = input("Enter password: ")
    analysis = check_password_strength(pwd)
    print(analysis)
