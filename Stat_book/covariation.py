import pandas as pd
import numpy as np
from scipy import stats


NIM = pd.Series([7.6, 7.9, 8.3, 7.2, 6.9, 7.9, 7.4, 7.8, 5.9, 7.1, 6.8])
rate = pd.Series([10, 12, 12, 8, 8, 7.5, 7.5, 7.5, 6.5, 7, 7])

# Scipy
# рассчитываем значение корреляции Пирсона между двумя сериями данных NIM и rate
corr_1 = stats.pearsonr(NIM, rate).statistic
# statistic
# pvalue

# Pandas
df_1 = pd.DataFrame({'NIM': [7.6, 7.9, 8.3, 7.2, 6.9, 7.9, 7.4, 7.8, 5.9, 7.1, 6.8],
                   'rate': [10, 12, 12, 8, 8, 7.5, 7.5, 7.5, 6.5, 7, 7],
                   'GDP_growth': [2.5, 1.8, 3.1, 1.9, 2.4, 2.8, 1.0, 3.2, 2.1, 2.2, 0.5]})

corr_matrix_1 = df_1.corr()


# _________________________________________________________

A = np.array([43, 32, 42, 48, 58, 57.5, 47.5, 37.5, 56.5, 67, 47.3])
B = np.array([12.5, 11.8, 13.1, 11.9, 12.4, 17.8, 13.3, 13.2, 12.1, 12.2, 8.5])

def solution(a,b): # a,b - некие массивы Numpy
    x = stats.pearsonr(a, b)[0].round(5)
    return x

print(solution(A,B))