def add_elements(s, elements):
    s.update(elements)
    return s

s = {1, 2, 3}
print(add_elements(s, {4, 5, 6}))