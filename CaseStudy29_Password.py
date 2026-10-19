# Topic 29 - Password Validation - 2600308
print("=== Topic 29 ===")
passwords = ["abc", "Hello123", "Hello@123", "helloworld"]
for pwd in passwords:
    print(f"\nChecking: {pwd}")
    if len(pwd) < 8:
        print("Fail: Min 8 chars")
        continue
    has_digit = False
    has_upper = False
    for ch in pwd:
        if ch.isdigit(): has_digit = True
        if ch.isupper(): has_upper = True
    if not has_digit: print("Fail: Need Digit")
    elif not has_upper: print("Fail: Need Uppercase")
    else: print("Pass: Valid Password")
