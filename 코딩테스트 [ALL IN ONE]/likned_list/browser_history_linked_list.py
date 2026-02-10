class Node:
    def __init__(self, value, next = None, prev = None):
        self.prev = prev
        self.next = next
        self.value = value

class BrowserHistory(object):
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        new_node = Node(homepage)
        self.head = new_node
        self.tail = new_node

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        new_node = Node(url)
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        return None

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        for _ in range(steps):
            if self.tail.prev == None:
                break
            self.tail = self.tail.prev
        return self.tail.value

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        for _ in range(steps):
            if self.tail.next == None:
                break
            self.tail = self.tail.next
        return self.tail.value


browserHistory = BrowserHistory('leetcode.com')
browserHistory.visit('google.com')
browserHistory.visit('facebook.com')
browserHistory.visit('youtube.com')
print(browserHistory.back(1))
print(browserHistory.back(1))
print(browserHistory.forward(1))

browserHistory.visit('linkedin.com')
print(browserHistory.forward(2))
print(browserHistory.back(2))
print(browserHistory.back(7))



