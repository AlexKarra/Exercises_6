# 1

def power(a, b):
    if a <= 0 or b <= 0:
        return -1
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)
    

# 2
        
def binary_search(numbers, num):
    """
    Recursive binary search algorithm to find the index of an integer in a sorted list.

    Args:
        numbers (list): Sorted list of integers.
        num (int): Integer to be searched for.

    Returns:
        int: Index of num in the list if it exists, otherwise -1.
    """
    # Base case: If the list is empty or the element is not in the list, return -1
    
    if len(numbers) == 0:
        return -1

    # Calculate the middle index of the list
    mid = len(numbers) // 2

    # If the middle element is equal to the search element, return its index
    if numbers[mid] == num:
        return mid

    # If the middle element is greater than the search element, search the left half of the list
    elif numbers[mid] > num:
        return binary_search(numbers[:mid], num)

    # If the middle element is less than the search element, search the right half of the list
    else:
        result = binary_search(numbers[mid+1:], num)
        return -1 if result == -1 else mid + 1 + result
