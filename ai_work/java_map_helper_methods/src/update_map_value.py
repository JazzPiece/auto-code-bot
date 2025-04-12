class MapHelper:
    @staticmethod
    def update_value(map, key, value):
        if key in map:
            map[key] = value

map = {'a': 1, 'b': 2}
MapHelper.update_value(map, 'b', 3)
print(map)