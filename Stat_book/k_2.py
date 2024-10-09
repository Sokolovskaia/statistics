import pandas as pd
import matplotlib.pyplot as plt


df_1 = pd.read_csv('states.csv',
                   sep=',',     # определить разделитель
                   # index_col=['state'],     # назначить столбец индексом
                   # usecols=['input', 'output', 'ulperrortol']       # фильтр, какие столбцы импортировать
                   )

# print(df_1.head())

# fig, ax = plt.subplots(figsize=(10, 6))
# ax.scatter(x=df_1['hs_grad'], y=df_1['poverty'])
# plt.xlabel("Среднее образование (%)")
# plt.ylabel("Бедность (%)")
#
# plt.show()

poverty = list(pd.Series(df_1['poverty']))
hs_grad = list(pd.Series(df_1['hs_grad']))

# Среднее mean
poverty_mean = sum(poverty) / len(poverty)
hs_grad_mean = sum(hs_grad) / len(hs_grad)

# st dev Стандартное отклонение
def variance_2(data):
    n = len(data)
    return (1 / (n - 1)) * sum([(i - sum(data)/n)**2 for i in data])


poverty_st_dev = variance_2(poverty)**0.5
hs_grad_st_dev = variance_2(hs_grad)**0.5
# print('poverty_st_dev', poverty_st_dev)
# print('hs_grad_st_dev', hs_grad_st_dev)

poverty_min = min(poverty)
poverty_max = max(poverty)
hs_grad_min = min(hs_grad)
hs_grad_max = max(hs_grad)


# Кэффициент корреляции
def correlation_coefficient(x, y):
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    return (sum([(i - x_mean) * (j - y_mean) for i, j in zip(x, y)]) /
            ((sum([(x_mean - i) ** 2 for i in x]) * sum([(y_mean - j) ** 2 for j in y])) ** 0.5))


# коэффициент b1
b_1 = (poverty_st_dev / hs_grad_st_dev) * correlation_coefficient(poverty, hs_grad)
# коэффициент b0
b_0 = poverty_mean - b_1 * hs_grad_mean

# print('b1 ', b_1)
# print('b0 ', b_0)
# Линия регрессии
# y^ = 64,78 - 0,62 * hs_grad


# std error Стандартная ошибка
poverty_predict = [(b_0 + b_1 * x) for x in hs_grad]  # y predict

# стандартное отклонение остатков
MSE = (sum([(y - y_pred)**2 for y, y_pred in zip(poverty, poverty_predict)]) / (len(poverty_predict)-2))**0.5

# стандартные ошибки параметров регрессионной модели
b_0_std_error = MSE * (1/len(hs_grad) + (hs_grad_mean**2 / sum([(i - hs_grad_mean)**2 for i in hs_grad])))**0.5
b_1_std_error = MSE * (1 / sum([(i - hs_grad_mean)**2 for i in hs_grad]))**0.5


# print(b_0_std_error)
# print(b_1_std_error)

# t-value
t_b0 = b_0 / b_0_std_error
t_b1 = b_1 / b_1_std_error

# print('t_b0 ', t_b0)
# print('t_b1', t_b1)

# Multiple R-squared Коэффициент детерминации
r_squared = correlation_coefficient(poverty, hs_grad)**2


# F-statistic
F = correlation_coefficient(poverty, hs_grad)**2 / (1 - correlation_coefficient(poverty, hs_grad)**2) * (len(poverty) -2)


# p_value  можно посмотреть по таблице (Указать обе степени свободы)
import scipy.stats as stats
p_val = stats.f.sf(F, 1, 49)

# y^ = 64,78 - 0,62 * hs_grad


print(7.5 + 2.199)

