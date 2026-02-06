contacts = {
    "Rahul": "9876543210",
    "Sneha": "9123456789",
    "Amit": "9988776655"
}

contacts["Priya"] = "9012345678"
contacts["Amit"] = "8899001122"

print("Lookup Existing:", contacts.get("Rahul", "Contact not found"))
print("Lookup Missing:", contacts.get("Karan", "Contact not found"))

print("\nContact List:")
for name, phone in contacts.items():
    print("Contact:", name, "| Phone:", phone)
