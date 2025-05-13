#!/usr/bin/env python
# bayes_inference_pymc.py
# ------------------------------------------------------------
# Inferenza bayesiana con PyMC e NUTS su ipotesi discrete
# (priori arbitrarie), stampa PDF Prior/Post e grafico.
#
# Avvio (esempio):
#   python bayes_inference_pymc.py --hypotheses ipotesi.csv \
#       --priors priori.csv --observations osservazioni.csv \
#       --sigma 0.5 --draws 5000 --tune 2000
# ------------------------------------------------------------

import argparse, pandas as pd, numpy as np, matplotlib.pyplot as plt
import pymc as pm, arviz as az


# ------------------------------------------------------------
def carica_csv(path: str, n_cols: int) -> pd.DataFrame:
    df = pd.read_csv(path)
    if len(df.columns) != n_cols:
        raise ValueError(f"{path} deve avere {n_cols} colonne, ne ha {len(df.columns)}.")
    return df


# ------------------------------------------------------------
def posteriori_mcmc(h_df: pd.DataFrame,
                    p_df: pd.DataFrame,
                    o_df: pd.DataFrame,
                    sigma: float,
                    draws: int,
                    tune: int,
                    target_accept: float,
                    random_seed: int) -> pd.DataFrame:

    h_df = h_df.rename(columns={h_df.columns[1]: "val"})
    p_df = p_df.rename(columns={p_df.columns[0]: "val",
                                p_df.columns[1]: "prob"})
    merged = h_df.merge(p_df, on="val")
    if merged.empty:
        raise ValueError("Valori numerici di ipotesi e priori non coincidono.")

    mu_vals = merged["val"].to_numpy(float)
    w_prior = merged["prob"].to_numpy(float)
    w_prior /= w_prior.sum()                 # normalizza PDF prior
    obs = o_df.iloc[:, 0].to_numpy(float)

    with pm.Model() as mdl:
        # prior discreta ≈ mistura di Normali con sd infinitesima
        comp = [pm.Normal.dist(mu=m, sigma=1e-6) for m in mu_vals]
        mu = pm.Mixture("mu", w=w_prior, comp_dists=comp)
        pm.Normal("obs", mu=mu, sigma=sigma, observed=obs)
        trace = pm.sample(draws=draws,
                          tune=tune,
                          target_accept=target_accept,
                          random_seed=random_seed,
                          chains=4,
                          cores=None,
                          progressbar=False)

    mu_smpl = trace.posterior["mu"].values.ravel()
    # assegna ogni campione alla µ più vicina
    idx = np.abs(mu_smpl[:, None] - mu_vals).argmin(axis=1)
    counts = np.bincount(idx, minlength=len(mu_vals))
    posterior = counts / counts.sum()

    return pd.DataFrame({
        "ipotesi": merged[h_df.columns[0]],
        "mu": mu_vals,
        "prior": w_prior,
        "posterior": posterior
    }).sort_values("posterior", ascending=False)


# ------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="PyMC NUTS – Prior vs Posterior")
    ap.add_argument("--hypotheses", required=True,
                    help="CSV 2 colonne: nome_ipotesi,valore")
    ap.add_argument("--priors", required=True,
                    help="CSV 2 colonne: valore,probabilità")
    ap.add_argument("--observations", required=True,
                    help="CSV 1 colonna: osservazione")
    ap.add_argument("--sigma", type=float, required=True,
                    help="Deviazione standard nota")
    ap.add_argument("--draws", type=int, default=5000,
                    help="Campioni posteriori salvati (default 5000)")
    ap.add_argument("--tune", type=int, default=2000,
                    help="Iterazioni di tuning NUTS (default 2000)")
    ap.add_argument("--target_accept", type=float, default=0.9,
                    help="target_accept NUTS (default 0.9)")
    ap.add_argument("--seed", type=int, default=42,
                    help="Random seed per riproducibilità")
    args = ap.parse_args()

    h_df = carica_csv(args.hypotheses, 2)
    p_df = carica_csv(args.priors, 2)
    o_df = carica_csv(args.observations, 1)

    tab = posteriori_mcmc(h_df, p_df, o_df,
                          args.sigma,
                          args.draws,
                          args.tune,
                          args.target_accept,
                          args.seed)

    # --------------------------------------------------------
    # Stampa delle due PDF
    # --------------------------------------------------------
    print("\n=== PDF PRIOR (normalizzata) ===")
    for mu, pr in zip(tab["mu"], tab["prior"]):
        print(f"µ={mu:.6f}  f_prior={pr:.6f}")

    print("\n=== PDF POSTERIOR (stimata via MCMC) ===")
    for mu, po in zip(tab["mu"], tab["posterior"]):
        print(f"µ={mu:.6f}  f_posterior={po:.6f}")

    # --------------------------------------------------------
    # Grafico confronto PDF
    # --------------------------------------------------------
    plt.figure(figsize=(8, 4.5))
    plt.plot(tab["mu"], tab["prior"],
             label="Prior",     marker="o", linestyle="--")
    plt.plot(tab["mu"], tab["posterior"],
             label="Posterior", marker="o")
    plt.xlabel("µ (ipotesi)")
    plt.ylabel("Densità PDF")
    plt.title("Prior vs Posterior – PyMC NUTS")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
