def greet_user(name, city="Pondicherry"):
    """Print a personalized greeting message."""
    print(f"Hello {name}! How's life in {city}?")

def main():
    greet_user("Arun")
    greet_user("Meera", "Chennai")

main()