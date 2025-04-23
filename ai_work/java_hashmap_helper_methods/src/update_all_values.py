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

    def update_all_values(self, new_value):
        for key in self.hash_map:
            self.hash_map[key] = new_value

# Example usage:
# h = HashMapHelper()
# h.put('key1', 'value1')
# h.put('key2', 'value2')
# h.update_all_values('new_value')
# print(h.get('key1'))
# print(h.get('key2'))