#Bararmna Missowin
#5/5/2024
# Using user-defined functions

import random
def disperse_change(change):
        # converting to value to an integer
        change = round(change* 100)
        print(f"change owed as integer: ${change}")
        #Determine how maney dollars are neeeded
        num_dollars = change // 100
        change = change - (num_dollars * 100)
        #Determine how maney quarters are neeeded
        
        num_quarters = change // 25
        change = change - (num_quarters * 25)
        #Determine how maney dimes are neeeded

        num_dimes = change // 10
        change = change - (num_dimes * 10)
        #Determine how maney nickels  are neeeded

        num_nickels = change // 5
        change = change - (num_nickels * 5)
         #Determine how maney pennies   are neeeded

        num_pennies = change

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
                
def main():
    #Generate the amount owed
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${amount_owed: .2f}")
    # variable to represent money put into machine
    money_in = float(input("How much cash will you put in the self-checkout? "))
    # Calculate change owed to customer
    change =  money_in -  amount_owed
    print(f"change is: ${change: .2f}")

    #call the disperse_change function
    disperse_change(change)
    
    
#Call the main function
main()
