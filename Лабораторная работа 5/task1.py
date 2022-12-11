from pprint import pprint  # импортируем функцию pprint из модуля pprint
# Список из словарей для чисел в одну строку, задаем необходимую последовательность чисел с помощью команды range
pprint([{'bin': bin(dec_numb), 'dec': dec_numb, 'hex': hex(dec_numb), 'oct': oct(dec_numb)} for dec_numb in range(16)])
# Конец программы (последняя строка для GitHub)
