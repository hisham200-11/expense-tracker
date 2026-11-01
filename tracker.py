# Project: Expense Tracker
# Lab 5
# Author: Hisham H. Muctar
# Section: DIT 3-7
# Installment 5: The Menu Comes Alive

print("=" * 40)
print("\t     EXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40 + "\n")

# Setup asked once before the loop, protected with loops and try/except
name = input("What's your name? ")

# Protected tax rate input: re-prompts on string/invalid input until a valid number is given
while True:
    try:
        tax_percent = float(input("Tax rate %? "))
        break
    except ValueError:
        print("  Please enter a valid number for tax rate.")

# Protected budget input: re-prompts on string/invalid input until a valid number is given
while True:
    try:
        budget = float(input("Your budget? "))
        break
    except ValueError:
        print("  Please enter a valid number for budget.")

print(f"Welcome, {name}!\n")

subtotal = 0
count = 0

# Interactive menu loop
while True:
    print("MAIN MENU")
    print("  [1] Add an expense")
    print("  [2] View all expenses (coming soon)")
    print("  [3] Show total spent")
    print("  [4] Exit")

    choice = input("Choose 1-4: ")

    if choice == "1":
        # Protected amount input: re-prompts until a valid number is given
        while True:
            try:
                amount = float(input("Amount? "))
                break
            except ValueError:
                print("  Please enter a valid number for amount.")

        subtotal += amount
        count += 1

        # Size check decision (contained once in the file)
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        over_budget = total > budget
        left = budget - total

        print(f"  Expenses:     {count}")
        print(f"  Subtotal:     ${subtotal:.1f}")
        print(f"  Tax ({tax_percent:.1f}%):  ${tax:.1f}")
        print(f"  Grand total:  ${total:.1f}")

        if over_budget:
            print(f"  Over budget by ${total - budget:.1f}!")
        elif total > (0.90 * budget):
            print(f"  Careful: only ${left:.1f} left.")
        else:
            print(f"  Within budget. ${left:.1f} left.")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print("Made by: Hisham H. Muctar  |  Installment 5")
        print("=" * 40)
        break

    else:
        # Handles any choice outside 1-4 (e.g. 7, 99, 'abc')
        print("  Please choose 1, 2, 3 or 4.")
