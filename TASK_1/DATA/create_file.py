'''
Модуль для создания csv файла.
'''
import csv
import random


# Заголовки csv файла
headers = ['lastname', 'name', 'patronymic', 'date_of_birth', 'id']


# Функция для генерации случайных данных
def generate_random_data():
    with open('TASK_1/DATA/people.txt', 'r', encoding='utf-8') as file1:
        people = random.choice(file1.readlines()).rstrip().split()
    with open('TASK_1/DATA/date.txt', 'r', encoding='utf-8') as file1:
        date = random.choice(file1.readlines()).rstrip()
    with open('TASK_1/DATA/id.txt', 'r', encoding='utf-8') as file1:
        id = random.choice(file1.readlines()).rstrip()
    return people[0], people[1], people[2], date, id[:10]


with open('TASK_1/file.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter='|')
    writer.writerow(headers)

    # Генерировать и записывать случайные данные
    for _ in range(25):
        data = generate_random_data()
        writer.writerow(data)
csvfile.close()
