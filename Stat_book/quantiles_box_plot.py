# Box Plot & квартили, квантили, перцентили

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


df_1 = pd.DataFrame({'ROE': [7.4, 7.8, 5.9, 7.1, 6.8, 7.6, 7.9, 8.3, 7.2, 6.9, 7.9],
                   'COF': [6.3, 4.2, 6.2, 8.1, 8.4, 7.5, 6.5, 7.8, 6.9, 7.1, 7.2],
                   'rating': ['AAA', 'BB+', 'BB+', 'AAA', 'BBB-', 'AA', 'AAA', 'AAA', 'BBB-', 'AAA', 'BB+']})

# список квартилей
Q = [0.25, 0.5, 0.75]
for_p_1 = df_1['ROE'].quantile([0.25, 0.5, 0.75])


# _________________________________________________________
def solution(A): # A - некий датафрейм
    x = A.groupby('rating')['COF'].quantile(0.25)['AAA'].round(1)
    # x = A[A['rating'] == 'AAA']['COF'].quantile(0.25).round(5)
    return x

for_p_2 = solution(df_1)
# _________________________________________________________

def solution(A): # A - некий датафрейм
    x = A.groupby('rating')['COF'].quantile([0.25, 0.5])['BB+']
    return round(max(x), 1)

for_p_3 = solution(df_1)

# _________________________________________________________
def solution(A): # A - некий датафрейм
    x = A.COF.quantile(.53).round(3)
    return x

for_p_4 = solution(df_1)

# _________________________________________________________

# график Box Plot


df_2 = pd.DataFrame({
    'ROE': [7.4, 7.8, 5.9, 7.1, 6.8, 7.6, 7.9, 8.3, 7.2, 6.9, 7.9],
    'COF': [6.3, 4.2, 6.2, 8.1, 8.4, 7.5, 6.5, 7.8, 6.9, 7.1, 7.2],
    'rating': ['AAA', 'BB+', 'BB+', 'AAA', 'BBB-', 'AA', 'AAA', 'AAA', 'BBB-', 'AAA', 'BB+']
})

# Показать ОДИН графика
# bp_1 = plt.boxplot(df_2['COF'],
#                  vert=True,  # расположение бокса (True по умолчанию)
#                  patch_artist=False,  # наполнение бокса цветом (False по умолчанию)
#                  showmeans=True,  # показывать среднее (зеленый треугольник) (False по умолчанию)
#                  showfliers=True,  # показывать выбросы (True по умолчанию)
#                  tick_labels=['COF'])  # надписи

# # Показать НЕСКОЛЬКО графиков
# bp_2 = plt.boxplot([df_2['COF'], df_2['ROE']],
#                      vert=True,  # расположение бокса (True по умолчанию)
#                      patch_artist=False,  # наполнение бокса цветом (False по умолчанию)
#                      showmeans=True, # показывать среднее (False по умолчанию)
#                      showfliers=True, # показывать выбросы (True по умолчанию)
#                      tick_labels=['COF', 'ROE'])  # надписи

# с помощью groupby
df_2.boxplot(column=['COF', 'ROE'],
             by='rating',
             grid=False,
             color='purple')

# plt.show()


def function1(x):
    return [el if 0 <= el <= 5 else 0 for el in x]

def function1_INT(x):
    return [
        0.5 * el ** 2 if 0 <= el <= 5 else (0 if el < 0 else 12.5)
        for el in x
    ]

def function3(x):
    return [
        (el if el <= 2.5 else 5 - el) if 0 <= el <= 5 else 0
        for el in x
    ]

def function3_INT(x):
    return [
        ((1/2)*el**2 if el <= 2.5 else 5*el - (1/2)*el**2 ) if 0 <= el <= 5 else (0 if el < 0 else 12.5)
        for el in x
    ]

def function4(x):
    return [
        (2.5 if el <= 2.5 else 5 ) if 0 <= el <= 5 else 0
        for el in x
    ]

def function4_INT(x):
    return [
        (2.5*el if el <= 2.5 else 5 *el) if 0 <= el <= 5 else (0 if el < 0 else 25)
        for el in x
    ]


x = np.arange(-10, 10.01, 0.01)

fig, axs = plt.subplots(3, 2, figsize=(12, 18))

axs[0, 0].plot(x, function1(x))
axs[0, 0].set_title('Function 1 PDF')

axs[0, 1].plot(x, function1_INT(x))
axs[0, 1].set_title('Function 1 CDF')

axs[1, 0].plot(x, function3(x))
axs[1, 0].set_title('Function 2 PDF')

axs[1, 1].plot(x, function3_INT(x))
axs[1, 1].set_title('Function 2 CDF')

axs[2, 0].plot(x, function4(x))
axs[2, 0].set_title('Function 4 PDF')

axs[2, 1].plot(x, function4_INT(x))
axs[2, 1].set_title('Function 4 CDF')

plt.tight_layout()
plt.show()









