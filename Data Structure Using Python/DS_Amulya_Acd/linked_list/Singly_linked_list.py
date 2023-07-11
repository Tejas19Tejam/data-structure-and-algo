# Creating a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


# Creating a linked list
class Linked_list:
    def __init__(self):
        self.head = None

    #     Let's check linked list is empty or not if not the print the list
    #     Program For traversing the list
    def print_list(self):
        if self.head is None:  # check linked list is empty or not
            print("Linked list is empty ")
        else:
            n = self.head
            while n is not None:
                print(n.data, "---->", end=" ")
                n = n.ref

    # Adding new node at the begining
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    #   Adding newly created node at the end of linked list
    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    # Adding newly created node after the given node (i.e x) of linked list
    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        if n is None:
            print("Node is not present in linked list ")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    # Adding newly created node before the given node (i.e x) of linked list

    def add_before(self, data, x):
        if self.head is None:
            print("Link is empty")
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                if n.ref.data == x:
                    break
                n = n.ref
            if n.ref is None:
                print("Node is not present in linked list ")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node

    def insert_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Linked list is not empty")

    # delete the first node of the linked list

    def rm_begin(self):
        if self.head is None:
            print("You are removing from an empty list ")
        else:
            self.head = self.head.ref

    # delete the last node of the linked list

    def rm_last(self):
        if self.head is None:
            print("You are removing from an empty list ")

            '''if the linked list contain only one node'''
        elif self.head.ref is None:
            self.head = None


        else:
            n = self.head
            '''Go to the second last node
            change the ref to none '''
            while n.ref.ref is not None:
                # print(n.ref.ref)
                n = n.ref
            # print(n.ref.ref)
            n.ref = None

    #  delete any node by value

    def rm_given(self, remove_node):
        if self.head is None:
            print("Linked list is empty,we can't delete")
        else:
            ''' If head is equal to remove node '''
            if self.head.data == remove_node:
                self.head = self.head.ref
                '''calling print_list methode'''
                # ll1.print_list()
                '''Printing one blank line '''
                # print()
                print(f'{remove_node} is deleted from the linked list ')

            else:
                n = self.head
                while n.ref is not None:
                    if n.ref.data == remove_node:
                        n.ref = n.ref.ref
                        break

                    else:
                        n = n.ref

                if n.ref is None:
                    print(f'{remove_node} is not present in the linked list ')


# DRIVER CODE

if __name__ == '__main__':
    # insertion operations

    ll1 = Linked_list()
    ll1.add_begin(20)
    ll1.add_begin(30)
    ll1.add_before(501, 20)
    ll1.add_begin(70)
    ll1.add_after(800, 20)
    ll1.add_end(40)
    # ll1.insert_empty(50)
    # ll1.insert_empty(70)

    # deletion operation
    ll1.print_list()
    print()
    # ll1.rm_begin()
    ll1.rm_given(2345)
    print()
    ll1.print_list()
