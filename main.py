import sqlite3
import datetime

connect_to_db = sqlite3.connect("expenses.db")
set_cursor = connect_to_db.cursor()

while True:
    print("Select an option:")
    print("1. Enter a new expense")
    print("2. View expenses summary")

    choice = int(input())

    # Enter your expenses
    if choice == 1:
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        description = input("Enter the description of the expense: ")

        set_cursor.execute("SELECT DISTINCT category FROM expenses")

        categories = set_cursor.fetchall()

        print("Select a category by number:")
        for idx, category in enumerate(categories):
            print(f"{idx + 1}. {category[0]}")
        print(f"{len(categories) + 1}. Create a new category")

        category_choice = int(input())
        if category_choice == len(categories) + 1:
            category = input("Enter the new category name: ")
        else:
            category = categories[category_choice - 1][0]

        price = input("Enter the price of the expense: ")

        set_cursor.execute(
            "INSERT INTO expenses (Date, description, category, price) VALUES (?, ?, ?, ?)",
            (date, description, category, price),
        )
        connect_to_db.commit()

    # View your expenses
    elif choice == 2:
        print("Select an option:")
        print("1. View all expenses")
        print("2. View monthly expenses by category")

        view_choice = int(input())
        if view_choice == 1:
            set_cursor.execute("SELECT * FROM expenses")
            expenses = set_cursor.fetchall()
            for expense in expenses:
                print(expense)
        elif view_choice == 2:
            month: str = input("Enter the month (MM): ")
            year: str = input("Enter the year (YYYY): ")
            # Here I want to show expenses organised by category
            set_cursor.execute(
                """SELECT category, SUM(price) FROM expenses 
                               WHERE strftime("%m', Date) = ? AND strftime("%Y', Date) = ?
                               GROUP BY category""",
                (month, year),
            )
            expenses = set_cursor.fetchall()
            for expense in expenses:
                print(f"Category: {expense[0]}, Total: {expense[1]}")
        else:
            exit()
    else:
        exit()

    repeat = input("Would you like to do something else? (y/n)?\n")
    if repeat.lower() != "y":
        break

connect_to_db.close()
