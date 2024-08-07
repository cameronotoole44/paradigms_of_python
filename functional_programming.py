# Implement a function that will flatten and sort an array of integers in ascending order, and which adheres to a functional programming paradigm.

# Remember, when writing in a functional style:
# Keep variables immutable
# Write only pure functions
# Remember, functions may be higher order



def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)