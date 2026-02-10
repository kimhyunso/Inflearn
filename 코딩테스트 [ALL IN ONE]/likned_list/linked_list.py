class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third
first.value = 6


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value
    
    def insert(self, idx, value):
        new_node = Node(value)
        cur = self.head
        if idx == 0:
            new_node.next = cur
            self.head = new_node
        else:
            prev = cur
            for _ in range(idx):
                prev = cur
                cur = cur.next

            new_node.next = cur
            prev.next = new_node
    def remove(self, idx):
        cur = self.head
        if idx == 0:
            self.head = cur.next
            cur.next = None
        else:
            prev = cur
            for _ in range(idx):
                prev = cur
                cur = cur.next
            prev.next = cur.next
            cur.next = None
    def insert_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)

# print(ll.get(0))
# print(ll.get(1))
# print(ll.get(2))
# print(ll.get(3))

# ll.insert(idx=3, value=9)
# print(ll.get(0))
# print(ll.get(1))
# print(ll.get(2))
# print(ll.get(3))

ll.remove(2)

print(ll.get(0))
print(ll.get(1))
print(ll.get(2))
print(ll.get(3))




