import csv
import os
from datetime import datetime
from collections import defaultdict

FILE_NAME = "expenses.csv"

FIELDS = [
    "id",
    "amount",
    "category",
    "description",
    "date"
]


# -----------------------------
# Initialize CSV file
# -----------------------------
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()


# -----------------------------
# Load expenses
# -----------------------------
def load_expenses():
    initialize_file()

    expenses = []

    try:
        with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                expenses.append(row)

    except FileNotFoundError:
        print("Expense file not found.")

    return expenses


# -----------------------------
# Save expenses
# -----------------------------
def save_expenses(expenses):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)

        writer.writeheader()
        writer.writerows(expenses)


# -----------------------------
# Generate next ID
# -----------------------------
def generate_id(expenses):
    if not expenses:
        return 1

    ids = []

    for expense in expenses:
        try:
            ids.append(int(expense["id"]))
        except (ValueError, TypeError):
            pass

    return max(ids, default=0) + 1


# -----------------------------
# Validate date
# -----------------------------
def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False


# -----------------------------
# Add expense
# -----------------------------
def add_expense():
    expenses = load_expenses()

    print("\n========== ADD EXPENSE ==========")

    # Amount validation
    while True:
        amount_input = input("Enter amount: ").strip()

        try:
            amount = float(amount_input)

            if amount <= 0:
                print("Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # Category
    while True:
        category = input("Enter category: ").strip()

        if category:
            break

        print("Category cannot be empty.")

    # Description
    while True:
        description = input("Enter description: ").strip()

        if description:
            break

        print("Description cannot be empty.")

    # Date
    while True:
        date = input(
            "Enter date (YYYY-MM-DD) or press Enter for today: "
        ).strip()

        if date == "":
            date = datetime.now().strftime("%Y-%m-%d")
            break

        if validate_date(date):
            break

        print("Invalid date. Example: 2026-09-30")

    new_expense = {
        "id": generate_id(expenses),
        "amount": f"{amount:.2f}",
        "category": category.title(),
        "description": description,
        "date": date
    }

    expenses.append(new_expense)
    save_expenses(expenses)

    print("\nExpense added successfully!")
    print(f"Expense ID: {new_expense['id']}")


# -----------------------------
# Display expenses
# -----------------------------
def display_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n" + "=" * 85)
    print(
        f"{'ID':<5}"
        f"{'Amount':<12}"
        f"{'Category':<18}"
        f"{'Description':<30}"
        f"{'Date':<12}"
    )
    print("=" * 85)

    for expense in expenses:
        print(
            f"{expense['id']:<5}"
            f"₹{float(expense['amount']):<11.2f}"
            f"{expense['category']:<18}"
            f"{expense['description']:<30}"
            f"{expense['date']:<12}"
        )

    print("=" * 85)


# -----------------------------
# View all expenses
# -----------------------------
def view_expenses():
    expenses = load_expenses()

    print("\n========== ALL EXPENSES ==========")

    display_expenses(expenses)

    if expenses:
        total = sum(float(expense["amount"]) for expense in expenses)
        print(f"\nTotal Spending: ₹{total:.2f}")


# -----------------------------
# Filter by category
# -----------------------------
def filter_by_category():
    expenses = load_expenses()

    category = input("\nEnter category to filter: ").strip().lower()

    filtered = [
        expense
        for expense in expenses
        if expense["category"].lower() == category
    ]

    print(f"\n========== CATEGORY: {category.title()} ==========")

    display_expenses(filtered)

    if filtered:
        total = sum(float(expense["amount"]) for expense in filtered)
        print(f"\nCategory Total: ₹{total:.2f}")


# -----------------------------
# Filter by date range
# -----------------------------
def filter_by_date_range():
    expenses = load_expenses()

    print("\n========== FILTER BY DATE ==========")

    while True:
        start_date = input("Enter start date (YYYY-MM-DD): ").strip()

        if validate_date(start_date):
            break

        print("Invalid date.")

    while True:
        end_date = input("Enter end date (YYYY-MM-DD): ").strip()

        if validate_date(end_date):
            break

        print("Invalid date.")

    if start_date > end_date:
        print("Start date cannot be after end date.")
        return

    filtered = [
        expense
        for expense in expenses
        if start_date <= expense["date"] <= end_date
    ]

    print(f"\n========== {start_date} TO {end_date} ==========")

    display_expenses(filtered)

    if filtered:
        total = sum(float(expense["amount"]) for expense in filtered)
        print(f"\nDate Range Total: ₹{total:.2f}")


# -----------------------------
# Monthly summary
# -----------------------------
def monthly_summary():
    expenses = load_expenses()

    print("\n========== MONTHLY SUMMARY ==========")

    month = input(
        "Enter month (YYYY-MM) or press Enter for current month: "
    ).strip()

    if month == "":
        month = datetime.now().strftime("%Y-%m")

    try:
        datetime.strptime(month, "%Y-%m")
    except ValueError:
        print("Invalid month. Example: 2026-09")
        return

    monthly_expenses = [
        expense
        for expense in expenses
        if expense["date"].startswith(month)
    ]

    if not monthly_expenses:
        print(f"No expenses found for {month}.")
        return

    category_totals = defaultdict(float)

    for expense in monthly_expenses:
        category_totals[expense["category"]] += float(expense["amount"])

    total = sum(category_totals.values())

    print(f"\nMonth: {month}")
    print("-" * 55)
    print(f"{'Category':<20}{'Amount':<15}{'Percentage':<15}")
    print("-" * 55)

    for category, amount in sorted(
        category_totals.items(),
        key=lambda item: item[1],
        reverse=True
    ):
        percentage = (amount / total) * 100

        print(
            f"{category:<20}"
            f"₹{amount:<14.2f}"
            f"{percentage:.2f}%"
        )

    print("-" * 55)
    print(f"Total Spending: ₹{total:.2f}")


# -----------------------------
# Main menu
# -----------------------------
def main_menu():
    initialize_file()

    while True:
        print("\n")
        print("=" * 50)
        print("       EXPENSE TRACKER")
        print("=" * 50)

        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Filter by Category")
        print("4. Filter by Date Range")
        print("5. Monthly Summary")
        print("6. Exit")

        print("=" * 50)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            filter_by_category()

        elif choice == "4":
            filter_by_date_range()

        elif choice == "5":
            monthly_summary()

        elif choice == "6":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please select 1-6.")


# -----------------------------
# Program start
# -----------------------------
if __name__ == "__main__":
    main_menu()