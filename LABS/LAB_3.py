# part (a) --> 
from timeit import *
x ='''
def binary_search(array, item):
        beg, end = 0, len(array)-1
        mid = int((beg+end)/2)

        while beg <= end and array[mid] != item:
            if item < array[mid]:
                end = mid - 1
                mid = int((beg+end)/2)
            else:
                beg = mid + 1
                mid = int((beg+end)/2)
        if array[mid] == item:
            return mid
        else:
            return None
binary_search([1,2,3,4,5,6],2)
'''
print('The time for own implementation is: ',timeit(x))
print('The time for built-in implementation is: ', timeit('''arr=[1,2,3,4,5,6]
arr.index(2)'''))

# part (c) --> 
def check_sort(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def take_array():
    array_elements = input(f"Enter the numbers of the array separated by commas: ").split(',')
    array_elements = list(map(lambda x: int(x), array_elements))
    if check_sort(array_elements):
        return array_elements
    else:
        return f'The inputed array is not sorted:('

def insertion_sort(arr):
    for i in range(len(arr)-1):
        if arr[i] < arr[-1]:
            continue
        else:
            temp = arr[i]
            arr[i] = arr[-1]
            arr[-1] = temp
    return arr

def binary_search():
    arr = take_array()
    if check_sort(arr):
        item = int(input(f'enter the number which you want to search in the above array: '))
        if isinstance(arr, list):
            beg, end = 0, len(arr)-1
            mid = (beg+end)//2
            while beg <= end and arr[mid] != item:
                if item < arr[mid]:
                    end = mid - 1
                    mid (beg+end)//2
                else:
                    beg = mid + 1
                    mid = (beg+end)//2
            if item == arr[mid]:
                return mid
            else:
                print(f'Your entered item is not in the array, adding that item in the array: ')
                arr.append(item)
                insertion_sort(arr)
                return arr
        else:
            message = f'The Inputed Array is not Sorted'
            return message
    else:
        return f'The inputed array is not sorted!!'

print(binary_search())