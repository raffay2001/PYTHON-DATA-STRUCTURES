from array import *


# ARRAY CREATION :- 
# from array import *

# arrayName = array(typecode, [Initializers])

# making an array of type integer i.e which holds integers 
array = array('i', [20, 30, 40, 50])

# INSERTION IN THE ARRAY 
# inserting a new element in the array at 0th position 
array.insert(0, 12)

# DELETION FROM THE ARRAY 
# removing an elementk from the array 
array.remove(40)


# TRAVERSING THE ARRAY 
# traversing the whole array anid printing all of its values 
for i in range(len(array)):
    print(array[i])

# SEARCHING FOR A DATA ELEMENT IN THE ARRAY 
# accessing the index of an element in the array 
print(f'The location of the element 30 in the array is: {array.index(30)}')

