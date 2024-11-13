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