#two sample z-test

import numpy as np
import scipy.stats as stats

mean1, std1, n1= 495,10,50
mean2, std2, n2= 500,12,60

z_stat= (mean1-mean2)/((std1**2/n1+std2**2/n2)**0.5)

p_value = 2*stats.norm.sf(abs(z_stat))

print(f"z-statistic: {z_stat:.2f}")
print(f"p-value: {p_value:.4f}")


if p_value < 0.05:
  print("Reject. The sample mean is signifivally different.")

else:
  print("Fail to reject. No difference.")