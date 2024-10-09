# QQ plot - графический анализ

import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import lognormal, randn

np.random.seed(0)
# Создаем выборку из 1000 значений, имеющих стандартное нормальное распределение
data = randn(1000)

# Строим QQ plot с reference line в виде прямой линии под 45 градусов
fig = sm.qqplot(data, line='45')
plt.show()
# _________________________________________________________

np.random.seed(0)
# Создаем выборку из 1000 значений, имеющих логнормальное распределение
data = lognormal(0, 1, 1000)

# Строим QQ plot с reference line в виде прямой линии под 45 градусов
fig = sm.qqplot(data, line='45')
plt.show()