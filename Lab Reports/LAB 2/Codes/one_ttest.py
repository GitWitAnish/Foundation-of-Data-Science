import numpy as np
import scipy.stats as stats


#One Sample t test
scores = [78, 72, 74, 76, 73, 79, 77, 71, 70, 74]
population_mean = 75
n=len(scores)

sample_mean = np.mean(scores)
sample_std = np.std(scores, ddof=1)

t_stat = (sample_mean - population_mean)/(sample_std/ np.sqrt(n))

df = n-1

p_value = 2*stats.t.sf(abs(t_stat), df)

print(f"sample mean: {sample_mean:.2f}")
print(f"t-statistic: {t_stat:.2f}")
print(f"p-value: {p_value:.2f}")

if p_value < 0.05:
  print("Reject. The sample mean is signifivally different.")

else:
  print("Fail to reject. No difference.")