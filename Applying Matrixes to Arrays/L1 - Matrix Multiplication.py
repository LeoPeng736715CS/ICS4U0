import numpy as np

Q = np.array([
    [0.5, 1.4, 1],
    [1, 2, 0.5]
])

P = np.array([
    [2.20],
    [3.10],
    [2.60]
])

total_spent = Q @ P  

I_3x3 = np.eye(3)

Q_expanded = np.vstack([Q, np.zeros((1, 3))]) 

Q_identity_product_corrected = Q_expanded @ I_3x3

ken_spent = total_spent[0, 0]
