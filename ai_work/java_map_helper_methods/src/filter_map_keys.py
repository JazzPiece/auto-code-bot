class MapHelper:
    @staticmethod
    def filter_keys(map, keys_to_keep):
        return {k: v for k, v in map.items() if k in keys_to_keep}

map = {'a': 1, 'b': 2, 'c': 3}
filtered_map = MapHelper.filter_keys(map, ['a', 'c'])
print(filtered_map)