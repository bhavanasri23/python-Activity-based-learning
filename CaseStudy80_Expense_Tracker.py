# Case Study 80 - Smart Expense Tracker & Budget Analyzer
# Bhavana Sri - 2600308
# Topic 80 - Best Topic

print("=== SMART EXPENSE TRACKER - Topic 80 ===")
print("Bhavana Sri - 2600308")

expenses = {
    "Food": 2500,
    "Transport": 1200,
    "Shopping": 3000,
    "Recharge": 500,
    "College Fees": 5000
}

total_expense = sum(expenses.values())
budget = 15000
remaining = budget - total_expense

print("\n--- Monthly Expenses ---")
for category, amount in expenses.items():
    print(f"{category}: Rs.{amount}")

print(f"\nTotal Spent: Rs.{total_expense}")
print(f"Monthly Budget: Rs.{budget}")
print(f"Remaining Balance: Rs.{remaining}")

# Budget Analysis
if remaining < 2000:
    print("Alert: Low Balance! Control Shopping!")
elif remaining < 5000:
    print("Warning: Budget is getting over!")
else:
    print("Great: Budget is under control!")

# Highest Expense
max_expense = max(expenses, key=expenses.get)
print(f"Highest Spent On: {max_expense} - Rs.{expenses[max_expense]}")

print("\n--- Analysis Complete - Bhavana Sri 2600308 ---")
