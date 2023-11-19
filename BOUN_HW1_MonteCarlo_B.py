import numpy as np
from scipy.stats import norm

# Prompting user for inputs
mu_x = float(input("Enter hypothesized mean of population x (µx): "))
mu_y = float(input("Enter hypothesized mean of population y (µy): "))
sigma_x2 = float(input("Enter known variance of population x (σx^2): "))
sigma_y2 = float(input("Enter known variance of population y (σy^2): "))
nx = int(input("Enter sample size from population x (nx): "))
ny = int(input("Enter sample size from population y (ny): "))
alpha = float(input("Enter significance level (α): "))
NR = int(input("Enter number of replications (NR): "))

# Critical value alıyoruz z için
z_alpha = norm.ppf(1 - alpha)

# Counter for Type I errors
type_I_error_count = 0

for _ in range(NR):
    # Sample üretiyoruz:
    sample_x = np.random.normal(mu_x, np.sqrt(sigma_x2), nx)
    sample_y = np.random.normal(mu_y, np.sqrt(sigma_y2), ny)

    # Sample mean hesaplıyoruz
    xbar = np.mean(sample_x)
    ybar = np.mean(sample_y)

    # Formülü embed ediyoruz.
    pooled_se = np.sqrt(sigma_x2/nx + sigma_y2/ny)
    z_statistic = (ybar - 2*xbar) / pooled_se

    # Reject regiona düşüp düşmediğini check ediyoruz
    if z_statistic > z_alpha:
        type_I_error_count += 1

# Oran hesaplıyoruz:
type_I_error_rate = type_I_error_count / NR

# Yazdırıyoruz:
print(f"Type I Error Rate: {type_I_error_rate}")
