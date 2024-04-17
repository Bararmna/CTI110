 #Bararmna Missowina

 # 4/12/2024

 # P2HW2

 # understanding of lists
 
# Asks the user to enter grades for following tests.
## Module 1
##Module 2
##Module 3
##Module 4
##Module 5
##Module 6
grades =[]
grades.append(float(input("Enter grade for Module 1: ")))
grades.append(float(input("Enter grade for Module 2: ")))
grades.append(float(input("Enter grade for Module 3: ")))
grades.append(float(input("Enter grade for Module 4: ")))
grades.append(float(input("Enter grade for Module 5: ")))
grades.append(float(input("Enter grade for Module 6: ")))

# The lowest grade in the list
lowest_grade = min(grades)
# The highest grade in the list
highest_grade = max(grades)
# the Sum of grades
total_grades = sum(grades)
# Calculate the average grade
avarage_grade = total_grades /  len(grades)
print()
# Display results
print(f"lowest_grade:       {lowest_grade:}")
print(f"highest_grade:      {highest_grade:}")
print(f"total_grades:       {total_grades:}")
print(f"avarage_grade:      {avarage_grade:.2f}")
