class InvalidOrderError(Exception):
    """Custom exception for invalid order format"""
    pass

def calculate_bill(price, qty):
    """Calculate total cost. Raises ValueError if price/qty not integer"""
    try:
        price = int(price)
        qty = int(qty)
        return price * qty
    except ValueError:
        raise InvalidOrderError("Price or Quantity is not a valid number")

def process_order(order):
    """Process a single order string and return result"""
    try:
        parts = order.split(',')
        
        # Check if format is correct: Product,Price,Qty
        if len(parts) != 3:
            raise InvalidOrderError(f"Invalid format. Expected 3 parts, got {len(parts)}")
        
        product, price, qty = parts
        total = calculate_bill(price, qty)
        return f"{product}: Total = ₹{total}"
    
    except InvalidOrderError as e:
        return f"{order} --> Error: {e}"

# Test with given data
orders = [
    "Laptop,55000,2",
    "Mobile,abc,1", 
    "Tablet,20000,3",
    "Camera,45000",
    "Headphones,2000,2",
    "TV,70000,1",
    "Mouse,500,5",
    "Keyboard,1500,2",
    "Charger,800",
    "INVALID"
]

print("=== Order Processing Results ===")
for order in orders:
    print(process_order(order))
