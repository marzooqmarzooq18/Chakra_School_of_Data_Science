import datetime

# Base exception class
class AppError(Exception):
    """Base class for all custom exceptions."""
    pass

# Derived custom exceptions
class ValidationError(AppError):
    pass

class DatabaseError(AppError):
    pass

class NetworkError(AppError):
    pass


# Logger class to record errors
class ErrorLogger:
    def __init__(self, logfile="errors.log"):
        self.logfile = logfile

    def log(self, error: Exception):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"[{timestamp}] {type(error).__name__}: {error}\n"
        with open(self.logfile, "a") as f:
            f.write(entry)
        print(f"{type(error).__name__} logged successfully.")


# Demonstration of usage
if __name__ == "__main__":
    logger = ErrorLogger()

    # Example 1: Validation Error
    try:
        raise ValidationError("Invalid input: empty email field")
    except AppError as e:
        logger.log(e)

    # Example 2: Database Error
    try:
        raise DatabaseError("Failed to connect to the database server")
    except AppError as e:
        logger.log(e)

    # Example 3: Network Error
    try:
        raise NetworkError("Connection timed out while reaching api.server.com")
    except AppError as e:
        logger.log(e)

    print("All custom errors logged successfully.")
