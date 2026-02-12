from scipy.stats import chisquare
import numpy as np

obs = np.array([450, 400, 150])
exp = np.array([430, 440, 150])

exp = exp * (obs.sum() / exp.sum())
chi, p = chisquare(f_obs=obs, f_exp=exp)

print("Chi-square =", chi)
print("p-value =", p)

if p > 0.05:
    print("No significant difference (Data fits expected distribution)")
else:
    print("Significant difference detected")