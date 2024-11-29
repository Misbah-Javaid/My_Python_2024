name = input("Please enter your name: ")
if name == "Misbah":
    password = input("Enter password: ")
    if name == password:
        age = int(input("Please enter your age: "))
    
        if age < 12:
            print("Access Denied ! you are not", name)
        else:
            print("Hello Misbah ! Welcome")    
     
    else:
        print("Have a nice day")
else:
    print("You are not Misbah !")        
