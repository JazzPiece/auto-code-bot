class MapHelper:
    @staticmethod
    def remove_value(map, value):
        keys_to_remove = [k for k, v in map.items() if v == value]
        for key in keys_to_remove:
            del map[key]

map = {'a': 1, 'b': 2, 'c': 3}
MapHelper.remove_value(map, 2)
print(map)