# Topic 12 - Attendance Recovery - 2600308
print("=== Topic 12 ===")
present = 35
total = 50
percent = present/total*100
print(f"Current: {percent:.1f}%")
required = 75
need = 0
# Calculate classes needed to reach 75%
while percent < required:
    present += 1
    total += 1
    percent = present/total*100
    need += 1
print(f"Need {need} more classes to reach 75%")
