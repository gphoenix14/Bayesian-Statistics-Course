# Regressione bayesiana: bodyfat ~ abdomen
# pip install pandas numpy pymc arviz matplotlib

import pandas as pd
import numpy as np
import pymc as pm
import arviz as az
import matplotlib.pyplot as plt
from matplotlib import gridspec

def run_model():
    # 1. Caricamento dataset
    url = "https://hbiostat.org/data/repo/bodyfat.csv"
    df = pd.read_csv(url)
    df.rename(columns={"BodyFat": "bodyfat", "Abdomen": "abdomen"}, inplace=True)
    x = df["abdomen"].values
    y = df["bodyfat"].values

    # 2. Modello bayesiano
    with pm.Model() as model:
        alpha = pm.Normal("alpha", mu=0, sigma=100)
        beta = pm.Normal("beta", mu=0, sigma=100)
        sigma = pm.HalfCauchy("sigma", beta=10)

        mu = alpha + beta * x
        y_obs = pm.Normal("y_obs", mu=mu, sigma=sigma, observed=y)

        trace = pm.sample(
            draws=2000,
            tune=1000,
            chains=4,
            cores=4,
            target_accept=0.9,
            return_inferencedata=True,
            progressbar=True
        )

    # 3. Sommario e distribuzioni posteriori
    print(az.summary(trace, var_names=["alpha", "beta", "sigma"], round_to=2))
    az.plot_posterior(trace, var_names=["alpha", "beta"], hdi_prob=0.95)
    plt.tight_layout()
    plt.show()

    # 4. Posterior predictive mean (valori predetti)
    alpha_samples = trace.posterior["alpha"].stack(samples=("chain", "draw")).values
    beta_samples = trace.posterior["beta"].stack(samples=("chain", "draw")).values
    y_hat_samples = np.array([a + b * x for a, b in zip(alpha_samples, beta_samples)])  # (n_samples, n_obs)
    y_hat_mean = y_hat_samples.mean(axis=0)

    # 5. Confronto predetti vs osservati + residui
    fig = plt.figure(constrained_layout=True, figsize=(12, 5))
    gs = gridspec.GridSpec(1, 2, figure=fig)

    # Scatter predetto vs osservato
    ax1 = fig.add_subplot(gs[0])
    ax1.scatter(y_hat_mean, y, alpha=0.6)
    ax1.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', label='perfetta predizione')
    ax1.set_xlabel("Predetto (media posterior)")
    ax1.set_ylabel("Osservato")
    ax1.set_title("Predizione vs Osservazione")
    ax1.legend()

    # Residui
    ax2 = fig.add_subplot(gs[1])
    residui = y - y_hat_mean
    ax2.scatter(x, residui, alpha=0.6)
    ax2.axhline(0, color='r', linestyle='--')
    ax2.set_xlabel("Circonferenza addominale (x)")
    ax2.set_ylabel("Residuo (y - predetto)")
    ax2.set_title("Analisi dei residui")

    plt.show()

    # 6. Regressione bayesiana + 95% CrI
    x_line = np.linspace(x.min(), x.max(), 100)
    y_post = np.array([a + b * x_line for a, b in zip(alpha_samples, beta_samples)])
    y_mean = y_post.mean(axis=0)
    y_hdi = az.hdi(y_post, hdi_prob=0.95)

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, "o", label="dati osservati", alpha=0.6)
    plt.plot(x_line, y_mean, color="navy", label="retta bayesiana (media)")
    plt.fill_between(x_line, y_hdi[:, 0], y_hdi[:, 1], color="skyblue", alpha=0.4, label="95% CrI")
    plt.xlabel("Circonferenza addominale (x)")
    plt.ylabel("Body-fat (y)")
    plt.title("Regressione bayesiana: retta + intervallo credibile")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 7. Predizione su nuovo valore
    new_abdomen = 90
    with model:
        pm.set_data({"abdomen": np.array([new_abdomen])})
        posterior_pred = pm.sample_posterior_predictive(trace, var_names=["y_obs"], progressbar=False)
    y_pred = posterior_pred["y_obs"].ravel()
    print(f"\nPredizione body-fat per abdomen = {new_abdomen} cm:")
    print(f"Media: {y_pred.mean():.2f}")
    print(f"95% intervallo credibile: ({np.percentile(y_pred, 2.5):.2f}, {np.percentile(y_pred, 97.5):.2f})")

# Richiesto su Windows per multiprocessing
if __name__ == "__main__":
    run_model()
