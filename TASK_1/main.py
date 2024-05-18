'''# ============================================ №1
# имеется текстовый файл file.csv, в котром разделитель полей с данными: | (верт. черта)
# пример ниже содержит небольшую часть этого файла(начальные 3 строки, включая строку заголовков полей)

lastname|name|patronymic|date_of_birth|id
Фамилия1|Имя1|Отчество1 |21.11.1998   |312040348-3048
Фамилия2|Имя2|Отчество2 |11.01.1972   |457865234-3431

# Задание
# 1. Реализовать сбор уникальных записей
# 2. Случается, что под одиннаковым id присутствуют разные данные - собрать отдельно такие записи
'''
import csv
from collections import Counter


unique_row = []
dublicate_row = []
id_counter = Counter()

# Собираем уникальные записи в список unique_row
# Дубликаты помещаем в список dublicate_row
with open('TASK_1/file.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='|')
    headers = next(reader)
    for row in reader:
        if row not in unique_row:
            unique_row.append(row)
        else:
            dublicate_row.append(row)
        # Используем Counter для подсчета количества записей с каждым id
        id_counter.update([row['id']])

# Разделение списка на два: с уникальными id и повторяющимися
unique_id = []
doublicate_id = []

for row in unique_row:
    if id_counter[row['id']] == 1:
        unique_id.append(row)
    else:
        doublicate_id.append(row)
