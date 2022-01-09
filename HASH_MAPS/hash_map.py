class HashTable:
    def __init__(self):
        self.MAX = 100      #we are assuming that our array which holds the values for keys is of the size 100
        self.arr = [None for i in range(self.MAX)]
    
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value
    
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
    
t = HashTable()
t['march 6'] = 1782.0
t['march 4'] = 892.0
t['march 9'] = 178.0
t['march 4'] = 1278.0
print(t.arr)
del t['march 6']
print(t.arr)