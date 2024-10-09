# Тест Шапиро-Уилка

from numpy.random import seed
from numpy.random import poisson
from scipy.stats import shapiro
import numpy as np


# инициализируем генератор псевдослучайных чисел
seed(0)

# создаем 100 значений, имеющих распределение Пуассона с лямбдой, равной 5
data = poisson(5, 100)

# запускаем тест Шапиро-Уилка на соответствие нашего распределения (data) нормальному распределению
f_p_1 = shapiro(data)


# _________________________________________________________

"""
Проверьте на нормальность выборку из 100 значений, распределенных стандартно нормально 
(генератор псевдослучайных чисел seed(0)).
 Используйте тест Шапиро-Уилка. Выведите полученное значение p-value на экран.
"""


from numpy.random import seed, standard_normal


seed(0)
for_p_1 = shapiro(standard_normal(100)).pvalue


# _________________________________________________________
""""
Проверьте на нормальность выборку из 10 000 значений, имеющих логнормальное распределение
со средним значением 1 и стандартным отклонением 13.22 (генератор псевдослучайных чисел seed(0)). 
Используйте тест Шапиро-Уилка. 
Выведите полученное значение статистики Шапиро-Уилка (statistic) на экран, округлив до 5 знаков после запятой.

"""
from numpy.random import lognormal

# Установка seed для генерации псевдослучайных чисел
seed(0)

# Генерация данных с логнормальным распределением
data = lognormal(1, 13.22, 10_000)

# Применение теста Шапиро-Уилка
stat, p_value = shapiro(data)

# Вывод значения статистики, округленного до 5 знаков
for_p_2 = round(stat, 5)




