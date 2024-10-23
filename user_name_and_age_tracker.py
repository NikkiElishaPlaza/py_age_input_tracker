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
    
<<<<<<< HEAD
    while True:
=======
while True:
>>>>>>> e8516e2eec97371ac1cf04995e81978a11e2a82e
        try:
            get_user_age = int(input("Kindly enter their age: "))
            break
        # Print error message when the input is not valid. 
        except:
            print("Boss, error. Kindly enter a valid answer.")
    


# Store all the collected information into array. 
# After every input, will ask the user if want to input another entry. 
#   When “Yes”, will ask the user again for input. Doing it until the user respond “No”. 
#   When the user responded “No”, display the name and age of the oldest person. Use the array in checking who is the oldest.