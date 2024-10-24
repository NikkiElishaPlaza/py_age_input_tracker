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
    getting_user_input.append((get_user_name, get_user_age)) 

    while True:
# After every input, will ask the user if want to input another entry.
        print("Thank you for using user name and age tracker!")
        break

    user_choice = input("Would you like to input again? (yes/no): ")

#   When the user responded “No”, display the name and age of the oldest person. Use the array in checking who is the oldest.
    if user_choice == "no":
            print("Here are all the data inputted: ")
    
            for person in getting_user_input:
                print(f"{person[0]:<20} {person[1]:<10}")

            oldest_person = getting_user_input[0]  # Assuming the first input is the oldest
            for person in getting_user_input:
                if person[1] > oldest_person[1]:  # Compare ages to find the oldest
                    oldest_person = person

            print(f"The oldest person is {oldest_person[0]} with {oldest_person[1]} years of age." "\nThank you for using user name and age tracker!" )
            break

#   When “Yes”, will ask the user again for input. Doing it until the user respond “No”. 
    elif user_choice == "yes":
        continue

    else:
        #Error message
        error = input("Invalid choice, please enter 'yes' or 'no': ")

        if error == "no":
            break

        elif error == "yes":
            continue
        