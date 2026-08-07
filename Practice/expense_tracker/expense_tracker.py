DATA_FILE = "expenses.txt"

def load_expenses():
    expenses = []

    try:
        file = open(DATA_FILE, "r")
        lines = file.readlines()
        file.close()

        for line in lines:
            line = line.strip()
            if not line:
                continue

            parts = line.split("|")
            if len(parts) == 4:
                expenses.append(
                    {
                        "date": parts[0],
                        "category": parts[1],
                        "amount": float(parts[2]),
                        "description": parts[3]
                    }
                )
    except FileNotFoundError:
        pass
    except Exception:
        print("Error Loading Expenses")

    return expenses  # Fixed: Un-indented outside of except block

def save_expenses(expenses):
    try:
        file = open(DATA_FILE, "w")
        for item in expenses:
            # Fixed: Added \n at the end so each expense gets its own line
            record = f"{item['date']}|{item['category']}|{item['amount']}|{item['description']}\n"
            file.write(record)
        file.close()
        print("Expenses Saved Successfully")
    except Exception:
        print("Error Saving Expenses")

def get_valid_amount():
    while True:
        raw_input = input("Enter amount: ").strip()
        parts = raw_input.split(".")
        is_valid = False

        if len(parts) == 1 and parts[0].isdigit():
            is_valid = True
        elif len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            is_valid = True

        if is_valid:
            amount = float(raw_input)
            if amount > 0:
                return amount
            print("Amount must be greater than 0")
        else:
            print("Invalid amount. Please enter a valid number.")

def get_valid_category():
    categories = ["Food", "Transport", "Bills", "Entertainment", "Other"]
    print("\nSelect a category: ")

    idx = 1
    for cat in categories:
        print(f" {idx}. {cat}")
        idx += 1

    while True:
        choice_raw = input("Enter Category number: ").strip()
        if choice_raw.isdigit():
            choice = int(choice_raw)
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
        print("Invalid choice. Please select a valid category number.")

def add_expenses(expenses):
    print("\n-----------Add New Expense------------")

    amount = get_valid_amount()
    category = get_valid_category()

    date_str = input("Enter date (YYYY-MM-DD): ").strip()
    if not date_str:
        date_str = "N/A"
    
    description = input("Enter description: ").strip()
    if not description:
        description = "N/A"

    expense = {
        "date": date_str,
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    save_expenses(expenses)

def view_expenses(expenses):
    print("\n-----------View Expenses------------")
    if not expenses:
        print("No expenses recorded.")
        return

    print(f"{'#':<4} | {'Date':<12} | {'Category':<13} | {'Amount':<9} | {'Description'}")
    print("-" * 60)

    count = 1
    for item in expenses:
        amt_str = f"${item['amount']:.2f}"
        # Fixed: Used amt_str directly instead of item[amt_str]
        print(f"{count:<4} | {item['date']:<12} | {item['category']:<13} | {amt_str:<9} | {item['description']}")
        count += 1

def view_summary(expenses):
    print("\n-----------Expense Summary------------")
    if not expenses:
        print("No expenses recorded.")
        return

    category_totals = {}
    total_spent = 0.0

    for item in expenses:
        cat = item['category']
        amt = item['amount']

        if cat in category_totals:
            category_totals[cat] += amt
        else:
            category_totals[cat] = amt

        total_spent += amt
    
    for cat in category_totals:
        amt = category_totals[cat]
        percentage = (amt / total_spent) * 100 if total_spent > 0 else 0
        print(f"• {cat:<13}: ${amt:8.2f} ({percentage:5.1f}%)")

    print("-" * 35)
    print(f"{'Total':<13}: ${total_spent:8.2f}")

def main():
    expenses = load_expenses()  # Fixed: Load saved data into RAM first

    while True:  # Fixed: Added while True loop to keep program alive
        print("\n====================================")
        print("     PERSONAL EXPENSE TRACKER       ")   
        print("====================================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Category Summary")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_summary(expenses)
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break  # Fixed: Gracefully exit the while loop
        else:
            print("Invalid choice. Please select a valid option.")

# Fixed: Un-indented outside of main()
if __name__ == "__main__":
    main()