# Case Study 3 - Hospital Billing and Patient Classification
# Bhavana Sri - 2600308
# Topic 3 - Official

print("=== Hospital Billing & Patient Classification - Topic 3 ===")
print("Bhavana Sri - 2600308\n")

# Store Patient Data as Nested List
# [PatientName, Consultation, Diagnostic, Treatment, Age, Category]
# Category: 0-General, 1-Senior Citizen (>60), 2-BPL, 3-Insurance Holder
patients = [
    ["Ramesh", 500, 1500, 5000, 65, 1],
    ["Sita", 400, 800, 2000, 30, 0],
    ["Krishna", 500, 2000, 10000, 45, 2],
    ["Lakshmi", 600, 3000, 15000, 70, 3]
]

print("--- Patient Billing Details ---")
print("Name | Consult | Diag | Treat | Total | Discount | Final Bill | Classification")

# To store results for summary
bill_table = []

for p in patients:
    name, consult, diag, treat, age, cat = p  # Tuple unpacking via list
    
    # 1. Validation of Billing Constraints
    if consult < 0 or diag < 0 or treat < 0:
        print(f"{name} - INVALID BILL: Negative charges not allowed")
        continue
    
    total = consult + diag + treat
    
    if total == 0:
        print(f"{name} - INVALID BILL: Total cannot be zero")
        continue

    # 2. Apply Conditional Concessions (Payment Policy)
    discount = 0
    policy = ""

    if cat == 1:  # Senior Citizen
        discount = total * 0.10
        policy = "Senior Citizen 10%"
    elif cat == 2:  # BPL
        discount = total * 0.20
        policy = "BPL 20%"
    elif cat == 3:  # Insurance
        discount = total * 0.30
        # Maximum concession limit Rs.5000 for insurance
        if discount > 5000:
            discount = 5000
        policy = "Insurance 30% (Max 5000)"
    else:
        policy = "No Concession - General"

    # Extra Senior check even if category 0 but age >60
    if age > 60 and cat == 0:
        discount = total * 0.10
        policy = "Senior Citizen 10% (Age Based)"

    final_bill = total - discount

    # 3. Classification as per payment policy
    classification = ""
    if final_bill > 15000:
        classification = "High Bill Patient"
    elif discount > 0:
        classification = "Concessional Patient"
    else:
        classification = "Fully Paid - General"

    print(f"{name} | {consult} | {diag} | {treat} | {total} | {discount:.0f} | {final_bill:.0f} | {classification} ({policy})")
    
    # Store for summary: [Name, Total, Discount, Final, Classification]
    bill_table.append([name, total, discount, final_bill, classification])

# 4. Summary Analysis
print("\n--- Summary Report ---")
total_collection = 0
total_discount_given = 0
high_bill_count = 0

for row in bill_table:
    total_collection += row[3]
    total_discount_given += row[2]
    if row[4] == "High Bill Patient":
        high_bill_count += 1

print(f"Total Patients Processed: {len(bill_table)}")
print(f"Total Hospital Collection: Rs.{total_collection:.0f}")
print(f"Total Discount Given: Rs.{total_discount_given:.0f}")
print(f"High Bill Patients Count: {high_bill_count}")

# 5. Identify patient with highest bill
max_bill = 0
max_patient = ""
for row in bill_table:
    if row[3] > max_bill:
        max_bill = row[3]
        max_patient = row[0]

print(f"Highest Final Bill: {max_patient} - Rs.{max_bill:.0f}")

print("\n--- Payment Policy Used ---")
print("Win= General: 0%, Senior: 10%, BPL: 20%, Insurance: 30% Max 5000")
print("\nTopic 3 Complete - Bhavana Sri 2600308")
