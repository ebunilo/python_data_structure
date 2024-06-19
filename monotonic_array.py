def monotonic_array(array):
    """
    Determines if an array is monotonic (either increasing or decreasing).

    Args:
        array (list): A list of integers.

    Returns:
        bool: True if the array is monotonic, False otherwise.
    """
    n = len(array)
    if n <= 2:
        return True
    
    first = 0
    last = len(array)-1
    
    # Check if the array is monotonic increasing
    if array[first] < array[last]:
        for i in range(n-1):
            if array[i] > array[i+1]:
                return False
    
    # Check if the array is monotonic decreasing
    elif array[first] > array[last]:
        for i in range(n-1):
            if array[i] < array[i+1]:
                return False
    
    # Check if all the values are equal
    else: 
        if array[first] == array[last]:
            for i in range(n-1):
                if array[i] != array[i+1]:
                    return False
    
    return True
    
 
print(monotonic_array([10, 9, 7, 5, 4, 3]))
    

