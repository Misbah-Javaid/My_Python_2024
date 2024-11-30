# Break statement

"""while True:
    print("Please type your name: ")
    name = input()
    if name == 'misbah':
        break
    else:
        print('Only misbah allowed')
print("Thank you")

# Continue statement

while True:
    age = int(input())
    if age != 18:
        continue
    print("Hello ! misbah. What is password (It is a fish)")
    password = input()
    if password == "fish":
        break
print('Access granted !')   
"""

# Truthy and Falsey values

name =  ""
while not name:  # if user presses enter then the loop will keep on asking the name
    print("Enter name: ")
    name = input()
print("How many guests will you have?")
numberOfguests = int(input("Enter number of guests: "))
if numberOfguests != 0: # if numberOfguests is also right
    print("Be sure to have enough room for the guests")
print("Done")  

# Write a program, which asks for user input. Until you claim to be Misbah, it should
# not ask for a password, and once you enter the correct password
# it should exit


"""name = ""
password = "starfish"

while name:
    print("Who are you?")
    user_name = input("Please enter your name: ")
    if user_name == name:
        user_password = input("Enter password. (Hint ! fish)")
        if user_password == password:
            break
        
print("Access Granted", name)       """  

       
    
    

