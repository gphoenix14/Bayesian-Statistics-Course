# Probabilità estratte dalla tabella
P_A_and_B = 0.05     # P(A ∩ B)
P_B = 0.15           # P(B)
P_A = 0.70           # P(A)

# Calcolo delle probabilità condizionate
P_A_given_B = P_A_and_B / P_B       # P(A|B)
P_B_given_A = P_A_and_B / P_A       # P(B|A)

# Output dei risultati
print(f"P(A|B) = {P_A_given_B:.4f}")
print(f"P(B|A) = {P_B_given_A:.4f}")
