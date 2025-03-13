import pandas as pd

# Create a dataframe for the periodic table elements
data = {
    'symbol': ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne'],
    'name': ['Hydrogen', 'Helium', 'Lithium', 'Beryllium', 'Boron', 'Carbon', 'Nitrogen', 'Oxygen', 'Fluorine', 'Neon'],
    'atomic_number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'atomic_mass': [1.008, 4.0026, 6.94, 9.0122, 10.81, 12.011, 14.007, 15.999, 18.998, 20.180],
}

periodic_table = pd.DataFrame(data)
print(periodic_table)