import numpy as np

def bubble_sort(array):
    n = len(array)
    for i in range (n-1):
        for j in range(0,n-1-i):
            if array[j] > array [j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
            

if __name__ == "__main__":
    numbers = [8,5,2,7]
    array = np.array(numbers)
    array_sorted = bubble_sort(array)
    print(array_sorted)