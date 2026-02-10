# array list
## back, forward => O(1)
## visit => O(n)

# linked list
## back, forward => O(n)
## visit => O(1)

class BrowserHistory(object):
    def __init__(self, homepage):
        self.li = [homepage]
        self.index = 0

    def visit(self, url):
        if self.index == len(self.li) - 1:
            self.li.append(url)
        else:
            for i in range(self.inedx + 1, len(self.li)):
                self.li.pop()
            self.li.append(url)
        self.index += 1
    
    def back(self, steps):
        if self.index - steps < 0:
            self.index = 0
            return self.li[0]
        else:
            ret = self.li[self.index - steps]
            self.index = self.index - steps
            return ret
    
    def forward(self, steps):
        if self.index + steps > len(self.li) - 1:
            ret = self.li[len(self.li) - 1]
            self.index = len(self.li) - 1
            return ret
        else:
            ret = self.li[self.index + steps]
            self.index = self.index + steps
            return ret
        
    