class HashMapHelper:
    def __init__(self):
        self.hash_map = {}

    def get_all_keys(self):
        return list(self.hash_map.keys())

# Example usage:
# h = HashMapHelper()
# h.put('key1', 'value1')
# h.put('key2', 'value2')
# print(h.get_all_keys())