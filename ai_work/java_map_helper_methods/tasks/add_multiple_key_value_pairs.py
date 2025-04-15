class MapHelper:
    @staticmethod
    def add_multiple_key_value_pairs(map, key_value_pairs):
        map.update(key_value_pairs)

map = {'a': 1, 'b': 2}
MapHelper.add_multiple_key_value_pairs(map, {'c': 3, 'd': 4})
print(map)