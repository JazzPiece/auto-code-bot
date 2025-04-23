class HashMapHelper:
    def __init__(self):
        self.hash_map = {}

    def add_key_value_pairs(self, key_value_pairs):
        for key, value in key_value_pairs.items():
            self.hash_map[key] = value

# Example usage:
# h = HashMapHelper()
# h.add_key_value_pairs({'key1': 'value1', 'key2': 'value2'})
# print(h.get('key1'))
# print(h.get('key2'))