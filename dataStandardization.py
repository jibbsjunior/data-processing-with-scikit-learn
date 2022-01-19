from cmath import pi
import numpy as np
from sklearn.preprocessing import scale

# Data standardization is a relatively simple process. For each data value, x, we subtract the overall mean of the data, μ, then divide by the overall standard deviation, σ. The new value, z, represents the standardized data value. Thus, the formula for data standardization is:
# z = ​x−μ / σ
pizza_data = np.array([
    [8483, 7383, 8332, 9384, 9490, 7845],
    [2016, 2016, 2021, 2016, 2017, 2019],
    [2011, 2783, 4324, 8746, 9837, 3343],
])

#standardizing each column of pizza
col_standardized = scale(pizza_data)
# print('{}\n'.format(repr(pizza_data)))

#Column means (rounded to the nearest thousandth)
col_means = col_standardized.mean(axis=0).round(decimals=3)
# print('{}\n'.format(repr(col_means)))

#COlumn standard deviation
col_std = col_standardized.std(axis=1)
print('{}\n'.format(repr(col_std)))