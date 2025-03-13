import re

def get_compound_formula(compound):
    return ' '.join(re.findall('[A-Z][a-z]*', compound))

compound_name = "H2O"
compound_formula = get_compound_formula(compound_name)
print(compound_formula)