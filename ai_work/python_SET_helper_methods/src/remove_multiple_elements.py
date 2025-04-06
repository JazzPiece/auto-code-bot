def remove_multiple_elements(s, elements):
    s.difference_update(elements)
    return s

s = {1, 2, 3, 4, 5}
print(remove_multiple_elements(s, {4, 5}))