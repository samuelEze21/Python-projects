class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.size() == 0

    def enqueue_element(self, element):
        self.queue += [element]

    def peek_element(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0]

    def size(self):
        count = 0
        for _ in self.queue:
            count += 1
        return count

    def dequeue_remove_element(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        first_element = self.queue[0]
        self.queue = self.queue[1:]
        return first_element

    def remove_element(self, element):
        if self.is_empty():
            raise IndexError("Queue is empty")

        new_queue = []
        found = False
        for item in self.queue:
            if item == element and not found:
                found = True
            else:
                new_queue += [item]

        self.queue = new_queue


    def front(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[0]  # Return the first element without removing it



