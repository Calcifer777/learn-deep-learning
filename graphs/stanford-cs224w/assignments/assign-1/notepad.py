# %%
# https://www.youtube.com/watch?v=reTP7XAJztU

# %%
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import eig

# %%
G = nx.Graph()
for i in range(1, 4):
  G.add_node(i)
G.add_edge(1, 2)
G.add_edge(1, 3)
G.add_edge(3, 2)
G.add_edge(3, 4)
nx.draw(G, with_labels=True, font_weight='bold')

# %%

A = np.array([
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0],
])

D = np.diag([2, 2, 3, 1])
D_inv = np.linalg.matrix_power(D, -1)
# %%
M =  (D_inv @ A)

# %%
r = np.array([0, 0, 1, 0])

# %%
def ply(m, r, n=1):
  scores =  r @ np.linalg.matrix_power(m, n)
  return scores / np.linalg.norm(scores)

# %%
x = list(range(100))
vectors = np.array([ply(M, r, n=n) for n in x])
max_steps_display = 25
plt.plot(x[:max_steps_display], vectors[:max_steps_display])
plt.legend(["1", "2", "3", "4"])
print(f"Limiting distribution: {vectors[-1]}")

# %%
eig_val, eig_vec_l, eig_vec_r = eig(M, left=True)

unit_eig_val_idx = np.abs(eig_val - 1) <= 1e-5
unit_eig_vec = eig_vec_l[:, unit_eig_val_idx].flatten()
print(f"Unit eigenvecor: {unit_eig_vec}")

# %%
