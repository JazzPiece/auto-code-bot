class MapHelper:
    @staticmethod
    def add_key_value_pair(map, key, value):
        map[key] = value

    @staticmethod
    def add_key_value_pairs(map, key_value_pairs):
        map.update(key_value_pairs)

    @staticmethod
    def add_multiple_key_value_pairs(map, key_value_pairs):
        map.update(key_value_pairs)

    @staticmethod
    def filter_keys(map, keys_to_keep):
        return {k: v for k, v in map.items() if k in keys_to_keep}

    @staticmethod
    def filter_values(map, values_to_keep):
        return {k: v for k, v in map.items() if v in values_to_keep}

    @staticmethod
    def get_common_keys(map1, map2):
        return set(map1.keys()) & set(map2.keys())

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

    @staticmethod
    def remove_keys(map, keys_to_remove):
        for key in keys_to_remove:
            if key in map:
                del map[key]

    @staticmethod
    def remove_key_value_pair(map, key):
        if key in map:
            del map[key]

    @staticmethod
    def remove_value(map, value):
        keys_to_remove = [k for k, v in map.items() if v == value]
        for key in keys_to_remove:
            del map[key]

    @staticmethod
    def update_value(map, key, value):
        if key in map:
            map[key] = value