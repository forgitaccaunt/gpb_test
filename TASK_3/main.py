# имеется список списков
a = [[1,2,3], [4,5,6]]

# Задание:
# сделать список словарей
b = [{'k1': 1, 'k2': 2, 'k3': 3}, {'k1': 4, 'k2': 5, 'k3': 6}]

# *написать решение в одну строку


b = [dict(zip(['k1', 'k2', 'k3'], lst)) for lst in a]
