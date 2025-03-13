def get_element_properties(symbol):
    # Function to get properties of an element based on its symbol
    properties = periodic_table[periodic_table['symbol'] == symbol]
    return properties

element_symbol = 'C'
element_properties = get_element_properties(element_symbol)
print(element_properties)