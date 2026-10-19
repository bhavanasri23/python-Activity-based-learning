# University Scholarship Allocation System
# Student: Bhavana Sri - 2600308
# Case Study 1

students = [
    ("Bhavana", 88, 90, 75, 120000),
    ("Ravi", 92, 95, 80, 90000),
    ("Anu", 78, 82, 60, 200000),
    ("Kiran", 85, 88, 78, 100000),
    ("Priya", 92, 92, 82, 110000)
]

eligible = []
print("=== University Scholarship Evaluation ===")

for name, agg, attend, sub_min, income in students:
    if agg >= 80 and attend >= 85 and sub_min >= 70 and income <= 150000:
        eligible.append((name, agg, attend))
        print(f"{name}: ELIGIBLE - {agg}%")
    else:
        print(f"{name}: NOT ELIGIBLE")

# Ranking - Nested loop sorting (syllabus method)
for i in range(len(eligible)):
    for j in range(i+1, len(eligible)):
        if eligible[j][1] > eligible[i][1]:
            eligible[i], eligible[j] = eligible[j], eligible[i]
        elif eligible[j][1] == eligible[i][1]:
            if eligible[j][2] > eligible[i][2]:
                eligible[i], eligible[j] = eligible[j], eligible[i]

print("\n--- Final Ranked List ---")
rank = 1
for name, agg, attend in eligible:
    print(f"Rank {rank}: {name} - {agg}%, Attendance {attend}%")
    rank += 1
