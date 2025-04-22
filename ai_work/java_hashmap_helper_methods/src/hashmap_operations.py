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

# Example usage:
# h = HashMapHelper()
# h.put('key1', 'value1')
# print(h.get('key1'))
# print(h.contains_key('key1'))
# h.remove('key1')
# print(h.contains_key('key1'))