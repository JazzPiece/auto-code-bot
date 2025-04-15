class MapHelper:
    @staticmethod
    def add_key_value_pair(map, key, value):
        map[key] = value

map = {'a': 1, 'b': 2}
MapHelper.add_key_value_pair(map, 'c', 3)
print(map)