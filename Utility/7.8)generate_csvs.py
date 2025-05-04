# generate_csvs.py
# Script di supporto: genera CSV casuali per ipotesi, priori e osservazioni
import argparse, pandas as pd, numpy as np
from pathlib import Path

def main():
    ap = argparse.ArgumentParser(description="Genera CSV casuali per test")
    ap.add_argument("--hypotheses_out",required=True)
    ap.add_argument("--priors_out",required=True)
    ap.add_argument("--observations_out",required=True)
    ap.add_argument("--n_hyp",type=int,default=50)
    ap.add_argument("--mu_min",type=float,default=4.0)
    ap.add_argument("--mu_max",type=float,default=6.0)
    ap.add_argument("--sigma",type=float,default=0.5)
    ap.add_argument("--n_obs",type=int,default=30)
    args = ap.parse_args()

    mu_vals = np.linspace(args.mu_min,args.mu_max,args.n_hyp)
    pd.DataFrame({"nome_ipotesi":[f"H{i}" for i in range(args.n_hyp)],"valore":mu_vals}).to_csv(args.hypotheses_out,index=False)

    dirichlet = np.random.dirichlet(np.ones(args.n_hyp))
    pd.DataFrame({"variabile":mu_vals,"probabilità":dirichlet}).to_csv(args.priors_out,index=False)

    true_mu = np.random.choice(mu_vals,p=dirichlet)
    obs = np.random.normal(loc=true_mu,scale=args.sigma,size=args.n_obs)
    pd.DataFrame({"osservazione":obs}).to_csv(args.observations_out,index=False)

    print(f"CSV generati in: {Path(args.hypotheses_out).resolve()}, {Path(args.priors_out).resolve()}, {Path(args.observations_out).resolve()}")
    print(f"μ reale usata per le osservazioni: {true_mu}")

if __name__=="__main__":
    main()
