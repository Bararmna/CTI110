
# Bararmna Missowina
# 4/6/2024
# P1HW2
# collect frmm users.


# Pseudocod
#3. Ask user to enter their budget

#4. Ask user to enter travel destination

#5. Ask user for amount they will spend on gas

#6. Ask user for amount they will spend on accommodation

#7. Ask user for amount they will spend on food

#8. Add expenses

#9. Subtract expenses from budget

#10. Display results
print("This program calculates and displays travel expenses")
Budget = float(input("Enter Budget:"))
Destination = input("Enter travel destination:")
Gaz_expense = float(input("How much do you think you will spend on gaz:"))
Accomodation_expense = float(input("Approximately, how much will you spend for accomodation:"))
Food_expense= float(input("How much will you spend for food:"))
print("Total_Travel_Expenses")
print("Location=Nashville")
print("Initial Budget:", Budget)

Total_Travel_Expenses = Gaz_expense + Accomodation_expense + Food_expense
print("Total_Travel_Expenses:", Total_Travel_Expenses)

remaining_Budget = Budget - Total_Travel_Expenses
print("remaining Budget:", remaining_Budget)



