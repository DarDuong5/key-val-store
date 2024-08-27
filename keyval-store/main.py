class KeyValueStore:
    def __init__(self):
        self.store = {}

    def insert(self, key, value):
        self.store[key] = value
    
    def get(self, key):
        try:
            return self.store.get(key)
        except Exception as e:
            print(f"Key {e} does not exist")

    def update(self, key, value):
        try:
            self.store[key] = value
        except Exception as e:
            print(f"Cannot find the key to update: {e}")
    
    def delete(self, key):
        try:
            del self.store[key]
        except Exception as e:
            print(f"Cannot find find the key to delete: {e}")
