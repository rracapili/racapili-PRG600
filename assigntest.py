import sys
import csv

def display_stock(stock_data):
    """
    Display the current stock in a formatted table.
    """
    print("# Item Current Stock Price per Item")
    print("=" * 40)

    i = 1  # Initialize index counter

    for item in stock_data:
        # Print formatted stock information
        print(f"{i}. {item['Item']} {item['Current Stock']} $ {item['Price per Item']:.2f}")
        
        i += 1  # Increment index counter

def update_stock(item, quantity_sold, lost_sales):
    """
    Update the stock based on the items sold and track lost sales.
    """
    if item['Current Stock'] > 0:
        # Check if there is available stock for the current item
        # If the current stock is greater than 0, decrement the stock by 1 for the sale
        item['Current Stock'] -= 1
    else:
        # If the current stock is 0, indicate a lost sale for the item
        # Increment the count of lost sales for this item in the 'lost_sales' dictionary
        lost_sales[item['Item']] += 1

def generate_reports(stock_data, total_sales, lost_sales):
    """
    Generate and print total sales, lost sales, and restock reports.
    """
    # Print Total Sales Report
    print("\nTotal Sales")
    print("# Item Sales Price per Item Total")
    print("=" * 45)
    grand_total = 0

    # Iterate through each item in stock_data
    for i in range(len(stock_data)):
        item = stock_data[i]
        sales = total_sales[item['Item']]
        total_price = sales * item['Price per Item']
        grand_total += total_price
        print(f"{i + 1}. {item['Item']} {sales} $ {item['Price per Item']:.2f} $ {total_price:.2f}")

    # Print total sales report footer
    print(f"TOTAL $ {grand_total:.2f}")

    # Print Lost Sales Report
    print("\nLost Sales")
    print("# Item Sales Price per Item Total")
    print("=" * 45)
    total_lost_sales = 0

    # Iterate through each item in stock_data
    for i in range(len(stock_data)):
        item = stock_data[i]
        lost_sale_count = lost_sales[item['Item']]
        total_price = lost_sale_count * item['Price per Item']
        total_lost_sales += total_price
        print(f"{item['Item']} {lost_sale_count} $ {item['Price per Item']:.2f} $ {total_price:.2f}")

    # Print lost sales report footer
    print(f"TOTAL $ {total_lost_sales:.2f}")

    # Print Restock Report
    print("\nRestock Report")
    print("# Item Demand 20% Total Demand Current Stock From Warehouse")
    print("=" * 65)

    # Iterate through each item in stock_data
    for i in range(len(stock_data)):
        item = stock_data[i]
        demand = total_sales[item['Item']] + lost_sales[item['Item']]
        demand20 = round(demand * 0.2)
        total_demand = demand + demand20
        from_warehouse = max(0, total_demand - item['Current Stock'])
        print(f"{i + 1}. {item['Item']} {demand} {demand20} {total_demand} {item['Current Stock']} {from_warehouse}")


def export_updated_stock_csv(stock_data, filename):
    """
    Export the updated stock information to a CSV file.
    """
    # Open the CSV file in write mode with newline='' to ensure consistent newline handling
    with open(filename, 'w', newline='') as file:

        # Create a CSV writer object
        writer = csv.writer(file)

        # Write the header row to the CSV file
        writer.writerow(["Item", "Current Stock", "Price per Item"])

        # Iterate through each item in stock_data and write its information to the CSV file
        for item in stock_data:
            # Write a new row with item details
            writer.writerow([item['Item'], item['Current Stock'], item['Price per Item']])

def main():
    """
    Main function to run the stock monitoring script.
    """
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <csv_file>")
        sys.exit(1)

    # Get the CSV file name from the command-line arguments
    csv_file = sys.argv[1]

    # Initialize an empty list to store stock data
    stock_data = []

    # Read stock information from the CSV file and populate stock_data list
    with open(csv_file, 'r') as file:
        # Skip the header row
        next(file)
        # Iterate through each line in the file
        for line in file:
            # Split the CSV line into individual values and create a dictionary for each item
            item, current_stock, price_per_item = line.strip().strip('"').split('","')
            stock_data.append({
                'Item': item.strip('"'),
                'Current Stock': int(current_stock),
                'Price per Item': float(price_per_item)
            })

    # Initialize dictionaries to track total sales and lost sales for each item
    total_sales = {item['Item']: 0 for item in stock_data}
    lost_sales = {item['Item']: 0 for item in stock_data}

    # Main loop to interact with the cashier until 'e' is entered
    while True:
        # Display current stock information
        display_stock(stock_data)

        # Get user input for the sale or end of the day
        action = input("Select a number (1-3) to indicate a sale, or 'e' to indicate end of day: ").lower()

        # Check if the user wants to end the day
        if action == 'e':
            break

        try:
            # Convert the user input to an integer and subtract 1 to get the item index
            item_index = int(action) - 1

            # Check if the item index is within the valid range
            if 0 <= item_index < len(stock_data):
                item = stock_data[item_index]

                # Update stock based on the sale and track sales
                update_stock(item, 1, lost_sales)
                total_sales[item['Item']] += 1
            else:
                print("Invalid input. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Generate and display reports
    generate_reports(stock_data, total_sales, lost_sales)

    # Export updated stock information to a CSV file
    export_updated_stock_csv(stock_data, 'updated_stock.csv')

if __name__ == "__main__":
    main()
