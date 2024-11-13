import math
import statistics
import asyncio
# Step 1: Precise Adjustment of Session Duration

def adjust_session_timeout(config: dict, target: float) -> dict:
    """
    Adjusts the session timeout incrementally toward a target value.
    """
    config["session_timeout"] = math.nextafter(config["session_timeout"], target)
    return config

def get_session_timeout_ulp(timeout: float) -> float:
    """
    Returns the Unit in the Last Place (ULP) for the session timeout.
    """
    return math.ulp(timeout)

# Example usage for Step 1
session_config = {
    "theme": "dark",
    "notifications": True,
    "timezone": "America/New_York",
    "session_timeout": 15.0
}

print("Initial session timeout:", session_config["session_timeout"])
session_config = adjust_session_timeout(session_config, session_config["session_timeout"]-1)
print("Adjusted session timeout:", session_config["session_timeout"])
print("ULP of session timeout:", get_session_timeout_ulp(session_config["session_timeout"]))

# Step 2: Analyzing the Most Common Session Durations

def find_common_session_durations(durations: list) -> list:
    """
    Identifies the most common session durations from the provided data.
    """
    return statistics.multimode(durations)

# Example usage for Step 2
session_durations = [15, 30, 30, 45, 15, 15, 60, 60, 60, 60, 15]
print("Common session durations:", find_common_session_durations(session_durations))

# Step 3: Asynchronous Archiving of Session Reports
def archive_report(filename: str, content: str):
    """
    Writes the session report content to a specified file.
    """
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Archived report: {filename}")

async def async_archive_reports(reports: dict):
    tasks = [asyncio.to_thread(archive_report, filename, content) for filename, content in reports.items()]
    await asyncio.gather(*tasks)


# Example usage for Step 3
reports_to_archive = {
    "session_report_2024-11-01.json": '{"session_timeout": 15, "timezone": "America/New_York"}',
    "session_report_2024-11-02.json": '{"session_timeout": 30, "timezone": "America/New_York"}'
}

asyncio.run(async_archive_reports(reports_to_archive))