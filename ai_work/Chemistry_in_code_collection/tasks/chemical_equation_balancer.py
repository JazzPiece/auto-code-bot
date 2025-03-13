```python
# This script will balance a chemical equation

from sympy import symbols, Eq, solve

# Enter the chemical equation in the format 'reactant -> product'
equation = input("Enter the chemical equation: ")

reactant, product = equation.split('->')
reactants = reactant.split('+')
products = product.split('+')

elements = set()
for r in reactants:
    elements.update(r.split())

for p in products:
    elements.update(p.split())

# Create symbols for each element
element_symbols = symbols(' '.join(elements))

# Create equations for each element
element_eqs = []
for element in elements:
    reactant_count = sum([r.count(element) for r in reactants])
    product_count = sum([p.count(element) for p in products])
    element_eqs.append(Eq(element_symbols[elements.index(element)], product_count - reactant_count))

# Solve equations to balance the chemical equation
solution = solve(element_eqs)
balanced_eq = equation
for element, count in zip(elements, solution):
    balanced_eq = balanced_eq.replace(element, str(count))

print(f"Balanced equation: {balanced_eq}")
```