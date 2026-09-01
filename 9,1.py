
print("========== Consumer Transaction Tracker ==========")

transactions = []

# Accept five transaction amounts
for i in range(5):
    amount = float(input("Enter transaction amount " + str(i + 1) + ": "))
    transactions.append(amount)

# Display transactions
print("\n--- Consumer Transactions ---")
for i in range(len(transactions)):
    print("Transaction", i + 1, ":", transactions[i])

# Find largest transaction
largest = max(transactions)

# Calculate average spending
average = sum(transactions) / len(transactions)

# Display results
print("\n--- Transaction Summary ---")
print("Largest Transaction Amount :", largest)
print("Average Spend :", average)
