# Project: Expense Tracker
# Lab 4
# Author: Hisham H. Muctar
# Section: DIT 3-7
# Installment 4: The Tracker Makes Decisions

print("=" * 40)
print("\t     EXPENSE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40 + "\n")

print("MAIN MENU")
print("  [1] Add an expense            (coming soon)")
print("  [2] View all expenses         (coming soon)")
print("  [3] Show total spent          (coming soon)")
print("  [4] Exit                      (coming soon)\n")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")

# subtotal starts at 0 and is updated right after each read
subtotal = 0

item1 = input("First expense? ")
amount1 = float(input("Amount? "))
subtotal += amount1

# Size message for first expense (checked in order: most restrictive first)
if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

item2 = input("Second expense? ")
amount2 = float(input("Amount? "))
subtotal += amount2

# Size message for second expense
if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

# Warning if both amounts are over 100
if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

# Calculations using required variable names
average = subtotal / 2
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
over_budget = total > budget
left = budget - total

print("\n" + "-" * 40)
print("SUMMARY")
print(f"  - {item1}:\t${amount1:.1f}")
print(f"  - {item2}:\t${amount2:.1f}")
print(f"Subtotal:\t${subtotal:.1f}")
print(f"Average:\t${average:.1f}")
print(f"Tax ({tax_percent:.1f}%):\t${tax:.1f}")
print(f"Grand total:\t${total:.1f}")

# Verdict logic (never shows a negative amount)
if over_budget:
    print(f"Over budget by ${total - budget:.1f}!")
elif total > (0.90 * budget):
    print(f"Careful: only ${left:.1f} left.")
else:
    print(f"Within budget. ${left:.1f} left.")

print("-" * 40)
print("Made by: Hisham H. Muctar  |  Installment 4")
