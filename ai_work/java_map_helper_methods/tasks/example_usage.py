from map_helper import MapHelper

# Example usage of the MapHelper class
map1 = {'a': 1, 'b': 2, 'c': 3}
map2 = {'d': 4, 'e': 5}

print("Initial map1:", map1)
print("Initial map2:", map2)

MapHelper.remove_key(map1, 'b')
print("Map1 after removing 'b':", map1)

keys = MapHelper.get_keys(map2)
print("Keys of map2:", keys)

values = MapHelper.get_values(map1)
print("Values of map1:", values)

merged_map = MapHelper.merge_maps(map1, map2)
print("Merged map:", merged_map)

MapHelper.clear_map(map2)
print("Map2 after clearing:", map2)