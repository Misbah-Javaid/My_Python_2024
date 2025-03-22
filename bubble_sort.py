def bubble_sort(array_number):
    n = len(array_number)
    # Swipe through all the numbers in the array
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            # Traverse the array of numbers from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if array_number[j] > array_number[j+1]:
                array_number[j], array_number[j+1] = array_number[j+1], array_number[j]
                swapped = True
        if (swapped == False):
            break

# Test code

def print_values(arrays):
    for value in arrays:
        print(value, end = " ")

if __name__ == "__main__":
    array_of_numbers = [64, 34, 25, 12, 22, 0, 1, 11, 90]
    bubble_sort(array_of_numbers)
    print(array_of_numbers)
    
            
                    
            
    