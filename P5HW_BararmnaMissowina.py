#Baramna Missowina

# 5/5/2024

#P5HW

#Use of loops, functions and module import 

# generate_number

import random

def numbers_generate():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def add_numbers(num1, num2):
    return num1 + num2

def subtraction_number(num1, num2):
    return num1 - num2
# list of menu
def main_menu():
    print("Welcome to the Math Quiz")
    print("MAIN MENU")
    print("------------------")
    print("1. Adding Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")
#When/if user enters 1
def main():
    menu_option = ''
    while menu_option != '3':
        main_menu()
        menu_option = input("Please choose an option : ")

        if menu_option == '1':
            num1, num2 = numbers_generate()
            result = add_numbers(num1, num2)
            user_result = int(input(f"Enter answer:\n{num1}\n+ {num2}\n"))

            if user_result == result:
                print("Congratulations!!!! Your answer is correct.")
            else:
                print("Sorry,  guess is too low. " or "Sorry,  guess is too high."  )

         #   When/if user enters 2,
         
        elif menu_option == '2':
            num1, num2 = numbers_generate()
            result = subtraction_number(num1, num2)
            user_result = int(input(f"Enter answer:\n{num1}\n- {num2}\n"))

            if user_result == result:
                print("Congratulations!!!! Your answer is correct.")
            else:
                print("sorry, guess is too low."  or "Sorry,  guess is too high."  )

            #If/when the user enters 3,
            
        elif menu_option == '3':
            print("Thank you for playing...")
            print("bye!")

        else:
            print("Invalid choice. Please enter 1, 2, 3.")

if __name__ == "__main__":
    main()






