
number_list = [2, 3, 4, 10, 40]

# Binary search using iterative

def binary_search(number_list, target):
    start_index = 0
    last_index = len(number_list) - 1
    mid_index = 0

    while start_index <= last_index:   # 0 <= 4
        mid_index = (start_index + last_index)//2
        # if target number is greater, ignore left half
        if number_list[mid_index] < target:
            start_index = mid_index + 1
        # if x is smaller, ignore right half
        elif number_list[mid_index] > target:   # means x is present in the mid
            last_index = mid_index - 1

        else:
            return mid_index

    return -1

# Run Program

target = 10

result = binary_search(number_list, target)

if result != -1:
    print("Element found on the index: ", result)
else:
    print("Element is not present in the list")

string_list = ["apple", "orange", "banana", "kiwi", "watermelon"]

search_string  = input("Enter string: ")
for i in range(len(string_list)):
    if string_list[i] == search_string:
        print("found")
        exit()
        
print("Not found")
    
