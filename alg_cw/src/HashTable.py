from Node import ListNode


class HashTable:

    def __init__(self, size):
        self.size = size
        self.cells = [None] * self.size

    def hash(self, key):
        sum = 0
        i = 1
        for pos in range(len(key)):
            sum += ord(key[pos]) * i
            i += 1
        return sum % self.size

    def hash_check(self, key):
        return key % self.size

    def add(self, key, value) -> True:
        pos = self.hash(key)
        if self.cells[pos] is None:
            self.cells[pos] = ListNode(key, value)
            return True
        h = head = self.cells[pos]
        while h:
            if h.key == key:
                h.value = value
                return True
            h = h.next
        self.cells[pos] = ListNode(key, value, head)
        return True

    def search(self, key) -> True:
        pos = self.hash(key)
        if self.cells[pos] is None:
            return False
        head = self.cells[pos]
        while head:
            if head.key == key:
                return True
            head = head.next
        return False

    def remove(self, key) -> True:
        pos = self.hash(key)
        if self.cells[pos] is None:
            return False
        else:
            head = self.cells[pos]
            if head.key == key:
                self.cells[pos] = head.next
                return True
            prev = h = head
            while h:
                if h.key == key:
                    prev.next = h.next
                    return True
                prev, h = h, h.next
