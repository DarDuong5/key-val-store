import os
import json

class KeyValueStore:
    def __init__(self, fileName='data.json'):
        self.fileName = fileName
        self.store = {}
    
    def writeToFile(self):
        with open(self.fileName, 'w') as f:
            json.dump(self.store, f)

    def insert(self, key, value):
        self.store[key] = value
        self.writeToFile()
    
    def get(self, key):
        try:
            return self.store.get(key)
        except Exception as e:
            print(f"Key {e} does not exist")

    def update(self, key, value):
        try:
            self.store[key] = value
            self.writeToFile()
        except Exception as e:
            print(f"Cannot find the key to update: {e}")
    
    def delete(self, key):
        try:
            del self.store[key]
            self.writeToFile()
        except Exception as e:
            print(f"Cannot find find the key to delete: {e}")

dictionary1 = KeyValueStore()

dictionary1.insert("hello", "world")
dictionary1.update("hello", "everyone")
dictionary1.delete()
