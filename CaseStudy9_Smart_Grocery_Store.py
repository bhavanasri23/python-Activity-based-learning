# Case Study 9 - Smart Grocery Store
# Bhavana Sri - 2600308

print("=== Smart Grocery Store ===")

items = {"Rice": 50, "Oil": 120, "Sugar": 45, "Milk": 60}
cart = []
total = 0

print("\nAvailable Items:")
for i, p in items.items():
    print(f"{i}: Rs.{p}")

cart = ["Rice", "Milk", "Sugar"]
for item in cart:
    total += items[item]

print(f"\nCart Items: {cart}")
print(f"Subtotal: Rs.{total}")

if total > 200:
    discount = total * 0.1
    print(f"Discount 10%: Rs.{discount}")
    total -= discount

print(f"Final Total: Rs.{total}")
print("Thank You - Bhavana Sri 2600308")
