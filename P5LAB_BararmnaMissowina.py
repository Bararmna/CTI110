
#Bararmna Missowina
# 5/1/2024
#P5LAB
#Use of loops, functions and module import


# amount owed

import random

def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    change_owed = float(input("You owe: $"))
#   Prompt the user to enter the amount of cash they will put into the self-checkout
 
    amount_paid = float(input("Enter the amount of cash you will put into the self-checkout: $"))
    
# Calculate the amount of change owed to the customer.
    change_owed = amount_paid - amount_owed  
    print(f"Change is: ${change_owed}")
# disperse change    
    disperse_change(change_owed)

def disperse_change(change_owed):
    num_dollars = change_owed // 100
    change_owed = change_owed - (num_dollars * 100)

    num_quarters = change_owed // 25
    change_owed = change_owed - (num_quarters * 25)

    num_dimes = change_owed // 10
    change_owed = change_owed - (num_dimes * 10)

    num_nickels = change_owed // 5
    change_owed = change_owed - (num_nickels * 5)

    num_pennies = change_owed

    if num_dollars > 0: 
        if num_dollars == 1:
            print(f"{num_dollars} dollar")
        else:
            print(f"{num_dollars} dollars")

    if num_quarters  > 0:
        if num_quarters  == 1:
            print(f"{num_quarters }quarter  ")
        else:
            print(f"{num_quarters } quarters  ")

    if num_dimes   > 0:
        if num_dimes   == 1:
            print(f"{num_dimes  } dime   ")
        else:
            print(f"{num_dimes  }  dimes  ")

    if num_nickels  > 0:
        if num_nickels  == 1:
            print(f"{num_nickels  }  nickel ")
        else:
            print(f"{num_nickels  }  nickels  ")

    if num_pennies   > 0:
        if num_pennies  == 1:
            print(f"{num_pennies  }  pennie   ")
        else:
            print(f"{num_pennies  }  pennies  ")

if __name__ == "__main__":
    main()
