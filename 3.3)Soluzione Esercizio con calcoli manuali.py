import matplotlib.pyplot as plt

def main():
    # Dati di base
    pA = 0.05              # P(A): % di clienti davvero interessati
    pB_given_A = 0.90      # P(B|A): Probabilità di dichiarare "Sì" se interessato
    pB_given_notA = 0.10   # P(B|¬A): Probabilità di dichiarare "Sì" se NON interessato

    # Calcoli delle probabilità
    pA_and_B = pA * pB_given_A                    # P(A ∩ B)
    pNotA = 1 - pA                                # P(¬A)
    pNotA_and_B = pNotA * pB_given_notA           # P(¬A ∩ B)
    pB = pA_and_B + pNotA_and_B                   # P(B)

    # Teorema di Bayes: P(A|B)
    pA_given_B = pA_and_B / pB
    pNotA_given_B = 1 - pA_given_B

    # Stampa risultato nel terminale
    print("Probabilità che il cliente sia DAVVERO interessato (A)\n"
          "dato che dichiara di preferire l'Offerta Green (B):")
    print(f" P(A=1|B=1) = {pA_given_B:.4f}  (circa {pA_given_B*100:.2f}%)")
    print(f" P(A=0|B=1) = {pNotA_given_B:.4f}  (circa {pNotA_given_B*100:.2f}%)\n")

    # Plot della distribuzione di Bernoulli
    outcomes = ['Non interessato (A=0)', 'Interessato (A=1)']
    probabilities = [pNotA_given_B, pA_given_B]

    plt.bar(outcomes, probabilities, color=['gray', 'green'])
    plt.ylabel('Probabilità')
    plt.title('Distribuzione Bernoulliana di A dato B')
    for i, v in enumerate(probabilities):
        plt.text(i, v + 0.01, f"{v:.2f}", ha='center', fontweight='bold')
    plt.ylim(0, 1)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Avvio
if __name__ == "__main__":
    main()
