# New in Python 3.9: Union (|) and Update (|=) Operators for Dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# Before Python 3.9, combining dictionaries required the `update()` method
dict_combined_before = dict1.copy()  # Copy to avoid modifying dict1
dict_combined_before.update(dict2)
print("Before Python 3.9, combined dict:", dict_combined_before)

# In Python 3.9, we can use `|` operator to combine dictionaries directly
dict_combined_39 = dict1 | dict2
print("In Python 3.9, combined dict with `|`:", dict_combined_39)

# Updating a dictionary with another dictionary using `|=`
dict1 |= dict2
print("In Python 3.9, updated dict1 with `|=`:", dict1)

# New String Methods: removeprefix() and removesuffix()
string = "HelloWorld"

# Before Python 3.9, we had to check prefixes/suffixes manually
if string.startswith("Hello"):
    string_without_prefix = string[len("Hello"):]
print("Before Python 3.9, removed prefix manually:", string_without_prefix)

# In Python 3.9, we can directly use `removeprefix()` and `removesuffix()`
string_without_prefix = string.removeprefix("Hello")
print("In Python 3.9, removed prefix with removeprefix:", string_without_prefix)

string_without_suffix = string.removesuffix("World")
print("In Python 3.9, removed suffix with removesuffix:", string_without_suffix)

def process_data(data: list[int]) -> dict[str, int]:
    return {'sum': sum(data)}

print("Using type hints with built-in collections:", process_data([1, 2, 3]))



from typing import Annotated, get_type_hints


def positive_number(number: Annotated[int, "positive"]) -> None:
    print(f"Positive number: {number}")


positive_number(10)
positive_number("test")
positive_number(-10)

# try:
#     validate_positive_number(positive_number, -10) 
# except ValueError as e:
#     print(e)

from datetime import datetime
from zoneinfo import ZoneInfo

import math
paris_time = datetime.now(ZoneInfo('Europe/Paris'))
print("Current time in Paris:", paris_time)

next_value = math.nextafter(1.0, 5.0)
print("Next floating-point number after 1.0:", next_value)

from statistics import multimode

data = [1, 2, 2, 3, 3,3,3, 4, 4, 4]
modes = multimode(data)
print("Modes in data", modes)


filenames = ["file1", "file2", "file3"]

from contextlib import ExitStack

# with [open(filename) for filename in filenames] as files:
#     pass

with ExitStack() as stack:
    files = [stack.enter_context(open(filename) for filename in filenames)]
    