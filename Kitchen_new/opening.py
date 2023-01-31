import json


def read_file(file_name):  # функция для чтения файлов
    with open(file_name, 'r') as f:  # открытие файла в режиме чтения
        lines = f.readlines()  # чтение файла по строчно
        return lines


def read_json_file(json_name):  # функция для чтения json файлов
    with open(json_name, "r") as j:  # открытие файла в режиме чтения
        read = json.load(j)  # чтение данных из файла
        return read


def json_key(key_derivation):
    derivation = read_json_file(key_derivation)
    for _ in derivation.keys():
        return list(derivation.keys())
