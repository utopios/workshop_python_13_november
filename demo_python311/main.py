# 2. Adding Notes to Exceptions with add_note()
import requests

def exception_notes():
    """
    Demonstrates using add_note to attach additional information to an exception.
    """
    try:
        r = requests.get('http://www.google.comx')
    except requests.exceptions.RequestException as e:
        e.add_note("Unable to fetch Google - check URL and connectivity.")
        raise

# exception_notes()


# 3. Exception Groups and `except*` for Multiple Errors
async def fetch_data():
    raise ConnectionError("Failed to connect to server")

async def read_file():
    raise FileNotFoundError("File not found")

async def process_data():
    raise ValueError("Invalid data")

import asyncio

async def main():
    """
    Demonstrates handling multiple exceptions using ExceptionGroup and except* syntax.
    """
    tasks = [fetch_data(), read_file(), process_data()]
    try:
        results = await asyncio.gather(*tasks, return_exceptions=True)
        raise ExceptionGroup("Multiple task errors", [result for result in results if isinstance(result, BaseException)])
    except* ConnectionError as err:
        print(f"Network issue: {err}")
    except* FileNotFoundError as err:
        print(f"File issue: {err}")
    except* ValueError as err:
        print(f"Data processing issue: {err}")

# asyncio.run(main())

# 4. Typing `Self` for Method Annotations
from typing import Self

class Custom2Path:
    def getCustom() -> 'CustomPath':
        pass

class CustomPath:
    def __init__(self, path: str):
        self.path = path

    def concat(self, other: str) -> Self:
        """
        Method returns an instance of CustomPath, annotated with Self for clarity.
        """
        return CustomPath(f'{self.path}/{other}')
    
    def __str__(self):
        return self.path

# Example usage
#p = CustomPath("/home/user")
#print(p.concat("documents"))

# 5. More Precise Error Messages
def example1():
    """
    Example demonstrating improved error message for an out-of-range index.
    """
    d = {"uno": [1, [1, 2, 3], 3]}
    print(d["uno"][5][2])

def example2():
    """
    Example showing Python 3.11’s detailed error message for division by zero.
    """
    a, b, c, d, e, f = 1, 2, 0, 4, 5, 6
    print(a / b / c / d / e / f)

def example3():
    """
    Example highlighting Python 3.11’s clear error message when calling a method on None.
    """
    a = None
    b = ""
    print(a.capitalize() + b.capitalize())

#example1()  # Uncomment to see the improved IndexError
#example2()  # Uncomment to see the detailed ZeroDivisionError
#example3()  # Uncomment to see the error with NoneType

from pathlib import Path

def list_directories():
    """
    Lists only directories within a specified path using pathlib's glob with trailing slash.
    """
    p = Path("/Users/ihababadi/Desktop/workshop-python")  # Replace with an existing directory path

    print("All files and directories:")
    for entry in p.glob("*"):
        if entry.is_file():
            print(entry)

    print("\nOnly directories:")
    for directory in p.glob("*/"):
        print(directory)

#list_directories()

from enum import StrEnum, auto

class Color(StrEnum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    #RED = auto()

print(Color.red)