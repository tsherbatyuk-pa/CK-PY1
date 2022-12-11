from string import ascii_lowercase, ascii_uppercase, digits  # Импортируем указанные библиотеки
import random  # импортируем модуль рандом для дальнейшей генерации чисел


def get_random_password(len_) -> str:  # аргумент -- длина пароля
    population_ = ascii_uppercase + ascii_lowercase + digits  # последовательность допуст. символов
    list_ = random.sample(population_, len_)  # генерация пароля по указанной последовательности и длине
    return ''.join(list_)  # обьединяем элементы списка без разделителя


print(get_random_password(8))
# Конец программы (последняя строка для GitHub)