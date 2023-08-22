class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None


    def print_forward(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.head
        llstr = ""
        
        while itr:
            llstr += str(itr.value) + "-->"
            itr = itr.next

        print(llstr)


    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next

        return itr


    def print_backward(self):
        if self.head is None:
            print("Linked List is empty")
            return

        itr = self.get_last_node()
        llstr = ""

        while itr:
            llstr += str(itr.value) + "<--"
            itr = itr.prev

        print(llstr)


    def insert_at_beginning(self, value):
        new_node = Node(value, self.head)
        self.head.prev = new_node
        self.head = new_node


    def insert_at_end(self,value):
        if self.head is None:
            self.head = Node(value, None, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(value, None, itr)


    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


    def get_length(self):
        if self.head is None:
            return 0
        
        itr = self.head
        counter = 0

        while itr:
            counter += 1
            itr = itr.next

        return counter 


    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        itr = self.head
        counter = 0

        while itr:
            if counter == index - 1:
                itr.next = itr.next.next
                itr.next.prev = itr
                break

            counter += 1
            itr = itr.next


    def insert_at(self, index, value):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            new_node = Node(value, self.head)
            self.head.prev = new_node
            self.head = new_node

        if index == self.get_length() - 1:
            self.insert_at_end(value)
        
        itr = self.head
        counter = 0

        while itr:
            if counter == index - 1:
                itr.next = Node(value, itr.next, itr.prev)
                break
            itr = itr.next
            counter += 1


    def insert_after_value(self, value_after, value_to_insert):
        if self.head.value == value_after:
            new_node = Node(value_to_insert, self.head.next, self.head)
            self.head.next.prev = new_node
            self.head.next = new_node
            return

        itr = self.head

        while itr:
            if itr.value == value_after:
                new_node = Node(value_to_insert, itr.next, itr)
                itr.next.prev = new_node
                itr.next = new_node
                break

            itr = itr.next


    def remove_by_value(self, value):
        if self.head.value == value:
            self.head = self.head.next
            self.head.prev = None
            return
        
        itr = self.head

        while itr.next:
            if itr.next.value == value:
                if itr.next.next is None:
                    itr.next = None
                else:
                    itr.next = itr.next.next
                    itr.next.prev = itr
                break
            
            itr = itr.next




ll = DoublyLinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print_forward()
ll.print_backward()
ll.insert_after_value("mango","apple")
ll.remove_at(2)
ll.print_forward()
ll.print_backward()
ll.remove_by_value("orange")
ll.print_forward()
ll.print_backward()
ll.remove_by_value("figs")
ll.print_forward()
ll.print_backward()
ll.remove_by_value("banana")
ll.remove_by_value("mango")
ll.remove_by_value("apple")
ll.remove_by_value("grapes")
ll.print_forward()
ll.print_backward()

        
