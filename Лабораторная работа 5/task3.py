import random  # импортируем модуль рандом для дальнейшей генерации чисел


def get_unique_list_numbers(start_, end_, len_) -> list[int]:  # аргументы: начало, конец, размер диапазона
    list_ = []  # задаем пустой список для добавления элементов
    while len(list_) < len_:  # ограничиваем длину списка
        numb = random.randint(start_, end_)  # выбираем случайное число из указанного диапазона
        if numb not in list_:  # указываем условие уникальности
            list_.append(numb)  # добавляем в список в случае выполнения условия
    return list_


list_unique_numbers = get_unique_list_numbers(-10, 10, 15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
# Конец программы (последняя строка для GitHub)