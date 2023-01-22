import doctest


class Time:
    def __init__(self, current_hour: int, current_minute: int):
        """
        Создание и подготовка к работе объекта "Часы"

        :param current_hour: Текущий час
        :param current_minute: Текущая минута
        >>> time = Time (14, 10)  # инициализация экземпляра класса
        """
        if not isinstance(current_hour, int):
            raise TypeError("Часы записываются в формате целого числа (тип int)")
        if current_hour < 0:
            raise ValueError("Значение часа должно быть неотрицательным")
        if current_hour >= 24:
            raise ValueError("В сутках 24 часа, максимальное количество часов на циферблате - 23")
        self.current_hour = current_hour

        if not isinstance(current_minute, int):
            raise TypeError("Минуты записываются в формате целого числа (тип int)")
        if current_minute < 0:
            raise ValueError("Значение минут должно быть неотрицательным числом")
        if current_minute >= 60:
            raise ValueError("В часе 60 минут, максимальное количество минут на циферблате - 59")
        self.current_minute = current_minute

    def current(self) -> str:
        """
        Вывод текущего времени в текстовом формате.

        :return: Текущее время (введено в экземпляре) в формате:"ХХ часов XX минут"

        Примеры:
        >>> time = Time(10, 30)
        >>> time.current()
        """
        ...

    def daytime(self) -> str:
        """
        Функция обьявляет, какое время суток сейчас

        :return: Время суток в формате "Утро", "День", "Вечер", "Ночь"

        Примеры:
        >>> time = Time(20, 40)
        >>> time.daytime()
        """
        ...


class Room:
    def __init__(self, room_number: int, amount_place: int, amount_students: int):
        """
        Создание и подготовка к работе обьекта "Комната общежития"

        :param room_number: номер комнаты
        :param amount_place: количество мест в комнате
        :param amount_students: количество человек в комнате

        Примеры:
        >>> room_416 = Room(416, 4, 2)
        """
        if not isinstance(room_number, int):
            raise TypeError("Номер комнаты должен быть типа int")
        if room_number <= 0:
            raise ValueError("Номер комнаты должен быть положительным числом")
        if room_number > 570:
            raise ValueError("Максимальный номер комнаты - 570")
        self.room_number = room_number

        if not isinstance(amount_place, int):
            raise TypeError("Количество мест в комнате должно быть типа int")
        if amount_place <= 0:
            raise ValueError("Количество мест должно быть положительным числом")
        if amount_place > 4:
            raise ValueError("Максимальное количество мест в комнате - 4")
        self.amount_place = amount_place

        if not isinstance(amount_students, int):
            raise TypeError("Количество студентов в комнате должно быть типа int")
        if amount_students <= 0:
            raise ValueError("Количество студентов должно быть положительным числом")
        if amount_students > amount_place:
            raise ValueError("Максимальное количество студентов в комнате равно количеству мест в комнате")
        self.amount_students = amount_students

    def is_empty_room(self) -> bool:
        """
        Функция проверяет, является ли комната пустой

        :return: Является ли комната пустой

        Примеры:
        >>> room_505 = Room(505, 1, 1)
        >>> room_505.is_empty_room()
        """
        ...

    def add_student_to_room(self, add_student: int) -> None:
        """
        Заселение студентов в комнату.

        :param add_student: Количество заселяемых студентов

        :raise ValueError: Если количество заселяемых студентов превышает свободныt местf в комнате - вызываем ошибку

        Примеры:
        >>> room_416 = Room(416, 4, 2)
        >>> room_416.add_student_to_room(2)
        """
        if not isinstance(add_student, int):
            raise TypeError("Количество заселяемых студентов должно быть типа int")
        if add_student <= 0:
            raise ValueError("Заселяемое количество студентов должно быть положительным")
        if add_student > self.amount_place - self.amount_students:
            raise ValueError("Заселяемое количество студентов должно быть не меньше свободных мест")
        ...


class Diary:
    def __init__(self, max_letter_per_paper: int, amount_papers: int, text: str):
        """
        Создание и подготовка к работе обьекта "Ежедневник"

        :param max_letter_per_paper: Максимальное количество символов на странице
        :param amount_papers: Количество страниц
        :param text: Записанный текст в ежедневнике

        Примеры:
        >>> diary_pavel = Diary(1800, 24, "Покупка продуктов")
        """
        if not isinstance(max_letter_per_paper, int):
            raise TypeError("Максимальное количество символов на странице должно быть типа int")
        if max_letter_per_paper < 50:
            raise ValueError("Максимальное количество символов на странице должно быть не меньше 50")
        self.max_letter_per_paper = max_letter_per_paper

        if not isinstance(amount_papers, int):
            raise TypeError("Количество страниц в ежедневнике должно быть типа int")
        if amount_papers < 10:
            raise ValueError("Количество страниц в ежедневнике должно быть не меньше 10")
        self.amount_papers = amount_papers

        if not isinstance(text, str):
            raise TypeError("Текст записи в ежедневнике должен быть типа str")
        self.text = text

    def print_text(self, add_text: str) -> None:
        """
        Добавление записи в ежедневник.

        :param add_text: Текст записи в ежедневник

        Примеры:
        >>> diary_pavel = Diary(1800, 48, "Домашнее задание")
        >>> diary_pavel.print_text("Почистить зубы")
        """
        self.text += add_text

    def delete_papers(self, amount_deleted_papers: int) -> None:
        """
        Метод "вырывает" (удаляет) страницы из ежедневника

        :param amount_deleted_papers:

        Примеры:
        >>> diary_misha = Diary(2000, 48, "Ананасы, Бананы")
        >>> diary_misha.delete_papers(3)  # метод вырывает 3 страницы
        """
        if not isinstance(amount_deleted_papers, int):
            raise TypeError("Количество вырываемых страниц должно быть типа int")
        if amount_deleted_papers > self.amount_papers:
            raise ValueError("Количество вырываемых страниц должно быть не больше суммарного количества страниц")
        self.amount_papers -= amount_deleted_papers


if __name__ == "__main__":
    doctest.testmod()
# Конец программы (последняя строка для GitHub)
