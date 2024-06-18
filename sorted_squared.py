def sorted_squared(array):
    #write code here.make sure to return desired array
    
    array_squared = [x**2 for x in array]
    n = len(array_squared)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n-i-1):
            if array_squared[j] > array_squared[j+1]:
                array_squared[j], array_squared[j+1] = array_squared[j+1], array_squared[j]
                swapped = True
        if not swapped:
            break
    
    print(array_squared)
    
    return array_squared

sorted_squared([-3, 2, 4, 6])