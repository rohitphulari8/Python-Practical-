
print("========== Automated Email Scanner ==========")

text = input("Enter the email text: ")

at_count = 0
dot_count = 0
exclamation_count = 0

for char in text:
    if char == "@":
        at_count += 1
    elif char == ".":
        dot_count += 1
    elif char == "!":
        exclamation_count += 1

print("\n========== Email Scan Result ==========")
print("Number of '@' characters :", at_count)
print("Number of '.' characters :", dot_count)
print("Number of '!' characters :", exclamation_count)

