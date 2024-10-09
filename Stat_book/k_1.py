# факториал
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res



# расчет числа перестановок
def p_1(n, k):
    return factorial(n) / factorial(n-k)


# расчет числа сочетаний
def c_1(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))


# формула Бернулли
"""  Вероятность того, что в 
n независимых испытаниях некоторое случайное событие наступит ровно m раз, 
p - вероятность наступления события"""
def bernoulli_distribution(m, n, p):
    return (c_1(n, m))*(p**m)*((1-p)**(n-m))


# расчет среднего
def average_average(data):
    return sum(data)/len(data)

# d = (100, 115, 93, 102, 97)
# print(average_average(d))




data = (6, 1, 4, 5, 2, 3)

import statistics
# медиана
statistics.median(data)

# дисперсия для генеральной совокупности
def variance_1(data):
    n = len(data)
    return (1 / n) * sum([(i - sum(data)/n)**2 for i in data])

# дисперсия для выборки
def variance_2(data):
    n = len(data)
    return (1 / (n - 1)) * sum([(i - sum(data)/n)**2 for i in data])


data_variance = [1, 2, 3, 4, 5]

# стандартное отклонение для генеральной совокупности
def standard_deviation_1(data):
    return variance_1(data)**0.5

# стандартное отклонение для выборки
def standard_deviation_2(data):
    return variance_2(data)**0.5

# print(variance_2(data_variance))
# print(standard_deviation_2(data_variance))

kv = standard_deviation_2(data_variance) / (sum(data_variance) / len(data_variance)) * 100

# print(kv)

# медиана

d = [1, 3, 5]


# _____________________________________________________________________________________

x = [490, 500, 530, 550, 580, 590, 600, 600, 650, 700]
y = [560, 500, 510, 600, 600, 620, 550, 630, 650, 750]

# Коэффициент корреляции Пирсона
def pearson_correlation_coefficient(x, y):
    x_avg = sum(x) / len(x)
    y_avg = sum(y) / len(y)
    ss_x = sum([(i - x_avg) ** 2 for i in x])
    ss_y = sum([(j - y_avg) ** 2 for j in y])
    ss_xy = sum([(i - x_avg) * (j - y_avg) for i, j in zip(x, y)])
    return ss_xy / ((ss_x * ss_y) ** 0.5)

# коэффициент детерминации
def determination_coefficient(x, y):
    return pearson_correlation_coefficient(x, y)**2

# проверка статистической значимости коэфф корреляции Пирсона:
r = pearson_correlation_coefficient(x, y)
t = r * (len(x) - 2)**0.5 / (1 - r**2)**0.5

a = [60, 62, 63, 65, 65, 67, 68, 70, 70, 71]
b = [103, 100, 98, 95, 110, 108, 104, 110, 97, 100]


k = pearson_correlation_coefficient(a, b)


from scipy import stats

z = (125-100)/15
for_p_1 = 1 - stats.norm.cdf(z)


# _____________________________________________
# Однофакторный дисперсионный анализ

vegetable = [151, 135, 137, 118, 132, 135, 131, 137, 121, 140, 152, 133, 151, 132, 139, 96]
fruits = [108, 94, 84, 87, 82, 79, 74, 73, 67, 78, 63, 90, 81, 96, 83, 89]
meet = [147, 138, 143, 135, 153, 137, 148, 140, 144, 146, 151, 145, 146, 147, 150, 144]

# среднее по группам
vegetable_avg = sum(vegetable) / len(vegetable)
fruits_avg = sum(fruits) / len(fruits)
meet_avg = sum(meet) / len(meet)

N = len(vegetable) + len(fruits) + len(meet)
total_avg = (sum(vegetable) + sum(fruits) + sum(meet)) / N

# между группами
MSb = (((vegetable_avg - total_avg)**2
       + (fruits_avg - total_avg)**2
       + (meet_avg - total_avg)**2) / 2) * len(vegetable)
# print('MSb = ', round(MSb, 2))


# внутри групп
vegetable_s = sum([(i - vegetable_avg)**2 for i in vegetable]) / (len(vegetable) - 1)
fruits_s = sum([(i - fruits_avg)**2 for i in fruits]) / (len(fruits) - 1)
meet_s = sum([(i - meet_avg)**2 for i in meet]) / (len(meet) - 1)

MSw = (vegetable_s + fruits_s + meet_s) / 3
# print('MSw = ', round(MSw, 2))


F = MSb / MSw
# print('F = ', round(F, 2))

# print(16*3 - 3)

# _____________________________________________
# Корреляция
x = [4, 5, 2, 3, 1]
y = [2, 1, 4, 3, 5]

import matplotlib.pyplot as plt
plt.scatter(x,y)
plt.show()


print((6/5)*0.5)