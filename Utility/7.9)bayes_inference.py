# bayes_inference.py
# ------------------------------------------------------------
# Calcolo bayesiano esatto su ipotesi discrete con stampa
# delle due PDF  (Prior e Posterior)  e relativo grafico.
# ------------------------------------------------------------
# Avvio:
#   python bayes_inference.py --hypotheses ipotesi.csv \
#       --priors priori.csv --observations osservazioni.csv \
#       --sigma 0.5
# ------------------------------------------------------------

import argparse, pandas as pd, numpy as np, matplotlib.pyplot as plt
from scipy.stats import norm


# ------------------------------------------------------------
def carica_csv(path: str, n_cols: int) -> pd.DataFrame:
    df = pd.read_csv(path)
    if len(df.columns) != n_cols:
        raise ValueError(f"{path} deve avere {n_cols} colonne, ne ha {len(df.columns)}.")
    return df


# ------------------------------------------------------------
def posteriori_esatta(h_df: pd.DataFrame,
                      p_df: pd.DataFrame,
                      o_df: pd.DataFrame,
                      sigma: float) -> pd.DataFrame:
    # Normalizziamo i nomi colonna → val (numerica) e prob (prior)
    h_df = h_df.rename(columns={h_df.columns[1]: "val"})
    p_df = p_df.rename(columns={p_df.columns[0]: "val",
                                p_df.columns[1]: "prob"})
    merged = h_df.merge(p_df, on="val")
    if merged.empty:
        raise ValueError("Valori numerici di ipotesi e priori non coincidono.")

    prior = merged["prob"].to_numpy(dtype=float)
    prior /= prior.sum()                               # PDF priori
    mu_vals = merged["val"].to_numpy(dtype=float)
    obs = o_df.iloc[:, 0].to_numpy(dtype=float)

    # Likelihood complessiva: prodotto delle pdf normali per ogni µ
    like = np.prod(norm.pdf(obs[:, None],
                            loc=mu_vals,
                            scale=sigma),
                   axis=0)
    posterior = like * prior
    posterior /= posterior.sum()                       # PDF posteriori

    return pd.DataFrame({
        "ipotesi": merged[h_df.columns[0]],
        "mu": mu_vals,
        "prior": prior,
        "posterior": posterior
    }).sort_values("posterior", ascending=False)


# ------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description="PDF Prior vs Posterior Bayesiani")
    ap.add_argument("--hypotheses", required=True,
                    help="CSV 2 colonne: nome_ipotesi,valore")
    ap.add_argument("--priors", required=True,
                    help="CSV 2 colonne: valore,probabilità")
    ap.add_argument("--observations", required=True,
                    help="CSV 1 colonna: osservazione")
    ap.add_argument("--sigma", type=float, required=True,
                    help="Deviazione standard nota")
    args = ap.parse_args()

    h_df = carica_csv(args.hypotheses, 2)
    p_df = carica_csv(args.priors, 2)
    o_df = carica_csv(args.observations, 1)

    tab = posteriori_esatta(h_df, p_df, o_df, args.sigma)

    # --------------------------------------------------------
    # Stampa delle due PDF
    # --------------------------------------------------------
    print("\n=== PDF PRIOR (normalizzata) ===")
    for mu, pr in zip(tab["mu"], tab["prior"]):
        print(f"µ={mu:.6f}  f_prior={pr:.6f}")

    print("\n=== PDF POSTERIOR (normalizzata) ===")
    for mu, po in zip(tab["mu"], tab["posterior"]):
        print(f"µ={mu:.6f}  f_posterior={po:.6f}")

    # --------------------------------------------------------
    # Grafico confronto PDF
    # --------------------------------------------------------
    plt.figure(figsize=(8, 4.5))
    plt.plot(tab["mu"], tab["prior"],     label="Prior",     marker="o", linestyle="--")
    plt.plot(tab["mu"], tab["posterior"], label="Posterior", marker="o")
    plt.xlabel("µ (ipotesi)")
    plt.ylabel("Densità PDF")
    plt.title("Prior vs Posterior – distribuzioni PDF")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
