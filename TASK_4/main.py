# Имеется папка с файлами
# Реализовать удаление файлов старше N дней


import os
from datetime import datetime


# Функция для проверки, старше ли файл N дней
def check_age(file_path: str, n_days: int):
    creation_time = os.path.getctime(file_path)
    creation_time = datetime.fromtimestamp(creation_time)
    age = (datetime.today() - creation_time).days
    return age > n_days


# Перебор всех файлов в директории и удаление тех, что старше n
def delete_old_files(dir_path: str, n_days: int):
    for file_name in os.listdir(dir_path):
        file_path = os.path.join(dir_path, file_name)
        if os.path.isfile(file_path) and check_age(file_path, n_days):
            os.remove(file_path)
            print('Файлы удалены')
    else:
        print('Нет подходящих файлов')


directory_path = input('Путь к папке: ')
n = input('Файлы старше <количество_дней>: ')
delete_old_files(directory_path, n)
