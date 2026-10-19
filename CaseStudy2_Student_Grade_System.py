# Case Study 2 - Student Grade System
# Bhavana Sri - 2600308

print("=== Student Grade System ===")

name = "Bhavana"
marks = [85, 90, 78, 92, 88]

total = sum(marks)
avg = total / len(marks)

print(f"Name: {name}")
print(f"Marks: {marks}")
print(f"Total: {total}")
print(f"Average: {avg}")

if avg >= 90:
    grade = "A+"
elif avg >= 80:
    grade = "A"
elif avg >= 70:
    grade = "B"
else:
    grade = "C"

print(f"Grade: {grade}")
print("Bhavana Sri - 2600308")
