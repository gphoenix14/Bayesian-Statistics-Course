import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# ---------- Target ----------
def target_log_pdf(theta):
    return -theta**4 + theta**2

def grad_log_pdf(theta):
    return -4 * theta**3 + 2 * theta

def target_pdf(theta):
    return np.exp(target_log_pdf(theta))

# ---------- 1. Random‑Walk Metropolis‑Hastings ----------
def metropolis_rw(init, n_samples, sigma=1.0):
    samples = np.empty(n_samples)
    theta = init
    accept = 0
    for i in range(n_samples):
        theta_p = np.random.normal(theta, sigma)
        log_alpha = target_log_pdf(theta_p) - target_log_pdf(theta)
        if np.log(np.random.rand()) < log_alpha:
            theta = theta_p
            accept += 1
        samples[i] = theta
    return samples, accept / n_samples

# ---------- 2. MALA ----------
def mala(init, n_samples, step=0.5):
    samples = np.empty(n_samples)
    theta = init
    accept = 0
    for i in range(n_samples):
        mean = theta + (step**2 / 2) * grad_log_pdf(theta)
        theta_p = np.random.normal(mean, step)
        log_p_fwd = target_log_pdf(theta_p)
        log_q_fwd = -((theta_p - mean)**2) / (2 * step**2)
        mean_rev = theta_p + (step**2 / 2) * grad_log_pdf(theta_p)
        log_p_rev = target_log_pdf(theta)
        log_q_rev = -((theta - mean_rev)**2) / (2 * step**2)
        log_alpha = (log_p_fwd + log_q_rev) - (log_p_rev + log_q_fwd)
        if np.log(np.random.rand()) < log_alpha:
            theta = theta_p
            accept += 1
        samples[i] = theta
    return samples, accept / n_samples

# ---------- 3. Slice Sampling (1‑D) ----------
def slice_sampling(init, n_samples, w=1.0, m=100):
    samples = np.empty(n_samples)
    theta = init
    for i in range(n_samples):
        log_y = target_log_pdf(theta) - np.random.exponential()
        u = np.random.rand()
        L = theta - u * w
        R = L + w
        cnt = 0
        while target_log_pdf(L) > log_y and cnt < m:
            L -= w
            cnt += 1
        cnt = 0
        while target_log_pdf(R) > log_y and cnt < m:
            R += w
            cnt += 1
        while True:
            theta_p = np.random.uniform(L, R)
            if target_log_pdf(theta_p) >= log_y:
                theta = theta_p
                break
            elif theta_p < theta:
                L = theta_p
            else:
                R = theta_p
        samples[i] = theta
    return samples

# ---------- 4. Hamiltonian Monte Carlo ----------
def leapfrog(theta, p, step_size, n_steps, mass=1.0):
    theta_new = theta
    p_new = p + 0.5 * step_size * grad_log_pdf(theta_new)
    for _ in range(n_steps - 1):
        theta_new += step_size * p_new / mass
        p_new += step_size * grad_log_pdf(theta_new)
    theta_new += step_size * p_new / mass
    p_new += 0.5 * step_size * grad_log_pdf(theta_new)
    p_new = -p_new  # momentum flip for symmetry
    return theta_new, p_new

def hmc(init, n_samples, step_size=0.3, n_steps=10, mass=1.0):
    samples = np.empty(n_samples)
    theta = init
    accept = 0
    for i in range(n_samples):
        p0 = np.random.normal(0, np.sqrt(mass))
        theta_new, p_new = leapfrog(theta, p0, step_size, n_steps, mass)
        current_U = -target_log_pdf(theta)
        current_K = p0**2 / (2 * mass)
        proposed_U = -target_log_pdf(theta_new)
        proposed_K = p_new**2 / (2 * mass)
        log_alpha = -(proposed_U + proposed_K) + (current_U + current_K)
        if np.log(np.random.rand()) < log_alpha:
            theta = theta_new
            accept += 1
        samples[i] = theta
    return samples, accept / n_samples

# ---------- 5. No‑U‑Turn Sampler (NUTS, simplified) ----------
def leapfrog_nuts(theta, p, step):
    p_half = p + 0.5 * step * grad_log_pdf(theta)
    theta_new = theta + step * p_half
    p_new = p_half + 0.5 * step * grad_log_pdf(theta_new)
    return theta_new, p_new

def hamiltonian(theta, p, mass=1.0):
    return -target_log_pdf(theta) + p**2 / (2 * mass)

def nuts(init, n_samples, step_size=0.3, max_depth=8, mass=1.0):
    samples = np.empty(n_samples)
    theta = init
    accept = 0
    for i in range(n_samples):
        p0 = np.random.normal(0, np.sqrt(mass))
        joint0 = hamiltonian(theta, p0, mass)
        # Initialize tree
        theta_minus, theta_plus = theta, theta
        p_minus, p_plus = p0, p0
        depth = 0
        theta_candidate = theta
        n = 1
        s = 1  # stop flag
        while s == 1 and depth < max_depth:
            direction = 1 if np.random.rand() < 0.5 else -1
            if direction == -1:
                theta_minus, p_minus, _, _, theta_prime, n_prime, s_prime = build_tree(
                    theta_minus, p_minus, direction, depth, step_size, theta, p0, joint0, mass
                )
            else:
                _, _, theta_plus, p_plus, theta_prime, n_prime, s_prime = build_tree(
                    theta_plus, p_plus, direction, depth, step_size, theta, p0, joint0, mass
                )
            if s_prime == 1 and np.random.rand() < n_prime / max(n + n_prime, 1):
                theta_candidate = theta_prime
            n += n_prime
            s = s_prime and stop_criterion(theta_minus, theta_plus, p_minus, p_plus)
            depth += 1
        theta = theta_candidate
        samples[i] = theta
    return samples

def build_tree(theta, p, direction, depth, step_size, theta0, p0, joint0, mass):
    if depth == 0:
        theta_new, p_new = leapfrog_nuts(theta, p, direction * step_size)
        joint = hamiltonian(theta_new, p_new, mass)
        d_joint = joint - joint0
        n = 1 if np.log(np.random.rand()) < -d_joint else 0
        s = 1 if -d_joint < 1000 else 0  # numerical stability
        return theta_new, p_new, theta_new, p_new, theta_new, n, s
    else:
        theta_minus, p_minus, theta_plus, p_plus, theta_prime, n_prime, s_prime = build_tree(
            theta, p, direction, depth - 1, step_size, theta0, p0, joint0, mass
        )
        if s_prime == 1:
            if direction == -1:
                theta_minus, p_minus, _, _, theta_prime2, n_prime2, s_prime2 = build_tree(
                    theta_minus, p_minus, direction, depth - 1, step_size, theta0, p0, joint0, mass
                )
            else:
                _, _, theta_plus, p_plus, theta_prime2, n_prime2, s_prime2 = build_tree(
                    theta_plus, p_plus, direction, depth - 1, step_size, theta0, p0, joint0, mass
                )
            if np.random.rand() < n_prime2 / max(n_prime + n_prime2, 1):
                theta_prime = theta_prime2
            n_prime += n_prime2
            s_prime = s_prime2 and stop_criterion(theta_minus, theta_plus, p_minus, p_plus)
        return theta_minus, p_minus, theta_plus, p_plus, theta_prime, n_prime, s_prime

def stop_criterion(theta_minus, theta_plus, p_minus, p_plus):
    delta_theta = theta_plus - theta_minus
    return (delta_theta * p_minus) >= 0 and (delta_theta * p_plus) >= 0

# ---------- Sampling ----------
N = 10000
rw_samples, rw_acc = metropolis_rw(0.0, N, sigma=1.0)
mala_samples, mala_acc = mala(0.0, N, step=0.5)
slice_samples = slice_sampling(0.0, N, w=1.0, m=100)
hmc_samples, hmc_acc = hmc(0.0, N, step_size=0.3, n_steps=10)
nuts_samples = nuts(0.0, N, step_size=0.3, max_depth=8)

print(f"RW‑MH acc: {rw_acc:.3f}")
print(f"MALA acc: {mala_acc:.3f}")
print(f"HMC acc:  {hmc_acc:.3f}")
print("Slice e NUTS non hanno rate definito")

# ---------- Plot ----------
def plot_hist(samples, title):
    plt.figure()
    plt.hist(samples, bins=100, density=True, alpha=0.6, label="Campioni")
    x = np.linspace(-3, 3, 500)
    pdf = target_pdf(x)
    pdf /= np.trapz(pdf, x)
    plt.plot(x, pdf, linewidth=2, label="Densità target normalizzata")
    plt.title(title)
    plt.legend()
    plt.grid(True)

plot_hist(rw_samples, "Random‑Walk Metropolis‑Hastings")
plot_hist(mala_samples, "Metropolis‑Adjusted Langevin (MALA)")
plot_hist(slice_samples, "Slice Sampling")
plot_hist(hmc_samples, "Hamiltonian Monte Carlo (HMC)")
plot_hist(nuts_samples, "No‑U‑Turn Sampler (NUTS)")

plt.show()
