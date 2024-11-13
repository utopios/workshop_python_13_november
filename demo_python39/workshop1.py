from zoneinfo import ZoneInfo
from datetime import datetime
# Step 1: Creating the Session Configuration

def create_session_config(config_default: dict, config_user: dict) -> dict:
    """
    Merges default settings with user preferences.
    User preferences take precedence in case of conflicts.
    """
    session_config = config_default | config_user
    return session_config

# Default configuration and user preferences
config_default = {
    "theme": "light",
    "notifications": True,
    "timezone": "UTC",
    "session_timeout": 15
}

config_user = {
    "theme": "dark",
    "timezone": "America/New_York",
    "session_timeout": 30
}

# Creating the complete session configuration
session_config = create_session_config(config_default, config_user)
print("Complete session configuration:", session_config)


# Step 2: Generating and Structuring a Session Report Filename
def generate_session_report_filename(session_config: dict) -> str:
    """
    Generates a structured filename for the session report based on the current date and the user's timezone.
    """
    user_timezone = session_config["timezone"]
    current_date = datetime.now(ZoneInfo(user_timezone)).strftime("%Y-%m-%d")
    filename = f"session_report_{current_date}_{user_timezone.replace('/', '_')}.json"
    return filename

print(generate_session_report_filename(session_config=session_config))

# Step 3: Displaying Last Login Time Based on Timezone
def display_last_login(last_login_utc: datetime, timezone: str) -> str:
    """
    Converts the last login time in UTC to the user's timezone and returns a formatted string.
    """
    last_login_user_tz = last_login_utc.astimezone(ZoneInfo(timezone))
    return last_login_user_tz.strftime("%Y-%m-%d %H:%M:%S")

# Example of the last login time in UTC
# last_login_utc = datetime(2024, 11, 1, 14, 30, tzinfo=ZoneInfo("UTC"))
last_login_utc = datetime.now(ZoneInfo('UTC'))
print(display_last_login(last_login_utc=last_login_utc, timezone="America/New_York"))