class MapHelper:
    @staticmethod
    def get_common_keys(map1, map2):
        return set(map1.keys()) & set(map2.keys())

map1 = {'a': 1, 'b': 2, 'c': 3}
map2 = {'b': 4, 'c': 5, 'd': 6}
common_keys = MapHelper.get_common_keys(map1, map2)
print(common_keys)