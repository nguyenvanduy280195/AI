class Stack():
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item, items = None):
        if items == None:
            self.items.append(item)
        else:
            for i in items:
                self.items.insert(0, i)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[self.size()-1]

    def size(self):
        return len(self.items)