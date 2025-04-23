from hashmap_operations import *

# Test the hashmap operations
hashmap = create_hashmap()
insert_item(hashmap, 'key1', 'value1')
insert_item(hashmap, 'key2', 'value2')

print('Original Hashmap:')
print_hashmap(hashmap)

update_item(hashmap, 'key2', 'updated_value2')
print('\nUpdated Hashmap:')
print_hashmap(hashmap)

print('\nGetting item for key1:')
print(get_item(hashmap, 'key1'))

delete_item(hashmap, 'key1')
print('\nAfter deleting key1:')
print_hashmap(hashmap)

clear_hashmap(hashmap)
print('\nAfter clearing the Hashmap:')
print_hashmap(hashmap)