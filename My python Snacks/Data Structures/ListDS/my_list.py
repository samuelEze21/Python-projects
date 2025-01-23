class MyList:
    def __init__(self):
        self.size = 0
        self.items = []

    def append_element(self, element):
        self.items += [element]
        self.size += 1


    def get_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.items[index]



    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        self.items = self.items[:index] + [element] + self.items[index:]



    def remove(self, element):
        if element not in self.items:
            raise ValueError("Element not found in list")

        new_items = []
        found = False
        for item in self.items:
            if item == element and not found:
                found = True  # Skip the first occurrence
            else:
                new_items += [item]  # Add the item to the new list

        self.items = new_items


    def pop(self, index=None):
        if self.is_empty():
            raise IndexError("Pop from empty list")
        if index is None:
            index = self.size - 1
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")

        element = self.items[index]
        self.items = self.items[:index] + self.items[index + 1:]
        return element


    def get_list_size(self):
        if self.size == 0:
            raise ValueError("Empty list")

        return self.size



    def is_empty(self):
        return self.size == 0
