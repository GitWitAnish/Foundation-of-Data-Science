#Two sample t-test

import numpy as np
import scipy.stats as stats

class_a = [85,88,90,92,86,84,87,89,91,93]
class_b = [78,80,82,79,81,77,83,76,75,80]

t_stat, p_value = stats.ttest_ind(class_a, class_b, equal_var=False)

print(f"t-statistic: {t_stat:.2f}")
print(f"p-value: {p_value:.2f}")

if p_value < 0.05:
  print("Reject. There is a significant difference.")

else:
  print("Fail to reject. No difference.")