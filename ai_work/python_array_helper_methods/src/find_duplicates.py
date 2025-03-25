def find_duplicates(arr):
    unique_elements = set()
    duplicates = []

    for element in arr:
        if element not in unique_elements:
            unique_elements.add(element)
        else:
            duplicates.append(element)

    return list(set(duplicates))