import sys
names_phone_numbers = {"Misbah": "0432675568", "Aysha": "602235", "Maryam": 2235}

for detail in names_phone_numbers:
    print("Name:", detail, "& Phone Number:", names_phone_numbers[detail])
    
# Insert values in dictionary
while True:
    new_name = input("Enter name: ")
    if new_name == "end":
        print(names_phone_numbers.items())
        break
    else:
        new_number = input("Enter number: ")
        names_phone_numbers.update({new_name:new_number})
        
print(names_phone_numbers.items())        
print(names_phone_numbers.items())   
print(names_phone_numbers.keys())
print(names_phone_numbers.values()) 
 
