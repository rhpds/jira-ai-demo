"""
Simple authentication module for demo purposes
"""

def check_password_strength(password):
    """Check password strength and return a score"""
    score = 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 1

    return score  # 0-6 score


def validate_login(username, password):
    """Validate user login credentials"""
    # Improved validation with explicit checks
    if not username or not password:
        return False

    # Username must be at least 3 characters
    if len(username) < 3:
        return False

    # Password must be at least 8 characters
    if len(password) < 8:
        return False

    # Password must have minimum strength score of 3
    if check_password_strength(password) < 3:
        return False

    # Username should only contain alphanumeric characters
    if not username.isalnum():
        return False

    # TODO: Add actual password validation against database
    if username == "admin" and password == "password123":
        return True

    return False


def main():
    print("Authentication Demo")

    # Test valid login
    result = validate_login("admin", "password123")
    print(f"Login result for 'admin': {result}")

    # Test invalid short username
    result = validate_login("ab", "password123")
    print(f"Login result for short username: {result}")


if __name__ == "__main__":
    main()
