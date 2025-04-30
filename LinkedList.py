class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None and self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None

        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index > self.length - 1:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)
        pre = self.get(index - 1)
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    """
    Implement the find_middle_node method for the LinkedList class.
    Note: this LinkedList implementation does not have a length member variable.
    If the linked list has an even number of nodes, return the first node of the second half of the list.
    Keep in mind the following requirements:
        The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.
        When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.
        The method should return the middle node when the number of nodes is odd or the first node of the second half of the list if the list has an even number of nodes.
        The method should only traverse the linked list once.  In other words, you can only use one loop.
    """

    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    """Has Loop ( ** Interview Question)
    Write a method called has_loop that is part of the linked list class.
    The method should be able to detect if there is a cycle or loop present in the linked list.
    You are required to use Floyd's cycle-finding algorithm (also known as the "tortoise and the hare" algorithm) to detect the loop.
    This algorithm uses two pointers: a slow pointer and a fast pointer. The slow pointer moves one step at a time, 
    while the fast pointer moves two steps at a time. If there is a loop in the linked list, the two pointers will 
    eventually meet at some point. If there is no loop, the fast pointer will reach the end of the list.
    The method should follow these guidelines:
    Create two pointers, slow and fast, both initially pointing to the head of the linked list.
    Traverse the list with the slow pointer moving one step at a time, while the fast pointer moves two steps at a time.
    If there is a loop in the list, the fast pointer will eventually meet the slow pointer. If this occurs, the method should return True.
    If the fast pointer reaches the end of the list or encounters a None value, it means there is no loop in the list. In this case, the method should return False."""

    def has_loop(self):
        fast = self.head
        slow = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def remove_duplicates(self):
        values = []
        previous = None
        current = self.head
        while current is not None:
            if current.value in values:
                previous.next = current.next
            else:
                values.append(current.value)
                previous = current
            current = current.next

    def binary_to_decimal(self):
        num = 0
        current = self.head
        while current is not None:
            num = num * 2 + current.value
            current = current.next
        return num

    def partition_list(self, x):
        if self.head is None and self.length == 0:
            return

        right = Node(0)
        left = Node(0)

        temp_right = right
        temp_left = left

        current = self.head

        while current is not None:

            if current.value < x:
                temp_left.next = current
                temp_left = current
            else:
                temp_right.next = current
                temp_right = current

            current = current.next

        temp_left.next = right.next
        temp_left.next = None








"""Find Kth Node From End ( ** Interview Question)
Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.

Given this LinkedList:

1 -> 2 -> 3 -> 4

If k=1 then return the first node from the end (the last node) which contains the value of 4.

If k=2 then return the second node from the end which contains the value of 3, etc.

If the index is out of bounds, the program should return None.

The find_kth_from_end function should follow these requirements:

The function should utilize two pointers, slow and fast, initialized to the head of the linked list.

The fast pointer should move k nodes ahead in the list.

If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.

The slow and fast pointers should then move forward in the list at the same time until the fast pointer reaches the end of the list.

The function should return the slow pointer, which will be at the k-th position from the end of the list.



This is a separate function that is not a method within the LinkedList class. This means you need to indent the function all the way to the LEFT."""


def find_kth_from_end(linkedlist, k):
    fast = linkedlist.head
    slow = linkedlist.head
    for i in range(k):
        if fast is None:
            return None
        fast = fast.next
    while fast is not None:
        slow = slow.next
        fast = fast.next
    return slow


my_linked_list = LinkedList(1)
my_linked_list.append(1)
my_linked_list.append(0)
my_linked_list.append(1)
my_linked_list.append(1)

my_linked_list.binary_to_decimal()


