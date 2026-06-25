"""
Simple authentication module for demo purposes
"""

def validate_login(username, password):
    """Validate user login credentials"""
    # Improved validation with explicit checks
    if not username or not password:
        return False

    if len(password) < 8:
        return False

    # TODO: Add actual password validation against database
    if username == "admin" and password == "password123":
        return True

    return False


def main():
    print("Authentication Demo")
    result = validate_login("admin", "password")
    print(f"Login result: {result}")


if __name__ == "__main__":
    main()
