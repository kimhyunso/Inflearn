class Node(object):
    def __init__(self, value = 0, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

class BrowserHistory(object):
    def __init__(self, homepage):
        self.head = self.current = Node(value=homepage)
    
    def visit(self, url):
        self.current.next = Node(value=url, prev=self.current)
        self.current = self.current.next
        return None
    
    def back(self, steps):
        while steps > 0 and self.current.prev != None:
            steps -= 1
            self.current = self.current.prev
        return self.current.value
    
    def forward(self, steps):
        while steps > 0 and self.current.next != None:
            steps -= 1
            self.current = self.current.next
        return self.current.value
    

