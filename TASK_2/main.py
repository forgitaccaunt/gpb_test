# в наличии список множеств. внутри множества целые числа
m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]

# Задание: посчитать 
#  1. общее количество чисел
#  2. общую сумму чисел
#  3. посчитать среднее значение
#  4. собрать все множества в один кортеж
# *написать решения в одну строку

count_num = sum(len(seq) for seq in m)
total_sum = sum(sum(seq) for seq in m)
average_num = total_sum / count_num
big_tuple = tuple(num for seq in m for num in seq)
