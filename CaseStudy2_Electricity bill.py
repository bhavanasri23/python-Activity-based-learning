BLUE = "\033[94m"
RESET = "\033[0m"
print(BLUE)
# Topic 2 - Progressive Electricity Billing - 2600308
print("=== Topic 2 ===")
units = 280
bill = 0
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100*5 + (units-100)*7
else:
    bill = 100*5 + 100*7 + (units-200)*10

bill += 50  # Fixed charge
print(f"Units: {units}, Bill: Rs.{bill}")
if bill > 2000:
    print("Unusual Increase - High Usage!")
print(RESET)
