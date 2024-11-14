# Step 1: Define User Roles with Structured Pattern Matching

def validate_user_access(user_profile: dict | None) -> str:
    """
    Validates user access based on their role and subscription status.
    Returns an access message depending on the user profile structure.
    """
    if user_profile is None:
        return "Error: Missing profile data."
    
    match user_profile:
        case {"role": "admin", "name": str(name)}:
            return f"Access granted to all resources for Admin {name}."
        case {"role": "member", "name": str(name), "subscription_status": True}:
            return f"Access granted to member resources for {name}."
        case {"role": "member", "name": str(name), "subscription_status": False}:
            return f"Limited access: {name}, please renew your subscription."
        case {"role": "guest", "name": str(name)}:
            return f"View-only access granted for Guest {name}."
        case _:
            return "Access denied: unknown role"