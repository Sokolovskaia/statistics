import pandas as pd
import numpy as np
from scipy import stats
# меры центральной тенденции (среднее, медиана, мода)
df_1 = pd.DataFrame({'player_number': [10, 8, 12, 22, 36, 7, 1, 20, 9, 4, 14],
                     'height': [168, 176, 178, 191, 185, 183, 185, 179, 169, 183, 167],
                     'weight': [76, 77, 79, 81, 82, 79, 74, 84, 73, 71, 68],
                     'score': [95, 86, 94, 96, 95, 95, 89, 83, 99, 78, 82]})


# к отдельному столбцу
# среднее
mean_height = df_1['height'].mean()
# медиана
meadian_height = df_1['height'].median()
# мода (на выходе Серия мод)
moda_height = df_1['height'].mode()

# ко всему ДатаФрейму
mean_df = df_1.mean()

# с помощью scipy и numpy
# среднее
mean_height_np = np.mean(df_1['height'])
# медиана
meadian_height_np = np.median(df_1['height'])
# мода
moda_height_scipy = stats.mode(df_1['height'])

# print(df_1[df_1['weight'] > 75])


# _________________________________________________________
# def solution(df): #
#     x = df['weight'][df['score'] > 90].mean()
#     return round(x, 5)
#
# for_p_1 = solution(df_1)

# print(for_p_1)
# _________________________________________________________

# def solution(A): # A - некий датафрейм
#     x = A[(A['weight'] > 80) & (A['score'] >= 95)]
#     return round(x['height'].mean(), 1)

# print(solution(df_1))
# _________________________________________________________

df_2 = pd.DataFrame({'Company': ['Occidental Petroleum',
                                 'Exxon Mobil Corporation',
                                 'Chevron Corporation',
                                 'Ovintiv Inc.',
                                 'Murphy Oil',
                                 'Apache Corp',
                                 'Continental Resources',
                                 'PDC Energy',
                                 'Phillips 99',
                                 'Devon Energy Corp',
                                 'Canadian Natural Resources',
                                 'Cenovus Energy',
                                 'Enbridge',
                                 'Husky Energy',
                                 'Imperial Oil',
                                 'Irving Oil',
                                 'Pembina Pipeline',
                                 'Suncor Energy'],
                     'ROE': [7.35, 4.33, 3.37, 8.3, 3.97, 9.88, 9.52, 7.48, 4.76,
                             8.95, 9.10, 4.21, 6.12, 7.91, 8.49, 8.72, 6.52, 4.75]})

# Дисперсия
df_var = df_2['ROE'].var(ddof=0)
# Стандартное отклонение
df_std = df_2['ROE'].std()

# print('Дисперсия ', df_var)
# print('Стандартное отклонение ', df_std)


def solution(A): # A - некий датафрейм
    x = A.query("Company != 'Apache Corp'").ROE.std().round(5)
    return x

print(solution(df_2))