 #Bararmna Missowina

 # 4/23/2024

 # P4HW1

 # collection of user score using loop


# Take input for the number of scores
scores = []
num_scores = int(input("Enter the number of scores: "))

# creation of a loop
for score_count in range(num_scores):
    # Take input for the score
    entered_score = int(input(f"Enter score #{score_count + 1}: "))

    # Check if the entered score is valid range
    while entered_score < 0 or entered_score > 100:
        print("INVALID SCORE entered!!! ")
        print("Score should be between 0 and 100.")
        # notify the user  for a valid score
        entered_score = int(input(f"Enter score #{score_count + 1} again: "))

    # Append the entered score to the list of scores
    scores.append(entered_score)

# Find the lowest score
lowest_score = min(scores)

# Remove the lowest score from the list of scores
scores.remove(lowest_score)

# Calculate the average score
average_score = sum(scores) / len(scores)

#Determine the letter grade

if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    lgrade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display results
print(f"lowest_score:       {lowest_score:}")
print(f"score list after droping lowest score:      {scores:}")
print(f"average_score:      {average_score:}")
print (f"grade:             {grade:}")















