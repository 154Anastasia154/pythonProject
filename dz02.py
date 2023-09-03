#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
#Выведите минимальное количество монет, которые нужно перевернуть

# def min_flips(coins):
#     heads_count = coins.count('H')
#     tails_count = coins.count('T')
#     min_flips = min(heads_count, tails_count)
#     return min_flips

# # Пример использования
# coins = ['H', 'T', 'T', 'H', 'H']
# min_flips_needed = min_flips(coins)
# print(f"Минимальное количество монет, которые нужно перевернуть: {min_flips_needed}")


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# def solve_petyas_puzzle(S, P):
#     for x in range(1, 1001):
#         y = S - x
#         if x * y == P:
#             return x, y

# # Заданные подсказки от Пети
# sum_hint = 25
# product_hint = 46

# # Решение задачи
# x_solution, y_solution = solve_petyas_puzzle(sum_hint, product_hint)

# # Вывод ответа
# print(f"Задуманные числа: {x_solution} и {y_solution}")


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

# def print_powers_of_two(n):
#     for power in range(int(n.bit_length())):
#         if 2 ** power > n:
#             break
#         print(2 ** power)

# # Пример использования
# print_powers_of_two(37)