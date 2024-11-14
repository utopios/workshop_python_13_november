import csv
from datetime import datetime
import asyncio
# Step 1: Data Loading and Validation with add_note()
def load_and_validate_data(file_path):
    """
    Load and validate rows from the given CSV file.
    """
    valid_rows = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for line_number, row in enumerate(reader, start=1):
            try:
                # Check for required fields
                if not all(key in row for key in ["OrderID", "OrderDate", "Quantity", "Price"]):
                    raise KeyError("Missing required fields")

                # Validate data types and values
                row["OrderDate"] = datetime.strptime(row["OrderDate"], "%Y-%m-%d")
                row["Quantity"] = int(row["Quantity"])
                row["Price"] = float(row["Price"])
                if row["Quantity"] < 0 or row["Price"] < 0:
                    raise ValueError("Negative values are not allowed")

                valid_rows.append(row)
            except Exception as e:
                e.add_note(f"Error in row {line_number}: {row}")
                raise
    return valid_rows


# Step 2: Asynchronous Revenue Calculation with ExceptionGroup
async def calculate_chunk_revenue(chunk):
    """
    Calculate revenue for a single chunk of data.
    """
    if any(row["Quantity"] < 0 for row in chunk):
        raise ValueError("Negative values in chunk")
    return sum(row["Quantity"] * row["Price"] for row in chunk)

async def calculate_total_revenue(data):
    """
    Calculate the total revenue for the dataset asynchronously.
    """
    chunk_size = 5
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    total_revenue = 0

    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(calculate_chunk_revenue(chunk)) for chunk in chunks]
        results = await asyncio.gather(*tasks, return_exceptions=True)

    errors = [result for result in results if isinstance(result, Exception)]
    if errors:
        raise ExceptionGroup("Errors occurred during chunk processing", errors)

    return sum(result for result in results if not isinstance(result, Exception))


# Step 1: Load and validate data
# file_path = "sales_data.csv"
# data = load_and_validate_data(file_path)
# print(f"Loaded {len(data)} valid rows.")

try:
    # Step 1: Load and validate data
    file_path = "sales_data.csv"
    data = load_and_validate_data(file_path)
    print(f"Loaded {len(data)} valid rows.")

    # Step 2: Calculate total revenue asynchronously
    total_revenue = asyncio.run(calculate_total_revenue(data))
    print(f"Total Revenue: ${total_revenue:.2f}")

except Exception as e:
    print(f"Unhandled exception : {e.__notes__}")
except ExceptionGroup as eg:
    print("Errors occured during processing : ")
    for exc in eg.exceptions:
        print(exc)
    