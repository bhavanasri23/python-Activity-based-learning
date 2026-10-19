# Topic 28 - Repeated Transaction - 2600308
print("=== Topic 28 ===")
ids = ["TX101", "TX102", "TX101", "TX103", "TX102"]
amounts = [500, 2000, 500, 150, 2000]
suspicious = []
for i in range(len(ids)):
    for j in range(i+1, len(ids)):
        if ids[i] == ids[j]:
            suspicious.append(ids[i])
print(f"Duplicate IDs: {suspicious}")
for i in range(len(amounts)):
    if amounts[i] > 1000:
        print(f"Threshold Violation: {ids[i]} - {amounts[i]}")
