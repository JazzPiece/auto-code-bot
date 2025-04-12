class MapHelper:
    @staticmethod
    def remove_key(map, key):
        if key in map:
            del map[key]

    @staticmethod
    def get_keys(map):
        return map.keys()

    @staticmethod
    def get_values(map):
        return map.values()

    @staticmethod
    def merge_maps(map1, map2):
        return {**map1, **map2}

    @staticmethod
    def clear_map(map):
        map.clear()