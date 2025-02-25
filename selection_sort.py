# Selection sort is a comparison-based selection sorting algorithm

arr_numbers = [64, 25, 12, 22, 11]

# Start from the index 0, select the value at index 0, and
# compare it with the smallest element in the array

#size = len(arr_numbers)
def selection_sort(arr_numbers):
    size = len(arr_numbers)
    for index in range(size - 1):
        minimum_index = index
        for j in range(index + 1, size):
            # Select the minimum element in every iteration
            if arr_numbers[j] < arr_numbers[minimum_index]:
                # swapping the elements to sort the array
                minimum_index = j
        (arr_numbers[index], arr_numbers[minimum_index]) = (arr_numbers[minimum_index], arr_numbers[index])
            
            
        #print(minimum_index)

# Print selection sort
def print_arr_numbers(arr_numbers):
    for value in arr_numbers:
        print(value, end = " ")
    print()    

if __name__ == "__main__":
    arr_numbers = [64, 25, 12, 22, 11]
    print("Values before Sorting")
    print_arr_numbers(arr_numbers)
    selection_sort(arr_numbers)
    print("Values after Sorting")
    print_arr_numbers(arr_numbers)


"""
# Python program for implementation of Selection
# Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
      
        # Assume the current position holds
        # the minimum element
        min_idx = i
        
        # Iterate through the unsorted portion
        # to find the actual minimum
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
              
                # Update min_idx if a smaller element is found
                min_idx = j
        
        # Move minimum element to its
        # correct position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def print_array(arr):
    for val in arr:
        print(val, end=" ")
    print()

if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    
    print("Original array: ", end="")
    print_array(arr)
    
    selection_sort(arr)
    
    print("Sorted array: ", end="")
    print_array(arr) """

