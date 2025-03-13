import pandas as pd

# Add more information to the periodic table dataframe
periodic_table['group'] = ['1', '18', '1', '2', '13', '14', '15', '16', '17', '18']
periodic_table['period'] = ['1', '1', '2', '2', '2', '2', '2', '2', '2', '2']
periodic_table['melting_point_C'] = [0.0, -272.2, 180.5, 1278, 2300, 3550, -210, -218.8, -219.6, -248.6]

print(periodic_table)