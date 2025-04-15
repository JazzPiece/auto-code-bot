class MapHelper:
    @staticmethod
    def filter_values(map, values_to_keep):
        return {k: v for k, v in map.items() if v in values_to_keep}

map = {'a': 1, 'b': 2, 'c': 3}
filtered_map = MapHelper.filter_values(map, [1, 3])
print(filtered_map)