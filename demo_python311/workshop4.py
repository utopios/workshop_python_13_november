import csv
from datetime import datetime
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

# Step 1: Load and validate data
file_path = "sales_data.csv"
data = load_and_validate_data(file_path)
print(f"Loaded {len(data)} valid rows.")

# try:
#     # Step 1: Load and validate data
#     file_path = "sales_data.csv"
#     data = load_and_validate_data(file_path)
#     print(f"Loaded {len(data)} valid rows.")
# except Exception as e:
#     print(f"Unhandled exception : {e}")
# except ExceptionGroup as eg:
#     print("Errors occured during processing : ")
#     for exc in eg.exceptions:
#         print(exc)
    