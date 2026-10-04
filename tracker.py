#Project: Banner and Menu
#  Lab 2 
#  Author: Hisham H. Muctar 
#  Shows landing page and ask for two expenses and total
print("==========================================")
print("\t     EXPENSE TRACKER")
print("\tKnow where your money goes!")
print("==========================================\n")
print("Welcome this is your personal Expense Tracker!\n")
print("MAIN MENU")
print(" [1] Add Expense \t(coming soon)")
print(" [2] View All Expenses \t(coming soon)")
print(" [3] Show Total Expense\t(coming soon)")
print(" [4] Exit\n")
name = input("What's your name? ")
print(f"Hello {name}, welcome to your personal Expense Tracker!\n")
item1 = input("First expense: ")
amount1 = float(input("Amount?: "))
item2 = input("Second expense: ")
amount2 = float(input("Amount?: "))

print("------------------------------------------")
print("Summary of your expenses")
print(f"  - {item1} : P{amount1:.2f}")
print(f"  - {item2} : P{amount2:.2f}")
print("------------------------------------------")
print("Made by: Hisham H. Muctar | Installment 2")

