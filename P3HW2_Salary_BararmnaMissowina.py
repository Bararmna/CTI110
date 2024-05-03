 # Missowia Bararmna

 # 4/19/2024

  # P3HW2_Salary

  # understamding of decision.

  #Ask user to enter name of  employee
Employee_Name =  input("Enter employee's name: ")
  
  # the number of hours the employee worked this week
Num_of_hours_worked  = float(input(" Enter number of hours worked: "))

  
  # enter employee's pay rate
Employee_pay_rate = float(input("   Enter employee's pay rate: "))
                             

#evalute if employee has worked overtime
if Num_of_hours_worked > 40: 
   overtime_hours = Num_of_hours_worked - 40
   overtime_owed = overtime_hours * ( Employee_pay_rate * 1.5)
else :
    overtime_hours = 0
    overtime_owed  = 0

# employee's regular hours
if Num_of_hours_worked == 40:
   regular_hours = 40
    
else:
     regular_hours = Num_of_hours_worked
     regular_pay = regular_hours * Employee_pay_rate
     
# Display the gross pay
gross_pay = regular_pay + overtime_owed
print(f" Employee_name =  {Employee_Name } ")

print("Employee_Name         Num_of_hours_worked     Employee_pay_rate    overtime_hours     overtime_owed    regular_pay    gross_pay")
print("--------------------------------------------------------------------------------------------------------------------------------")


#print(f'{Employee_Name:<20} {Num_of_hours_worked:<11.2f} {Employee_pay_rate:<19.2f} {overtime_hours:<8.2f} {overtime_owed:<13.2f} {regular_pay:<13.2f} {gross_pay:<17.2f}')

print(f'{Employee_Name:<15}  {Num_of_hours_worked:<14.2f}  {Employee_pay_rate:<19.2f}  {overtime_hours:<18.2f}  {overtime_owed:<22.2f}  {regular_pay:<19.2f}  {gross_pay:<19.2f}')
