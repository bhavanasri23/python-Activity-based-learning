# Case Study 47 - Sports Tournament Ranking System
# Bhavana Sri - 2600308
# Topic 47 - Official

print("=== Topic 47 - Sports Tournament Ranking System ===")
print("Bhavana Sri - 2600308\n")

# Nested List: [TeamName, [Match1, Match2, Match3, Match4]]
teams_data = [
    ["CSK", [78, 82, 75, 80]],
    ["MI", [80, 75, 82, 78]],
    ["RCB", [85, 80, 79, 78]],
    ["KKR", [70, 75, 72, 68]]
]

# For tie-breaking: Total Wins if points equal
wins_data = [
    ("CSK", 3),
    ("MI", 3),
    ("RCB", 2),
    ("KKR", 1)
]

print("--- Team Scores ---")
ranking_table = []  # [Team, Total, Average, MaxScore]

for team in teams_data:
    name, scores = team  # Tuple unpacking
    total = 0
    max_score = 0
    for s in scores:
        total += s
        if s > max_score:
            max_score = s
    avg = total / len(scores)
    
    # Find wins for tie-break
    wins = 0
    for w in wins_data:
        if w[0] == name:
            wins = w[1]
    
    ranking_table.append([name, total, avg, max_score, wins])
    print(f"{name} -> Scores: {scores} Total: {total} Avg: {avg:.1f} Max: {max_score} Wins: {wins}")

# Ranking with Tie-Breaking Rules
# Rule 1: Higher Total, Rule 2: If tie then Higher Wins, Rule 3: If still tie then Higher Max Score
print("\n--- Final Ranking (Tie-Break Applied) ---")

# Simple Bubble Sort for Ranking
for i in range(len(ranking_table)):
    for j in range(i+1, len(ranking_table)):
        # Compare
        if ranking_table[j][1] > ranking_table[i][1]:  # Higher total
            ranking_table[i], ranking_table[j] = ranking_table[j], ranking_table[i]
        elif ranking_table[j][1] == ranking_table[i][1]:
            # Tie - check wins
            if ranking_table[j][4] > ranking_table[i][4]:
                ranking_table[i], ranking_table[j] = ranking_table[j], ranking_table[i]
            elif ranking_table[j][4] == ranking_table[i][4]:
                # Still tie - check max score
                if ranking_table[j][3] > ranking_table[i][3]:
                    ranking_table[i], ranking_table[j] = ranking_table[j], ranking_table[i]

# Print Ranking
rank = 1
for row in ranking_table:
    name, total, avg, max_s, wins = row
    print(f"Rank {rank}: {name} - Total {total}, Wins {wins}, Max {max_s}, Avg {avg:.1f}")
    rank += 1

print("\n--- Winner ---")
print(f"Champion: {ranking_table[0][0]} with {ranking_table[0][1]} points")

print("\nTopic 47 Complete - Bhavana Sri 2600308")
