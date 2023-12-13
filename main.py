class Flask:

    def __init__(self):
        self.cone = []

    def push(self, symbol):
        self.cone.append(symbol)

    def pop(self):
        popped_symbol = self.cone.pop()
        return popped_symbol

    def count(self):
        return len(self.cone)

    def current(self):
        return self.cone[self.count() - 1]

    def __iter__(self):
        self.index = self.count() - 1
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration()
        result = self.array[self.index]
        self.index -= 1
        return result
