
"""
linear_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
               11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
num1 = 0
for num in range(len(linear_list)+ 1):
    #print(f"Index is:",linear_list.index(num))
    if num == num1:
        print(f"Index is:",linear_list.index(num1)) 

    

for index in range(len(array_elements)):
    print("The value on index {0} is {1}".format(index, array_elements[index]))"""
    
array_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
               11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
array_element = []

target = 5
def linear_search(array_elements, target):
    # Traverse through all the elements
    for index in range(len(array_elements)):
        
        if array_elements[index] == target:
            #print(index)
            return index
            
    return -1    
result = linear_search(array_elements, target)

if result != -1:
    print("Item found at index", result)
else:
    print("Item not found")    

