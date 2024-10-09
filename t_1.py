
def xor(a,b):
    return True if {a, b} == {True, False} else False

# ----------------------------------------------------------------------------------

def combat(health, damage):
    return (health - damage) if health > damage else 0

def combat_best(health, damage):
    return max(0, health-damage)


# ----------------------------------------------------------------------------------
def get_age(age):
    return int(age[0])
    # test.assert_equals(get_age("2 years old"), 2)
    # test.assert_equals(get_age("4 years old"), 4)
    # test.assert_equals(get_age("5 years old"), 5)
    # test.assert_equals(get_age("7 years old"), 7)

# print(type(get_age("2 years old")))
# print(get_age("7 years old"))

# ----------------------------------------------------------------------------------

def solution(a, b):
    temp = [a, b]
    temp.sort(key=len)
    return temp[0] + temp[1] + temp[0]

def solution_best(a, b):
    a, b = sorted((a, b), key=len)
    return a + b + a

# print(solution_best('45', '1') == '1451')
# print(solution_best('13', '200') == '1320013')
# print(solution_best('Soon', 'Me') == 'MeSoonMe')
# print(solution_best('U', 'False') == 'UFalseU')

# ----------------------------------------------------------------------------------
def narcissistic_1(value):
    temp = 0
    value_str = str(value)
    value_len = len(value_str)
    for i in value_str:
        temp += int(i) ** value_len
    return True if temp == value else False


def narcissistic(value):
    return value == sum(int(i) ** len(str(value)) for i in str(value))



# test.assert_equals(narcissistic(7), True, '7 is narcissistic');
# test.assert_equals(narcissistic(371), True, '371 is narcissistic');
# test.assert_equals(narcissistic(122), False, '122 is not narcissistic')
# test.assert_equals(narcissistic(4887), False, '4887 is not narcissistic')

# ----------------------------------------------------------------------------------
def find_outlier(integers):
    res = None
    if sum(i % 2 for i in integers[:3]) <= 1:
        for i in integers:
            if i % 2 != 0:
              res = i
              break
    else:
        for i in integers:
            if i % 2 == 0:
              res = i
              break
    return res
#
# test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
#         test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
#         test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)

# odd - нечетные, even - четные

# print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
# print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))


# a = [2, 0, 3, 7, 9]
# print(a[:3])
# if sum(i % 2 for i in a[:3]) <= 1:
#     print('ЧЕтные')
# else:
#     print('net')