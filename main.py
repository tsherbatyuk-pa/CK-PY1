class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        """
        Создание и подготовка к работе обьекта "Книга"
        :param name: Название книги
        :param author: Имя автора
        >>> book = Book("Букварь", "Без автора")  # инициализация экземпляра класса
        """

        self._name = name
        self._author = author

        @property
        def name(self):
            return self._name

        @property
        def author(self):
            return self._author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    """Класс бумажной книги (дочерний класс Книги)"""
    def __init__(self, name: str, author: str, pages: int):
        """
        Создание и подготовка к работе класса "Бумажная книга"
        :param name: Название книги
        :param author: Имя автора
        :param pages: Количество страниц
        >>> book = Book("Букварь", "Без автора", 1)  # инициализация экземпляра класса
        """
        super().__init__(name, author)

        self.pages = pages
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = pages


    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"


class AudioBook(Book):
    """Класс аудиокниги (дочерний класс Книги)"""
    def __init__(self, name: str, author: str, duration: float):
        """
        Создание и подготовка к работе класса "Аудиокнига"
        :param name: Название книги
        :param author: Имя автора
        :param duration: Длительность
        >>> book = Book("Букварь", "Без автора", 1.1)  # инициализация экземпляра класса
        """
        super().__init__(name, author)
        if not isinstance(duration, float):
            raise TypeError("Длительность аудиокниги должна быть типа float")
        if duration <= 0:
            raise ValueError("Длительность аудиокниги должна быть положительным значением")
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"

if __name__ == '__main__':
    book_base = Book("Букварь", "Без автора")
    print(book_base.__str__())
    print(book_base.__repr__())

    book_paper = PaperBook("Алфавит", "Нет автора", 1)
    print(book_paper.__str__())
    print(book_paper.__repr__())

    book_audio = AudioBook("Азбука", "-", 1.1)
    print(book_audio.__str__())
    print(book_audio.__repr__())