# This script will perform a simulation of a quantum system using the QuTiP library

import numpy as np
import matplotlib.pyplot as plt
from qutip import basis, qeye, destroy, mesolve

# Parameters
N = 5  # number of quantum states
a = destroy(N)
H = a.dag() * a  # Hamiltonian

# Initial state
psi0 = basis(N, 0)

# Time evolution
tlist = np.linspace(0, 10, 100)
result = mesolve(H, psi0, tlist, [], [a.dag() * a])

# Plot results
plt.plot(tlist, result.expect[0])
plt.xlabel('Time')
plt.ylabel('Occupation probability')
plt.title('Quantum System Dynamics')
plt.show()