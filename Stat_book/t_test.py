# Одновыборочный t-тест
# Двухвыборочный t-тест & тест Уэлча

import pandas as pd
from scipy.stats import ttest_1samp



sample = [7, 8, 9, 13, 10, 9, 9, 10, 9, 11, 12, 8, 9, 11, 10, 9, 10]

# Проведем одновыборочный t-тест с помощью .ttest_1samp с нулевой гипотезой о том, что 𝜇=9.71:
for_p_1 = ttest_1samp(sample, 9.71)

# Полученное значение p-value = 0,8646 сильно больше 0,05, поэтому у нас недостаточно оснований,
# чтобы отвергнуть нулевую гипотезу и утверждать, что математическое ожидание генеральной совокупности
# на самом деле отличается от 9,71.

# _________________________________________________________

"""
Проведите одновыборочный t-тест о равенстве математического ожидания ГС 
значений веса мужчин на острове Джерси значению 86.44. 
У нас есть данные по выборке, состоящей из 40 мужчин острова Джерси. 
Выборочное среднее равно 83.55, стандартное отклонение 7.74. 
Выведите полученное значение p-value (pvalue) на экран, округлив до 5 знаков после запятой.
"""

import pandas as pd
import numpy as np


weight = np.array([
    100, 82, 92, 88, 78, 85, 89, 79, 61, 87, 89, 87, 89, 86, 79, 78, 78, 85, 89, 79, 61, 87, 92, 88,
    78, 85, 79, 78, 78, 85, 101, 87, 89, 86, 79, 78, 78, 85, 89, 79])
sd = 7.74
n = 40

t = (sum(weight) / len(weight) - 86.44) / (sd / (n**0.5))
res = ttest_1samp(weight, 86.44)

for_p_2 = ttest_1samp(weight, 86.44).pvalue.round(5)
# _________________________________________________________

"""
Проведите одновыборочный t-тест о равенстве мат ожидания значений изменения индекса S&P 500 значению 0.00087. 
Известная нам выборка состоит из 1254 значений изменений индекса S&P 500. 
Выведите полученное значение t-статистики (statistic) на экран, округлив до 5 знаков после запятой.
"""
df_1 = pd.read_csv('SP_500_returns.csv', sep=';')

def solution_1(A): # A - некий датафрейм
    x = ttest_1samp(A['Return_SP_500'], 0.00087).statistic.round(5)
    return x

# print(solution_1(df_1))


# _________________________________________________________
# Двухвыборочный t-тест & тест Уэлча

sample_x = [7, 8, 9, 13, 10, 9, 9, 10, 9, 11, 12, 8, 9, 11, 10, 9, 10]
sample_y = [9, 12, 11, 11, 12, 8, 7, 9, 8, 10, 11, 10, 9, 10, 11, 9, 8]

# Проверим выборочные дисперсии:
var_x = np.var(sample_x)
var_y = np.var(sample_y)

# Предпосылка о гомогенности дисперсий соблюдается.
# Можем проводить стандартный двухвыборочный t-тест для независимых выборок с помощью ttest_ind
# с нулевой гипотезой о том, что 𝜇𝑥=𝜇𝑦


from scipy.stats import ttest_ind


res_test = ttest_ind(sample_x, sample_y)

# Полученное значение p-value = 0,909 сильно больше 0,05, поэтому у нас недостаточно оснований,
# чтобы отвергнуть нулевую гипотезу о равенстве математических ожиданий двух генеральных совокупностей.


# _________________________________________________________

# Есть также вариант проведения двухвыборочного t-теста для сравнения двух независимых выборок между собой
# путем задания характеристик каждой из двух выборок
# (mean_x = 65, sd_x = 7, n_x = 1000 и mean_x = 72, sd_x = 9, n_x = 1000) с помощью ttest_ind_from_stats:

from scipy.stats import ttest_ind_from_stats

s = ttest_ind_from_stats(65, 7, 1000, 72, 9, 1000)

"""
Оцените гомогенность дисперсий. 
Выведите отношение большей выборочной дисперсии к меньшей выборочной дисперсии на экран, 
округлив полученное значение до 5 знаков после запятой.
"""



import pandas as pd

df_2 = pd.DataFrame({
    'Year': [1971, 1972, 2019, 2020],
    'China': [1.995611, 1.849711, 2.563502, 1.434195],
    'US': [3.073314, 0.841075, 2.473712, -1.408486]})
# print(df)

# var_China = np.var(df_2['China'])
# var_US = np.var(df_2['US'])
# x = var_US / var_China if var_US >= var_China else var_China / var_US
#
# print(x)

def solution_2(A): # A - некий датафрейм
    var_China = np.var(A['China'])
    var_US = np.var(A['US'])
    x = var_US / var_China if var_US >= var_China else var_China / var_US
    return round(x, 5)

for_p_3 = solution_2(df_2)


# _________________________________________________________
"""
Есть две выборки значений среднегодовой доходности банковского сектора в США и Китае с 1971 по 2019 год. 
Проведите необходимый t-тест на проверку равенства средних. 
Выведите значение p-value на экран, округлив полученное значение до 5 знаков после запятой.

"""

df_3 = pd.DataFrame({
    'Year': [1971, 1972, 2019, 2020],
    'China': [1.995611, 1.849711, 2.563502, 1.434195],
    'US': [3.073314, 0.841075, 2.473712, -1.408486]})

ress = ttest_ind(df_3.China, df_3.US)
for_p_4 = round(ress.pvalue, 5)

# _________________________________________________________


df = pd.DataFrame({
    'test': [29.07, 22.60, 25.22, 21.63, 22.83, 21.46, 23.77],
    'control': [29.91, 28.44, 30.82, 27.42, 20.14, 32.44, 18.99]})

from scipy.stats import kstest


# проверка дисперсий на гомогенность
var_test, var_control = np.var(df['test']), np.var(df['control'])

# если отношение большей дисперсии к меньшей меньше 4, то гомогенны
def homogenous(var_x, var_y):
    res = 'Yes' if max(var_x, var_y) / min(var_x, var_y) < 4 else 'No'
    print(res)

homogenous(var_test, var_control)


# проверка на нормальность тест Колмогорова-Смирнова

# print(kstest(df.test, 'norm'))
# print(kstest(df.control, 'norm'))



r = ttest_ind(df.test, df.control)
print(round(ttest_ind(df.test, df.control).pvalue, 5))