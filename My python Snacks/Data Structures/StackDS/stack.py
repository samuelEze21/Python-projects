class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def append_element(self, element):
        self.stack += [element]
        self.size += 1

    def peek_element(self):
        if not self.is_empty():
            return self.stack[self.size - 1]
        else:
            raise IndexError('Stack is empty, cannot peek')

    def pop_element(self):
        if not self.is_empty():
            element = self.stack[self.size - 1]
            self.stack = self.stack[:-1]
            self.size -= 1
            return element
        else:
            raise IndexError('Stack is empty, cannot pop')


    def get_size(self):
        count = 0

        for _ in self.stack:
            count += 1

        return count


