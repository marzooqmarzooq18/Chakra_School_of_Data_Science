# logger.py
import logging, os

# Ensure logs directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "system.log")

# Configure logger
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_info(message):
    """Log normal informational messages."""
    print(f"[INFO] {message}")
    logging.info(message)

def log_error(message):
    """Log errors with timestamp."""
    print(f"[ERROR] {message}")
    logging.error(message)
