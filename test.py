import numpy as np
import pandas as pd

group_A = pd.DataFrame([[2, 5, 8, 3], [3, np.nan, 7, 4], [5, 2, 50, 5], [2, 3, 8, 2], [3, 6, 2, 5]],
                       columns=['A', 'B', 'C', 'key'], dtype=int)
print(group_A)
