class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, value):
        node = Node(value, self.head)
        self.head = node

    def insert_at_end(self, value):
        if self.head is None:
            self.head = Node(value, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(value, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        counter = 0
        itr = self.head
        while itr:
            counter += 1
            itr = itr.next

        return counter
    
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next

        counter = 0
        itr = self.head

        while itr:
            if counter == index - 1:
                itr.next = itr.next.next 
                break 
            
            itr = itr.next
            counter += 1

    def insert_at(self, index, value):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_beginning(value)
            return
        
        counter = 0
        itr = self.head

        while itr:
            if counter == index - 1:
                node = Node(value, itr.next)
                itr.next = node
                break

            itr = itr.next
            counter =+ 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
          
        if self.head.value == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
        
        itr = self.head
        while itr:
            if itr.value == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break 
            
            itr = itr.next

    def remove_by_value(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.value == value:
                itr.next = itr.next.next
                break
            itr = itr.next

        
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        itr = self.head 
        # itr is a variable and stands for iteration
        llstr = ""
        # llstr stands for linked list string 

        while itr:
            llstr += str(itr.value) + "-->"
            itr = itr.next

        print(llstr)


ll = LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
ll.insert_after_value("mango","apple")
ll.print()
ll.remove_by_value("orange")
ll.print()
ll.remove_by_value("figs")
ll.print()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print()




# Add the following two methods 

# def insert_after_value(self, data_after, data-to-insert)
# Search for first occurence of data_after value in the linked list
# Now insert data_to_insert after data_after_node

#def remove_by_value(self, data)
# Remove first node that contains data
