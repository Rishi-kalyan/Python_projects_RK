class HashTable():
    def __init__(self, size=7):
        self.data_map=[None]*size

    def __has(self, key):
        my_hash=0