class MapHelper:
    @staticmethod
    def remove_keys(map, keys_to_remove):
        for key in keys_to_remove:
            if key in map:
                del map[key]

map = {'a': 1, 'b': 2, 'c': 3}
MapHelper.remove_keys(map, ['a', 'c'])
print(map)