# Topic 31 - Answer Evaluation - 2600308
print("=== Topic 31 ===")
key = "ABCDD"
answers = ["ABCCD", "ABCDD", "ABBDD"]
for ans in answers:
    correct = 0
    for i in range(len(key)):
        if ans[i] == key[i]:
            correct += 1
    incorrect = len(key) - correct
    score = correct*4 - incorrect*1  # Negative marking
    print(f"{ans} -> Correct:{correct}, Score:{score}")
