def get_compound_formula(compound):
    # Function to get the chemical formula of a compound
    compound_formula = ""
    for char in compound:
        if char.isupper():
            if compound_formula:
                compound_formula += " "
            compound_formula += char
        else:
            compound_formula += char
    return compound_formula

compound_name = "H2O"
compound_formula = get_compound_formula(compound_name)
print(compound_formula)