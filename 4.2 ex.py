
print("***********Smart Home Climate Monitoring System***********")

status = input("Enter atmospheric status: ").lower().strip()

if status == "hot":
    print("Atmospheric status is hot")
    print("Hardware Recommendation: Turn on AC")

elif status == "cold":
    print("Atmospheric status is cold")
    print("Hardware Recommendation: Activate heater")

elif status == "normal":
    print("Atmospheric status is normal")
    print("Hardware Recommendation: Keep AC and heater OFF")

else:
    print(f"Invalid status: '{status}'")
    print("Please enter hot, cold, or normal.")
