class MapHelper:
    @staticmethod
    def remove_key_value_pair(map, key):
        if key in map:
            del map[key]

map = {'a': 1, 'b': 2, 'c': 3}
MapHelper.remove_key_value_pair(map, 'b')
print(map)