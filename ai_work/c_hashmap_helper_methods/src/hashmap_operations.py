def create_hashmap():
    return {}

def insert_item(hashmap, key, value):
    hashmap[key] = value

def get_item(hashmap, key):
    return hashmap.get(key)

def delete_item(hashmap, key):
    if key in hashmap:
        del hashmap[key]

def update_item(hashmap, key, value):
    if key in hashmap:
        hashmap[key] = value

def clear_hashmap(hashmap):
    hashmap.clear()

def print_hashmap(hashmap):
    for key, value in hashmap.items():
        print(f'{key}: {value}')