# Creating a program that ask user to input name and age.
# Set definition of valid name and valid age. 

getting_user_input = []

print("Welcome to user name and age tracker!")

while True:
    while True:
            get_user_name = input("Kindly enter a name: ")

            #Check if the user input contain alphabets only and not numbers
            if get_user_name.isalpha():
                break
            # Print error message when the input is not valid. 
            else:
                print(f"Kindly enter a valid name that contains letters and not numbers.")
    
    while True:
        try:
            get_user_age = int(input("Kindly enter their age: "))
            break
        # Print error message when the input is not valid. 
        except:
            print("Boss, error. Kindly enter a valid answer.")

# Store all the collected information into array. 
    while True:
# After every input, will ask the user if want to input another entry.
        print("Thank you for using user name and age tracker!")
        break

    user_choice = input("Would you like to input again? (yes/no) ")

#   When “Yes”, will ask the user again for input. Doing it until the user respond “No”. 
    if user_choice == "yes":
        print(getting_user_input)
#   When the user responded “No”, display the name and age of the oldest person. Use the array in checking who is the oldest.
    else: 
        user_choice == "no"