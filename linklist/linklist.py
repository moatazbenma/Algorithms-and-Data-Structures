# Node class for individual elements in the linked list
class Node:
    def __init__(self, data):
        self.data = data  # This holds the data of the node
        self.next = None  # This points to the next node (initially None)

# LinkedList class to manage the nodes
class LinkedList:
    def __init__(self):
        self.head = None  # This is the start of the list (initially empty)

    # Method to add a node at the end of the list
    def add_node(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if self.head is None:  # If the list is empty, make this the first node
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Move to the last node
                current = current.next
            current.next = new_node  # Add the new node at the end

    # Method to delete a node by its value
    def delete_node(self, data):
        if self.head is None:  # If the list is empty
            print("List is empty.")
            return
        if self.head.data == data:  # If the node to delete is the first one
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:  # Search for the node
            current = current.next
        if current.next is None:  # If node wasn't found
            print(f"Node with value '{data}' not found.")
        else:
            current.next = current.next.next  # Bypass the node to delete it

    # Method to print the entire list
    def print_list(self):
        current = self.head
        while current:  # Traverse each node
            print(current.data, end=" -> ")
            current = current.next
        print("None")  # Indicates the end of the list

# Example usage
my_list = LinkedList()
my_list.add_node("Node 1")
my_list.add_node("Node 2")
my_list.add_node("Node 3")

print("Initial list:")
my_list.print_list()

my_list.delete_node("Node 2")

print("After deleting 'Node 2':")
my_list.print_list()
