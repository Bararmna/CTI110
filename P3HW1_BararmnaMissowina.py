# I was supposed to put a comment here
# Bararmna Missowina
# 4/17/2024
# P3HW1
# Partial program with bugs


# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 4: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5]
# TO DO: determine lowest, highest , sum and average for grades

Lowest_grade= min(grades)
Highest_grade = max(grades)
Sum_of_grades = sum(grades)
Avarage_grade = Sum_of_grades  / len(grades)

print()
# Display a result
print(f"Lowest_grade:       {Lowest_grade:.1f}")
print(f"Highest_grade:      {Highest_grade:.1f}")
print(f"Sum_of_grades:      {Sum_of_grades:.1f}")
print(f"Avarage_grade:      {Avarage_grade:.2f}")



print()

# determine letter grade for average


if Avarage_grade >= 90:
   print('Your grade is: A')
elif Avarage_grade  > 80:
   print('Your grade is: B')
else:
   print('Your grade is: F') # TO DO: finish this





