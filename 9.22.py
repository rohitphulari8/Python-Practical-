
print("========== Student Score Filter ==========")

grades = []

# Enter 5 grades
for i in range(5):
    grade = int(input("Enter grade: "))
    grades.append(grade)

print("\nOriginal Grades:")
print(grades)

# Update a grade
index = int(input("Enter index position to update: "))

if 0 <= index < len(grades):
    new_grade = int(input("Enter new grade: "))
    grades[index] = new_grade

    print("\nCorrected Grades:")
    print(grades)

else:
    print("Invalid index position.")
