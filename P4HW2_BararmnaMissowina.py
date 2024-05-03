# Missowia Bararmna

# 4/26/2024

# P4HW2

# student ability to edit and enhance exiting program



total_overtime_pay = 0
total_regular_pay = 0
gross_pay_total = 0
num_employees = 0

# Enter employee's name
Employee_Name = input("Enter employee's name or 'Done' to terminate: ")



# Enter user pay rate and hours worked
while Employee_Name.lower() != "done":
    Num_of_hours_worked = float(input("How many hours did " + Employee_Name + " work? : "))
    Employee_pay_rate = float(input("What is " + Employee_Name + "'s pay rate? : "))
    print(f"Employee Name = {Employee_Name}")

    # Evaluate if employee has worked overtime
    if Num_of_hours_worked > 40: 
        overtime_hours = Num_of_hours_worked - 40
        overtime_pay = overtime_hours * (Employee_pay_rate * 1.5)
    else:
        overtime_hours = 0
        overtime_pay = 0

    # Employee's regular hours and pay
    if Num_of_hours_worked == 40:
        regular_hours = 40
    else:
        regular_hours = Num_of_hours_worked
    regular_pay = regular_hours * Employee_pay_rate

    # Calculate the gross pay
    gross_pay = regular_pay + overtime_pay

    #  totals
    total_regular_pay += regular_pay
    total_overtime_pay += overtime_pay
    gross_pay_total += gross_pay
    num_employees += 1

    # Display the results for each employee
    print(" Num_of_hours_worked     Employee_pay_rate    overtime_hours     overtime_pay    regular_pay    gross_pay")
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print(f'{Num_of_hours_worked:<14.2f}  {Employee_pay_rate:<19.2f}  {overtime_hours:<18.2f}  {overtime_pay:<22.2f}  {regular_pay:<19.2f}  {gross_pay:<19.2f}')

    # Prompt for the next employee's name
    Employee_Name = input("Enter employee's name or 'Done' to terminate: ")

# Display results
print(f"Total Overtime Pay:            ${total_overtime_pay}")
print(f"Total Regular Pay:             ${total_regular_pay}")
print(f"Gross Pay Total:               ${gross_pay_total}")
print(f"Number of Employees Entered:   {num_employees}")


