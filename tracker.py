#Project: Banner and Menu
#  Lab 3
#  Author: Hisham H. Muctar 
#  Shows the value added tax and budget comparison of the user inputted expenses
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
tax1 = float(input("Tax rate(%): "))            #new
budget = float(input("Budget: "))               #new

print("------------------------------------------")
print("Summary of your expenses")
print(f"  - {item1} :\t\tP{amount1:.2f}")
print(f"  - {item2} :\t\tP{amount2:.2f}")
average = (amount1 + amount2) / 2               #added variable for average as well as its print statement
print(f"Average:\t\tP{average:.2f}")
tax_amount = (amount1 + amount2) * tax1 / 100   #tax calculator
print(f"Tax:\t\t\tP{tax_amount:.2f}")
Expenses = (amount1 + amount2 + tax_amount)
print(f"Total Expenses:\t\tP{Expenses:.2f}")
overBudget = (Expenses > budget)                #new variable to check if the expenses are over the budget
print("Overbudget?:\t\t" , overBudget)  
print(f"Budget Remaining: \tP{(budget - (amount1 + amount2 + tax_amount)):.2f}")     #new budget calculation with tax
print("------------------------------------------")
print("Made by: Hisham H. Muctar | Installment 3")

