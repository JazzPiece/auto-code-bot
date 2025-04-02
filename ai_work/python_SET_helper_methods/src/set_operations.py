def add_element(s, element):
    s.add(element)
    return s

def remove_element(s, element):
    s.discard(element)
    return s

def clear_set(s):
    s.clear()
    return s

def difference_sets(s1, s2):
    return s1.difference(s2)

def intersection_sets(s1, s2):
    return s1.intersection(s2)

def is_subset(s1, s2):
    return s1.issubset(s2)

def symmetric_difference_sets(s1, s2):
    return s1.symmetric_difference(s2)

def union_sets(s1, s2):
    return s1.union(s2)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(add_element(s1, 4))
print(remove_element(s2, 4))
print(clear_set(s1))
print(difference_sets(s1, s2))
print(intersection_sets(s1, s2))
print(is_subset(s1, s2))
print(symmetric_difference_sets(s1, s2))
print(union_sets(s1, s2))