#One sample z-test

import numpy as np
import scipy.stats as stats

sample_mean = 495
population_mean = 500
population_std = 10
n = 30

z_stat = (sample_mean - population_mean)/(population_std/np.sqrt(n))

p_value = 2*stats.norm.sf(abs(z_stat))

print(f"z-statistic: {z_stat:.2f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
  print("Reject. The sample mean is signifivally different.")

else:
  print("Fail to reject. No difference.")

