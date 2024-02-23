# This function is in LinkedList class
# Function to insert a new node at the beginning
def push(self, new_data):
 
    # 1 & 2: Allocate the Node &
    # Put in the data
    new_node = Node(new_data)
 
    # 3. Make next of new Node as head
    new_node.next = self.head
 
    # 4. Move the head to point to new Node
    self.head = new_node

# Inserts a new node after the given prev_node.
def insertAfter(self, prev_node, new_data):
 
    # 1. check if the given prev_node exists
    if prev_node is None:
        print("The given previous node must inLinkedList.")
        return
 
    # 2. Create new node &
    # 3. Put in the data
    new_node = Node(new_data)
 
    # 4. Make next of new Node as next of prev_node
    new_node.next = prev_node.next
 
    # 5. make next of prev_node as new_node
    prev_node.next = new_node

# Appends a new node at the end. 
def append(self, new_data):
 
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)
 
        # 4. If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            self.head = new_node
            return
 
        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next
 
        # 6. Change the next of last node
        last.next = new_node
