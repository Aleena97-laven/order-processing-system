# Order Processing System

## Introduction
Python program demonstrating exception handling. Processes order data in `Product,Price,Quantity` format and calculates total bill. Invalid inputs handled using custom `InvalidOrderError` exception.

## Procedure
1. Created custom exception `InvalidOrderError` class for invalid order data
2. `calculate_bill(price, qty)` function converts inputs and validates positive values  
3. `process_order(order)` function splits string and checks for 3-part format
4. Used try-except blocks to catch `ValueError` and `InvalidOrderError`
5. Tested with 10 sample orders including invalid cases: "Mobile,abc,1", "Camera,45000", "INVALID"

## Code
Complete code in `order-processing.py` file.

## Output Screens
Screenshots of program execution added below in screenshots folder.



GROUP MEMBERS:
SYEDA ALEENA WAJID-160625748058
SAHERISH MAZHAR-160625748050
ZUREEN ARISHA-160625748065
