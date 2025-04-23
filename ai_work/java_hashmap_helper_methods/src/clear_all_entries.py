class HashMapHelper:
    def __init__(self):
        self.hash_map = {}

    def put(self, key, value):
        self.hash_map[key] = value

    def get(self, key):
        return self.hash_map.get(key)

    def contains_key(self, key):
        return key in self.hash_map

    def remove(self, key):
        if key in self.hash_map:
            del self.hash_map[key]

    def clear_all_entries(self):
        self.hash_map.clear()

# Example usage:
# h = HashMapHelper()
# h.put('key1', 'value1')
# h.put('key2', 'value2')
# h.clear_all_entries()
# print(h.contains_key('key1'))
# print(h.contains_key('key2'))