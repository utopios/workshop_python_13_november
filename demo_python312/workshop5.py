from typing import TypedDict, Unpack, override
from datetime import datetime


# Step 1: Define TypedDict for Configurations and Orders
class ReportConfig(TypedDict, total=False):
    """
    Defines the structure of the report configurations.
    """
    Customer: str
    Shipping: str
    Discount: float


class Order(TypedDict):
    """
    Defines the structure of order data.
    """
    OrderID: int
    ProductID: int
    Quantity: int
    Price: float


# Step 2: Advanced String Formatting (Python 3.12)
def generate_report(monthly_revenue: dict[str, float]) -> None:
    """
    Generate a formatted report for monthly revenues using advanced string formatting.
    """
    template = "Month: {month}, Revenue: ${revenue:.2f}"
    report = "\n".join(
        template.format(month=month, revenue=revenue) for month, revenue in monthly_revenue.items()
    )
    print(f"\nSales Report:\n{report}")

    # Example of variable braces
    fields = ["Month", "Revenue"]
    dynamic_template = "{field}: {{value}}"  # Double braces for dynamic substitution
    for field in fields:
        print(dynamic_template.format(field=field).format(value="Placeholder"))


# Step 3: Method Overrides and Type Consistency (Python 3.12)
class DataProcessor:

    ### ... old code
    """
    Base class for processing data.
    """
    def filter_by_date(self, start_date: datetime, end_date: datetime) -> None:
        """
        Base method to filter rows within a date range.
        """
        pass  # Placeholder for implementation


class CustomProcessor(DataProcessor):
    """
    Derived class with an overridden method.
    """
    @override
    def filter_by_date(self, start_date: datetime, end_date: datetime) -> None:
        """
        Override filter_by_date to include additional processing.
        """
        print(f"Filtering data between {start_date} and {end_date}")


# Step 4: Generate Sales Report with TypedDict and Unpack
def generate_sales_report(order: Order, **config: Unpack[ReportConfig]) -> dict:
    """
    Generate a sales report by merging order details and configurations using Unpack.
    """
    report = {
        "OrderID": order["OrderID"],
        "ProductID": order["ProductID"],
        "Customer": config.get("Customer", "Default Customer"),
        "Quantity": order["Quantity"],
        "Price": order["Price"],
        "Discount": config.get("Discount", 0.0),
        "Shipping": config.get("Shipping", "Standard"),
        "TotalPrice": order["Quantity"] * order["Price"] * (1 - config.get("Discount", 0.0)),
    }
    return report


# Step 1: Example Monthly Revenue Report
monthly_revenue = {"2024-01": 1000.0, "2024-02": 1500.0, "2024-03": 2000.0}
generate_report(monthly_revenue)

# Step 2: Use CustomProcessor with @override
processor = CustomProcessor()
processor.filter_by_date(datetime(2024, 1, 1), datetime(2024, 3, 31))

# Step 3: Generate Sales Report with TypedDict and Unpack
base_config: ReportConfig = {"Customer": "Alice Johnson", "Shipping": "Express", "Discount": 0.1}
order: Order = {"OrderID": 1, "ProductID": 101, "Quantity": 3, "Price": 50.0}
sales_report = generate_sales_report(order, **base_config)

print("\nGenerated Sales Report:")
print(sales_report)
    