# Topic 13 - ATM Simulation - 2600308
print("=== Topic 13 ===")
balance = 5000
transactions = [("Deposit", 2000), ("Withdraw", 1500), ("Withdraw", 8000), ("Deposit", 500)]
for ttype, amt in transactions:
    if ttype == "Deposit":
        balance += amt
        print(f"Deposit {amt} -> Balance {balance}")
    else:
        if amt > balance or amt > 5000:
            print(f"Withdraw {amt} Failed - Limit/Balance")
        else:
            balance -= amt
            print(f"Withdraw {amt} -> Balance {balance}")
print(f"Final Balance: {balance}")
