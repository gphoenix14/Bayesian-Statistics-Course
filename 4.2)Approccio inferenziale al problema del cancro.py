import pymc as pm
import numpy as np
import arviz as az
import matplotlib.pyplot as plt

# ================================
# Parte 1: Inferenza Bayesiana con PyMC
# ================================
with pm.Model() as model:
    # Prior: probabilità che una donna abbia il cancro (1%)
    cancer = pm.Bernoulli("cancer", p=0.01)
    
    # Deterministic: probabilità del test positivo in funzione della presenza del cancro:
    # se cancer == 1 => 0.8, altrimenti 0.096
    p_test = pm.Deterministic(
        "p_test",
        pm.math.switch(pm.math.eq(cancer, 1), 0.8, 0.096)
    )
    
    # Likelihood: osserviamo un test positivo (1)
    test = pm.Bernoulli("test", p=p_test, observed=1)
    
    # Campionamento MCMC: utilizziamo Metropolis (adatto per variabili discrete)
    trace = pm.sample(
        draws=2000,
        tune=1000,
        chains=2,
        step=pm.Metropolis(),
        random_seed=42
    )

# Calcolo della probabilità a posteriori di avere il cancro dai campioni MCMC
posterior_p_cancer = np.mean(trace.posterior["cancer"].values)
print(f"[PyMC] Probabilità a posteriori di cancro: {posterior_p_cancer:.4f}")

# Visualizzazione del trace tramite ArviZ
az.plot_trace(trace, var_names=["cancer"])
plt.show()

# Istogramma manuale per la variabile "cancer"
posterior_vals = trace.posterior["cancer"].values.flatten()
plt.hist(posterior_vals, bins=[-0.5, 0.5, 1.5], density=True, rwidth=0.5)
plt.xlabel("Valore di 'cancer' (0 = no, 1 = sì)")
plt.ylabel("Densità")
plt.title("Distribuzione a posteriori della variabile 'cancer'")
plt.xticks([0, 1])
plt.show()

# ================================
# Parte 2: Simulazione Monte Carlo
# ================================
# Questo blocco simula N individui, assegna il cancro secondo una Bernoulli(p=0.01),
# simula il test in base alla presenza o meno di cancro e stima la probabilità
# di cancro fra coloro che hanno un test positivo.

# Numero di simulazioni
N = 1_000_000

# Simulazione del cancro: 1 se la donna ha il cancro, 0 altrimenti
cancers = np.random.binomial(1, 0.01, size=N)

# Per ciascun individuo, la probabilità che il test risulti positivo:
# se ha il cancro -> 0.8, altrimenti -> 0.096
p_tests = np.where(cancers == 1, 0.8, 0.096)

# Simulazione del test (1 = positivo, 0 = negativo)
tests = np.random.binomial(1, p_tests)

# Calcolo: fra gli individui con test positivo, quale proporzione risulta avere il cancro?
indice_test_positivo = (tests == 1)
posterior_mc = np.sum(cancers[indice_test_positivo]) / np.sum(indice_test_positivo)
print(f"[Monte Carlo] Probabilità stimata di cancro dati test positivi: {posterior_mc:.4f}")

# Istogramma della distribuzione dei test positivi (solo per visualizzazione della variabile "cancer")
plt.hist(cancers[indice_test_positivo], bins=[-0.5, 0.5, 1.5], density=True, rwidth=0.5)
plt.xlabel("Valore di 'cancer' (0 = no, 1 = sì)")
plt.ylabel("Densità")
plt.title("Distribuzione (Monte Carlo) della variabile 'cancer' nei test positivi")
plt.xticks([0, 1])
plt.show()
