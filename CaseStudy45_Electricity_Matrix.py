# Topic 45 - Electricity Matrix - 2600308
print("=== Topic 45 ===")
# [Fan, Light, AC] x 7 days
matrix = [
    [2, 3, 1],
    [2, 4, 2],
    [3, 3, 5],
    [2, 2, 1],
    [1, 3, 2],
    [2, 4, 6],
    [3, 3, 1]
]
daily_total = []
for day in matrix:
    daily_total.append(sum(day))
print(f"Daily Totals: {daily_total}")
print(f"Max Consumption Day: Day {daily_total.index(max(daily_total))+1}")
appliance_total = [0,0,0]
for day in matrix:
    for j in range(3):
        appliance_total[j] += day[j]
print(f"Appliance Totals [Fan, Light, AC]: {appliance_total}")
