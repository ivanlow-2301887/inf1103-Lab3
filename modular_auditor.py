def get_valid_input():
    
    user_input = input("Enter stock quantity: ").strip()

    # Check for quit signal
    if user_input.lower() == "quit":
        return "quit"

    # Validate: must be an integer (allow optional leading minus)
    if not user_input.lstrip("-").isdigit():
        print(f"  [ERROR] '{user_input}' is not a valid integer. Entry rejected.\n")
        return -1  # sentinel for rejected entry

    quantity = int(user_input)

    # Business rule: reject negative numbers
    if quantity < 0:
        print(f"  [ERROR] Negative quantity ({quantity}) is not allowed. Entry rejected.\n")
        return -1  # sentinel for rejected entry

    return quantity


def process_delivery(current_total, new_value):
    
    return current_total + new_value


def calculate_tax(amount):
    
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    
    print("\n=== Audit Report ===")
    print(f"Total Units Processed  : {total_units}")
    print(f"Total Deliveries Tax   : {total_units * 0.10:.2f}")
    print(f"Failed/Rejected Entries: {failed_attempts}")


# Entry point
if __name__ == "__main__":
    # 1. Initialize inventory and counters to zero
    total_inventory = 0
    failed_entries = 0
    deliveries_processed = 0
    total_tax = 0.0

    print("=== Smart Inventory Auditor (Modular) ===")
    print("Enter stock quantities as whole numbers.")
    print("Type 'quit' at any time to finish.\n")

    # 2. Continuous loop until 'quit' is typed
    while True:
        result = get_valid_input()

        # Handle quit signal
        if result == "quit":
            break

        # Handle rejected entry (sentinel value)
        if result == -1:
            failed_entries += 1
            continue

        # 3. Valid entry: process delivery
        quantity = result

        # Add delivery to running total
        total_inventory = process_delivery(total_inventory, quantity)

        # Calculate tax for THIS specific delivery
        delivery_tax = calculate_tax(quantity)
        total_tax += delivery_tax

        # Update delivery counter
        deliveries_processed += 1

        print(f"  [OK] Added {quantity}. Running total: {total_inventory}")
        print(f"       Tax on this delivery: {delivery_tax:.2f}")

        # Overstock alert
        if total_inventory > 500:
            print("=" * 45)
            print(f"  [ALERT] Overstock! Total {total_inventory} exceeds 500 units.")
            print("=" * 45)
            break

    # 4. Reporting
    generate_report(total_inventory, failed_entries)
    print(f"Deliveries Processed  : {deliveries_processed}")
    print(f"Total Tax Collected   : {total_tax:.2f}")