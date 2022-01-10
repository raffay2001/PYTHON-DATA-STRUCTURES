from abc import abstractproperty
from array import ArrayType
import ctypes

class Array:
    def __init__(self, n):
        assert n > 0, "Array Size should be greater than Zero"
        self.size = n
        self.elements = (ctypes.py_object*self.size)()
        self.clear(None)

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        assert index >= 0 and index < len(self), "Invalid Index of the Array"
        return self.elements[index]

    def __setitem__(self, index, value):
        assert index >= 0 and index < len(self), "Invalid Index of the Array"
        self.elements[index] = value

    def insert(self, index, value):
        for i in range(self.size-1, index, -1):
            self.elements[i] = self.elements[i-1]
        self.elements[index] = value
    
    def delete(self, index):
        for i in range(index, self.size-1, 1):
            self.elements[i] = self.elements[i+1]
        self.elements[self.size-1] = None

    def traverse(self):
        for i in range(len(self)):
            print(self.elements[i], end="  ")
    
    def clear(self, value):
        for i in range(len(self)):
            self.elements[i] = value
    

class Array2D:
    def __init__(self, rows, cols):
        self.theRows = Array(rows)             
        for i in range(rows):
            self.theRows[i] = Array(cols)
    
    def numrows(self):
        return (len(self.theRows))
    
    def numcols(self):
        return (len(self.theRows[0]))
    
    def clear(self, value):
        for i in range(self.numrows()):
            self.theRows[i].clear(value)
    
    def __getitem__(self, pos):
        assert len(pos) == 2, "Two Subscripts are required"
        i = pos[0] 
        j = pos[1]
        assert i >= 0 and i < self.numrows() and j >= 0 and j < self.numcols(), "Invalid Element Subscript"
        return self.theRows[i][j]
    
    def __setitem__(self, pos, value):
        assert len(pos) == 2, "Two Subscripts are required"
        i = pos[0] 
        j = pos[1]
        assert i >= 0 and i < self.numrows() and j >= 0 and j < self.numcols(), "Invalid Element Subscript"
        self.theRows[i][j] = value

    def traverse(self):
        x = self.numrows()
        y = self.numcols()
        for i in range(x):
            for j in range(y):
                print(self.theRows[i][j], end = " ")
            print()

# a = Array(10)
# a[0] = 120
# a[1] = 125
# a[2] = 250
# a.traverse()
# a.insert(2, 4520)
# print()
# a.traverse()
# a.delete(2)
# print()
# a.traverse()

a = Array2D(3, 3)
