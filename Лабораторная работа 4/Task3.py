def delete(list_, index=None):
    if index is None or index == -1:  # Если пользователь не указал индекс / указал -1
        return list_[:-1]  # То удаляем последний элемент списка
    else:  # Для всех остальных положительных и отрицательных индексов применима одна формула
        return list_[:index] + list_[(index + 1):]



print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]
# конец программы (последння строка для GitHub)