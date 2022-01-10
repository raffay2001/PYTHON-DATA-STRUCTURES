# first creating the class Node which holds its data and pointer to the next node 
class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


# now creating a class called LinkedList which will keep track of all the Nodes 
class LinkedList:
    def __init__(self):
        self.head = None

    
    # method to insert a node at the beginning of the Linked List 
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    
    # method to insert a node at the end of the Linked List 
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            
            itr.next = Node(data, None)
    
    # method to insert a node at the given index of the Linked List 
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Linked List Index Out of Range")
        
        # for inserting at the head 
        if index == 0:
            self.insert_at_beginning(data)
            return
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    node = Node(data, itr.next)
                    itr.next = node
                    break
                itr = itr.next
                count += 1
        
    # method to search for a node at the given index of the Linked List 
    def search_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Linked List Index Out of Range")
        
        if index == 0:
            return self.head.data
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index:
                    return itr.data
                itr = itr.next
                count += 1


    
    # method to delete a node from the LinkedList
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Linked List Index Out of Range")
        
        # for deleting the very first node
        if index == 0:
            self.head = self.head.next
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    # method to create a new LinkedList from a list of values
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    
    # method to calculate the length of the Linked List 
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    
    #method to traverse the linkedList.
    def printll(self):
        if self.head is None:
            print(f'The Linked List is Empty.')
            return
        else:
            itr = self.head  # itr --> Node Object
            llstr = ""
            while itr:
                llstr += str(itr.data) + "-->"
                itr = itr.next
            return llstr

l = LinkedList()
l.insert_at_beginning(5)
l.insert_at_beginning(10)
l.insert_at_end(12)
# l.insert_values(['Raffay', 'Ali'])
print(l.printll())
l.insert_at(1, 344)
print(l.printll())
print(l.search_at(34))
# l.remove_at(1)
# print(f'The length of the linked list is: {l.get_length()}')
# print(l.printll())
