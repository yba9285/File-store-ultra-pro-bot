import os
from dotenv import load_dotenv

load_dotenv()

# ==========================================================
# 🔹 TELEGRAM BOT CONFIGURATION
# ==========================================================

API_ID = int(os.getenv("API_ID", ))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN" "")
OWNER_ID = int(os.getenv("OWNER_ID", ))

OWNER_USERNAME = os.getenv("OWNER_USERNAME", "sammarathi")

# ==========================================================
# 🔹 DATABASE CONFIGURATION
# ==========================================================

MONGO_URI = os.getenv("MONGO_URI", "")
DATABASE_NAME = os.getenv("DATABASE_NAME", "file_store_bot")

DB_CHANNEL = int(os.getenv("DB_CHANNEL", -1002121119805))

# ==========================================================
# 🔹 DOMAIN & ROUTES
# ==========================================================
WEB_URL = os.getenv(
    "WEB_URL",
    "https://file-store-ultra-pro-bot-25cg.onrender.com"
)
DOMAIN = os.getenv(
    "DOMAIN",
    "https://file-store-ultra-pro-bot-25cg.onrender.com"
)

ADMIN_PANEL_PATH = os.getenv("ADMIN_PANEL_PATH", "/admin")
STREAM_PATH = os.getenv("STREAM_PATH", "/stream")

ADMIN_PANEL_URL = f"{DOMAIN}{ADMIN_PANEL_PATH}"
STREAM_BASE_URL = f"{DOMAIN}{STREAM_PATH}"


# ==========================================================
# 🔹 START MESSAGE CONFIGURATION
# ==========================================================

# Must be direct public HTTPS image URL
START_PHOTO = os.getenv(
    "START_PHOTO",
    "https://graph.org/file/cc28bdd52a4d3f4075721-34c483a7b7d2187e79.jpg"
)

START_CAPTION = os.getenv(
    "START_CAPTION",
    "Welcome {first} to Ultra File Store Pro 🚀"
)


# ==========================================================
# 🔹 WEB PANEL CONFIGURATION
# ==========================================================

SECRET_KEY = os.getenv("SECRET_KEY", "H44PBHTWWP4LS0N5")
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "H44PBHTWWP4LS0N5")
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "H44PBHTWWP4LS0N5")


# ==========================================================
# 🔹 LOGGING CONFIGURATION
# ==========================================================

LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID", ))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")


# ==========================================================
# 🔹 SERVER CONFIGURATION
# ==========================================================

HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))
DEBUG = os.getenv("DEBUG", "False") == "True"
WORKERS = int(os.getenv("WORKERS", 2))


# ==========================================================
# 🔹 CONFIG VALIDATION
# ==========================================================

def validate_config():
    required = {
        "API_ID": API_ID,
        "API_HASH": API_HASH,
        "BOT_TOKEN": BOT_TOKEN,
        "OWNER_ID": OWNER_ID,
        "MONGO_URI": MONGO_URI,
        "DOMAIN": DOMAIN,
        "SECRET_KEY": SECRET_KEY,
        "FLASK_SECRET_KEY": FLASK_SECRET_KEY,
        "ADMIN_PASSWORD": ADMIN_PASSWORD,
        "LOG_CHANNEL_ID": LOG_CHANNEL_ID,
    }

    missing = [k for k, v in required.items() if not v]

    if missing:
        raise ValueError(
            f"Missing required configuration values: {', '.join(missing)}"
)
