class Queue:
    def __init__(self):
       self.elements = list()
       self.clear()
    
    def __len__(self):
        return len(self.elements)

    def isEmpty(self):
        return len(self) == 0

    # method to add an element to the front of the Queue.
    def enqueue(self, item):
        self.elements.append(item) 
    
    # method to removv an element from the rear of the Queue.
    def dequeue(self):
        if self.isEmpty():
            print("The Queue is Empty.")
            return  
        return self.elements.pop(0)
    
    def first(self):
        return self.elements[0]
    
    def clear(self):
        self.elements.clear()

    def traverse(self):
        print("Front", end=' <--')
        for i in self.elements:
            print(i, end='<--')
        print(" Rear")

q = Queue()
q.enqueue(23)
q.enqueue(43)
q.enqueue(34)
q.traverse()
q.dequeue()
print()
q.traverse()
q.enqueue(45)
q.traverse()
