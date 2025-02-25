
names = ["Misbah", "Javaid", "Aysha", "Maryam", "Amna"]
phone_numbers = ["0432675568", "090078", "123456", "602235", "3528"]

user_name = input("Enter name: ")

for name in range(len(names)):
    if names[name] == user_name:
        print("Number found", phone_numbers[name])
        exit()
        
print("Not found")        
        
    
    
