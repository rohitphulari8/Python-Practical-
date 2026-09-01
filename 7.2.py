
print("========== Python Word Count Utility ==========")

paragraph = input("Enter a paragraph: ")

words = paragraph.lower().split()
count = 0

for word in words:
    if word.strip(".,!?;:'\"()[]{}") == "python":
        count += 1

print("\n========== Result ==========")
print("The word 'Python' appears", count, "times.")
