# Creating a program that ask user to input name and age.
# Set definition of valid name and valid age. 

getting_user_input = []

print("Welcome to user name and age tracker!")

while True:
    get_user_name = input("Kindly enter a name: ")

    

# Print error message when the input is not valid. 
# Store all the collected information into array. 
# After every input, will ask the user if want to input another entry. 
#   When “Yes”, will ask the user again for input. Doing it until the user respond “No”. 
#   When the user responded “No”, display the name and age of the oldest person. Use the array in checking who is the oldest.