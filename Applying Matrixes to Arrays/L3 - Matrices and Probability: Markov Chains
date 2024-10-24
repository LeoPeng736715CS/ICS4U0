def mmult(P, Q):
    R = [[0], [0]]
    
    for i in range(len(Q)):
      tempsum = 0
      for j in range(len(P)):
        tempsum += Q[i][j] * P[j]
      R[i] = tempsum
    
    return R

A = [.3, .7] # prob. Marla is late today
B = [[.7, .3],
     [.9, .1]] # conditional prob. model for Marla's punctuality tomorrow

C = mmult(A, B)
print("On day 1, the probability that Marla will be early the next day is: ", C[0])
print("On day 1, the probability that Marla will be late the next day is: ", C[1])

days = 15
for i in range(2, days):
    C = mmult(C, B)
    print("On day %d, the prob. Marla is early the next day is: %f" % (i, C[0]) )
    print("On day %d, the prob. Marla is late the next day is: %f" % (i, C[1]) )
