import pandas as pd

def get_element_info(symbol):
    element_info = periodic_table[periodic_table['symbol'] == symbol]
    return element_info

element_symbol = 'O'
element_info = get_element_info(element_symbol)
print(element_info)