# Case Study 13 - Smart Cab Booking System
# Bhavana Sri - 2600308
# Topic 13

print("=== SMART CAB BOOKING - Topic 13 ===")
print("Bhavana Sri - 2600308\n")

cabs = {
    "Mini": {"price_per_km": 10, "available": 5},
    "Sedan": {"price_per_km": 15, "available": 3},
    "SUV": {"price_per_km": 20, "available": 2}
}

print("--- Available Cabs ---")
for cab, details in cabs.items():
    print(f"{cab} - Rs.{details['price_per_km']}/km | Available: {details['available']}")

# Customer Booking
customer = "Bhavana"
pickup = "Vijayawada"
drop = "Gannavaram Airport"
distance = 20  # km
cab_type = "Sedan"

print(f"\nCustomer: {customer}")
print(f"From: {pickup} To: {drop}")
print(f"Distance: {distance}km, Cab: {cab_type}")

if cabs[cab_type]['available'] > 0:
    fare = distance * cabs[cab_type]['price_per_km']
    gst = fare * 0.05
    total = fare + gst
    
    cabs[cab_type]['available'] -= 1
    
    print("\n--- BOOKING CONFIRMED ---")
    print(f"Base Fare: Rs.{fare}")
    print(f"GST (5%): Rs.{gst}")
    print(f"Total Fare: Rs.{total}")
    print(f"Driver Assigned: Ravi - AP05 AB 1234")
    print(f"OTP: 4567")
else:
    print(f"Sorry! {cab_type} Not Available!")

print("\n--- Updated Availability ---")
for cab, details in cabs.items():
    print(f"{cab}: {details['available']} Cabs Left")

print("\nHappy Journey! - Bhavana Sri 2600308")
