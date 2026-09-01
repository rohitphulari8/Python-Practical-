
def sanitize_name(first_name, last_name):
    first_name = first_name.strip().title()
    last_name = last_name.strip().title()

    full_name = f"{first_name} {last_name}"

    return full_name


first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

result = sanitize_name(first_name, last_name)

print("\n--- Cleaned Full Name ---")
print("Full Name:", result)
