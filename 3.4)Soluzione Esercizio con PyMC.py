import pymc as pm
import arviz as az
import matplotlib.pyplot as plt

def main():
    # Dati del problema
    p_interessati = 0.05
    p_si_se_interessati = 0.90
    p_si_se_non_interessati = 0.10

    # Definizione del modello
    with pm.Model() as modello_offerta_green:

        # Prior sulla variabile "realmente interessato"
        interessato = pm.Bernoulli('interessato', p_interessati)

        # Likelihood del cliente che dichiara "Sì"
        prob_dichiara_si = pm.math.switch(interessato, p_si_se_interessati, p_si_se_non_interessati)

        # Osservazione (cliente dichiara "sì")
        dichiara_si = pm.Bernoulli('dichiara_si', prob_dichiara_si, observed=1)

        # Campionamento (con 2 chain)
        trace = pm.sample(5000, tune=2000, return_inferencedata=True, chains=2)

    # Risultati
    az.plot_posterior(trace, var_names=['interessato'], hdi_prob=0.95)
    plt.title('Probabilità che il cliente sia davvero interessato\n dato che ha dichiarato "Sì"')
    plt.show()

    # Riepilogo numerico
    summary = az.summary(trace, var_names=['interessato'], hdi_prob=0.95)
    print(summary)

if __name__ == '__main__':
    main()
