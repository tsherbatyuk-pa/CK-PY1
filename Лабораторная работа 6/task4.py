import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, delimiter=',', new_line='\n') -> list[dict]:  # Входящие аргументы
    with open(filename, 'r', encoding='utf-8') as f:  # Открываю файл
        headers = f.readline().rstrip(new_line).split(delimiter)  # Читаю заголовки, удаляю символ переноса, разделяю
        #print(headers)  # проверяю корректность вывода
        # Читаю остальной файл, удаляю символ переноса, разделяю. Список кортежей из двух списков (заголовки и строки)
        json_output = [dict(zip(headers, row.rstrip(new_line).split(delimiter))) for row in f]
        #print(json_output) проверяю корректность вывода
    return json.dumps(json_output, indent=4)  # Сериализуем в JSON


print(csv_to_list_dict(INPUT_FILE))
# Конец программы (последняя строка для GitHub)