def sorted_squared(array):
    """
    Sorts the squared values of the input array in ascending order. Time complexity = O(n)

    Args:
        array (list): A list of integers.

    Returns:
        list: A new list containing the squares of the numbers in the input array, sorted in non-decreasing order.
    """
    n = len(array)
    # Create a new list to store the squared and sorted values
    squared_sorted = [0] * len(array)

    # Pointers to the start and end of the input array
    start = 0
    end = len(array) - 1

    # Iterate from the end of the array
    for i in reversed(range(n)):
        # Compare the absolute values of the elements at the start and end pointers
        if abs(array[start]) > abs(array[end]):
            # Square the value at the start pointer and store it in the result array
            squared_sorted[i] = array[start] ** 2
            # Move the start pointer to the right
            start += 1
        else:
            # Square the value at the end pointer and store it in the result array
            squared_sorted[i] = array[end] ** 2
            # Move the end pointer to the left
            end -= 1
    print(squared_sorted)
    
    return squared_sorted

sorted_squared([-3, 2, 4, 6])