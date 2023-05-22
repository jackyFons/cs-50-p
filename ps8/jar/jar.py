class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        cookies = "🍪" * self._size
        return cookies


    def deposit(self, n):
        if self._size + n > 12:
            raise ValueError
        else:
            self._size += n

    def withdraw(self, n):
        if self._size - n < 0:
            raise ValueError
        else:
            self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size