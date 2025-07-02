def searchMinor(array):
    minor = array[0] # first set a variable to find a minor number in array in this case we use the first element of the array
    minor_index = 0 # and the same for your index

    for i in range(1, len(array)): # so to 1 until the end of the array 
        if array[i] < minor: # check if the element is minor then we have
            minor = array[i] # if is we set a new minor
            minor_index = i # and same for the index

    return minor_index # return local of the minor number of the array

def selection_sort(array):
    sort_array = [] # create a new array to put the sort valeus. ASC

    for i in range(len(array)): # in the range of the array
        minor = searchMinor(array) # search a minor element
        sort_array.append(array.pop(minor)) # insert in the sort array end delete from the original array
    return sort_array # return the sorted array

print(selection_sort([5,3,6,2,10])) # Insert numbers here for sort!