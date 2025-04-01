def is_subset(s1, s2):
    return s1.issubset(s2)

s1 = {1, 2}
s2 = {1, 2, 3, 4}
print(is_subset(s1, s2))