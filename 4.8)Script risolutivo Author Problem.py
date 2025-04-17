#!/usr/bin/env python3
"""
Inferenza bayesiana sull’autore del documento n. 54 basata sui
tassi di «upon».

Il CSV deve contenere le colonne: id, author, rate
e *una* riga con author = 'Unknown' per il documento incerto.
Il rate osservato viene letto da quella riga; l’utente fornisce
solo la prior.

Esempio d’uso:
    python3 script_bayes_author.py upon_rates.csv
"""
import argparse
import sys
import pandas as pd
import matplotlib.pyplot as plt

KNOWN = {"Hamilton", "Madison"}

def assign_bin(rate: float) -> str:
    if rate == 0:
        return "0"
    for low in range(0, 8):
        high = low + 1
        if low < rate <= high:
            return "(0,1]" if low == 0 else f"({low},{high}]"
    return ">8"     # fuori dalla distribuzione tabellata

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    if not {"author", "rate"}.issubset(df.columns):
        sys.exit("Il CSV deve contenere le colonne 'author' e 'rate'.")
    return df

def likelihoods(df: pd.DataFrame, bin_label: str) -> dict:
    tot = df[df["author"].isin(KNOWN)].groupby("author").size()
    same = df[(df["author"].isin(KNOWN)) &
              (df["rate"].apply(assign_bin) == bin_label)]
    cnt = same.groupby("author").size()
    return {a: cnt.get(a, 0) / tot[a] for a in tot.index}

def main():
    ap = argparse.ArgumentParser(description="Bayesian Author Attribution")
    ap.add_argument("csv", help="Dataset con i tassi standardizzati di upon")
    args = ap.parse_args()

    df = load_data(args.csv)
    unknown = df[~df["author"].isin(KNOWN)]
    if unknown.empty:
        sys.exit("Manca la riga con author 'Unknown' per il documento incerto.")

    rate_obs = unknown.iloc[0]["rate"]
    bin_obs  = assign_bin(rate_obs)
    like     = likelihoods(df, bin_obs)

    prior_h = float(input("Probabilità a priori per Hamilton (0‑1): ").strip())
    if not 0 <= prior_h <= 1:
        sys.exit("La prior deve essere fra 0 e 1.")
    prior_m = 1 - prior_h

    p_d_h, p_d_m = like.get("Hamilton", 0.0), like.get("Madison", 0.0)
    post_h = (p_d_h * prior_h) / (p_d_h * prior_h + p_d_m * prior_m)
    post_m = 1 - post_h

    # ── Output testuale ────────────────────────────────────────────────────
    print("\n=== RISULTATI ===")
    print(f"Rate osservato                         : {rate_obs}")
    print(f"Intervallo (bin)                       : {bin_obs}")
    print(f"Verosimiglianza P(data|Hamilton)       : {p_d_h:.5f}")
    print(f"Verosimiglianza P(data|Madison)        : {p_d_m:.5f}")
    print(f"Prior Hamilton                         : {prior_h:.3f}")
    print(f"Prior Madison                          : {prior_m:.3f}")
    print(f"Posterior Hamilton                     : {post_h:.5f}")
    print(f"Posterior Madison                      : {post_m:.5f}")

    # ── Barplot ───────────────────────────────────────────────────────────
    labels     = ["Hamilton", "Madison"]
    prior_vals = [prior_h, prior_m]
    post_vals  = [post_h, post_m]
    x, width   = range(len(labels)), 0.35

    fig, ax = plt.subplots()
    ax.bar([xi - width/2 for xi in x], prior_vals, width, label="Prior")
    ax.bar([xi + width/2 for xi in x], post_vals,  width, label="Posterior")
    ax.set_ylabel("Probabilità")
    ax.set_title("Prior vs Posterior")
    ax.set_xticks(list(x))
    ax.set_xticklabels(labels)
    ax.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
