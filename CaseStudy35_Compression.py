# Topic 35 - Text Compression - 2600308
print("=== Topic 35 ===")
s = "aaabbbcccaaa"
compressed = ""
i = 0
while i < len(s):
    count = 1
    while i+count < len(s) and s[i+count] == s[i]:
        count += 1
    compressed += s[i] + str(count)
    i += count
print(f"Original: {s} len {len(s)}")
print(f"Encoded: {compressed} len {len(compressed)}")
if len(compressed) >= len(s):
    print("Not Beneficial")
