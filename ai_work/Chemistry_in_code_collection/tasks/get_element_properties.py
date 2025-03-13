import pandas as pd

def get_element_properties(symbol):
    element_properties = periodic_table[periodic_table['symbol'] == symbol]
    return element_properties[['symbol', 'name', 'atomic_number', 'atomic_mass']]

element_symbol = 'C'
element_properties = get_element_properties(element_symbol)
print(element_properties)