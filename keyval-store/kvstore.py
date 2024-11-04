import os
import json

import argparse

class KeyValueStore:
    def __init__(self, fileName='data.json'):
        self.fileName = fileName
        self.store = self.readFromFile()

    def readFromFile(self):
        if os.path.exists(self.fileName):
            try:
                with open(self.fileName, 'r') as file:
                    return json.load(file)
            except json.JSONDecodeError:
                print(f"Warning: Could not decode the JSON file {self.fileName}. Initializing empty store.")
                return {}
        else:
            return {}
    
    def writeToFile(self):
        with open(self.fileName, 'w') as file:
            json.dump(self.store, file, indent=4)
            
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

# # CLI setup
# def main():
#     parser = argparse.ArgumentParser(description="Key-Value Store CLI")
#     subparsers = parser.add_subparsers(dest="command")

#     # `get` command
#     get_parser = subparsers.add_parser("read", help="Read the value of a key")
#     get_parser.add_argument("key", type=str, help="Key to retrieve")

#     # `create` command
#     create_parser = subparsers.add_parser("create", help="Create the value of a key")
#     create_parser.add_argument("key", type=str, help="Key to create")
#     create_parser.add_argument("value", type=str, help="Value to create")

#     # 'update' command
#     update_parser = subparsers.add_parser("update", help="Update the value of a key")
#     update_parser.add_argument("key", type=str, help="Key to update")
#     update_parser.add_argument("value", type=str, help="Value to update")

#     # `delete` command
#     delete_parser = subparsers.add_parser("delete", help="Delete a key")
#     delete_parser.add_argument("key", type=str, help="Key to delete")

#     args = parser.parse_args()

#     store = KeyValueStore()

#     # Execute commands
#     if args.command == "read":
#         print(store.get(args.key))
#     elif args.command == "create":
#         print(store.insert(args.key, args.value))
#     elif args.command == "update":
#         print(store.update(args.key, args.value))
#     elif args.command == "delete":
#         print(store.delete(args.key))
#     else:
#         parser.print_help()

# if __name__ == "__main__":
#     main()
