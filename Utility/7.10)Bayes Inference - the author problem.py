#!/usr/bin/env python3
"""
Attribuzione autore (Hamilton = 1 / Madison = 0) con regressione logistica
bayesiana (PyMC + MCMC) e visualizzazione delle *chain* in uscita.

ESEMPIO
    python3 bayes_mcmc_author_trace.py upon_rates.csv
"""

import os, warnings, argparse, sys, numpy as np, pandas as pd
import matplotlib.pyplot as plt, pymc as pm, arviz as az

# ── sopprime l’avviso g++ se non hai il compilatore ────────────────────────
os.environ["PYTENSOR_FLAGS"] = "cxx="
warnings.filterwarnings("ignore", category=RuntimeWarning)

SEED  = 42
RNG   = np.random.default_rng(SEED)
LABEL = {"Hamilton": 1, "Madison": 0}

def load_data(path:str):
    df = pd.read_csv(path)
    if not {"author","rate"}.issubset(df.columns):
        sys.exit("csv privo di colonne author/rate")
    df = df[df["author"].isin(LABEL)]
    return df["rate"].to_numpy(), df["author"].map(LABEL).to_numpy()

def fit_mcmc(x,y):
    with pm.Model() as mdl:
        α = pm.Normal("α", 0, 5)
        β = pm.Normal("β", 0, 5)
        p = pm.Deterministic("p", pm.math.sigmoid(α + β * x))
        pm.Bernoulli("obs", p=p, observed=y)
        trace = pm.sample(
            draws      = 3000,
            tune       = 1000,
            target_accept = .95,
            random_seed   = SEED,
            progressbar   = True  # mostra il progresso live
        )
    return trace

def posterior_p(trace, rate):
    α = trace.posterior["α"].values.ravel()
    β = trace.posterior["β"].values.ravel()
    return 1 / (1 + np.exp(-(α + β * rate)))   # P(Hamilton | rate) per campione

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    args = ap.parse_args()

    x, y = load_data(args.csv)
    trace = fit_mcmc(x, y)

    # ── visualizza subito l’andamento delle chain α e β ────────────────────
    az.plot_trace(trace, var_names=["α","β"])
    plt.tight_layout()
    plt.show()

    try:
        rate = float(input("Rate del documento sconosciuto: ").strip())
    except ValueError:
        sys.exit("numero non valido")

    p_smpl = posterior_p(trace, rate)
    ph     = p_smpl.mean()
    pmad   = 1 - ph

    print(f"\nRate inserito: {rate}")
    print(f"P(Hamilton | rate): {ph:.5f}")
    print(f"P(Madison  | rate): {pmad:.5f}")

    # ── grafico Bernoulli per la previsione ────────────────────────────────
    preds   = RNG.binomial(1, p_smpl, size=p_smpl.size)
    counts  = np.bincount(preds, minlength=2) / preds.size
    fig, ax = plt.subplots()
    ax.bar(["Madison", "Hamilton"], counts, width=0.4)
    ax.set_ylabel("Probabilità")
    ax.set_title("Distribuzione Bernoulliana delle predizioni")
    for i, v in enumerate(counts):
        ax.text(i, v + 0.01, f"{v:.3f}", ha="center")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
