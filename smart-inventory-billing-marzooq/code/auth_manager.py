import csv
import os
from getpass import getpass
from code.logger import log_info, log_error

USERS_FILE = "data/users.csv"
os.makedirs("data", exist_ok=True)


class AuthManager:
    """Handles user registration and login."""

    def __init__(self):
        # Create the users.csv file if not exists
        if not os.path.exists(USERS_FILE):
            with open(USERS_FILE, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["username", "password"])

    def register_user(self):
        """Register a new user."""
        print("\n--- User Registration ---")
        username = input("Enter username: ").strip()

        # Prevent empty usernames
        if not username:
            print("Username cannot be empty.")
            return

        # Check if username exists
        with open(USERS_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["username"] == username:
                    print("Username already exists. Try another.")
                    return

        password = input("Enter password (visible): ").strip()

        if not password:
            print("Password cannot be empty.")
            return

        # Save the new user
        with open(USERS_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([username, password])

        log_info(f"New user registered: {username}")
        print("Registration successful! You can now log in.")

    def login_user(self):
        """Authenticate user login."""
        print("\n--- User Login ---")
        username = input("Enter username: ").strip()
        password = input("Enter password (visible): ").strip()


        with open(USERS_FILE, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["username"] == username and row["password"] == password:
                    log_info(f"User logged in: {username}")
                    print(f"Welcome, {username}!")
                    return True

        log_error(f"Failed login attempt for {username}")
        print("Invalid username or password.")
        return False
