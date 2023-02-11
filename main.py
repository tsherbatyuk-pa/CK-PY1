class Building:
    """Базовый класс: здание"""
    def __init__(self, name: str, functional: str, storeys: int, area: float, price: float):
        """
        Создание и подготовка к работе обьекта класса "Здание"
        :param name: Название здания - защищенный атрибут, название здания задается только в начале, остальные параметры могут меняться в ходе проверки информации
        :param functional: Функциональное назначение здания
        :param storeys: Этажность здания
        :param area: Площадь здания в кв.м
        :param price: Общая стоимость здания в долларах
        >>> building = Building (name="Название", functional="Функц.тип", storeys=2, area=1000.2, price=1000.2)
        """
        self._name = name  # делаем атрибут названия здания защищенным (пользователь не может его менять)
        self.functional = functional
        self.storeys = storeys
        self.area = area
        self.price = price

    @property  # защищаем атрибут названия здания
    def name(self) -> str:
        """Функция возвращает название здания"""
        return self._name

    def square_price(self) -> float:
        """
        Метод расчитывает стоимость 1 квадратного метра здания
        :return: Стоимость 1 квадратного метра здания
        >>> building = Building (name="Название", functional="Функц.тип", storeys=2, area=1000.2, price=1000.2)
        >>> building.square_price()
        """
        square_price = self.price/self.area
        return square_price

    def structural_analysis(self, region: int, step: float, length: float, width: float, height: float) -> dict:
        """
        Метод совершает конструктивный расчет здания и подбирает сечения элементов
        :param region: снеговой район
        :param step: шаг конструкций (м)
        :param length: длина здания (м)
        :param width: ширина здания (м)
        :param height: высота здания (м)
        :return: сечения элементов (ключ - элемент, значение - номер сечения)
        >>> building = Building (name="Название", functional="Функц.тип", storeys=2, area=1000.2, price=1000.2)
        >>> building.structural_analysis(region=1, step=6, length=24, width=12, height=8)
        """
        ...  # Выполнение расчета

    def __str__(self) -> str:  # строковое представление обьекта класса
        return f"Здание {self.name} {self.functional}. Этажность: {self.storeys}. Стоимость 1 кв.м: {self.square_price()}"

    def __repr__(self) -> str:  # формальное строковое представление объекта
        return f"{self.__class__.__name__}(name={self.name!r}, functional={self.functional!r}, storeys={self.storeys!r}, area={self.area!r}, price={self.price!r})"


class ModularBuilding(Building):  # Наследуемся от класса Building, в том числе метод square_price
    """Дочерний класс: модульное здание"""
    def __init__(self, name: str, functional: str, storeys: int, area: float, price: float, module_types: int, amount_modules: int):
        """
        Создание и подготовка к работе обьекта класса "Модульное здание"
        :param functional: Функциональное назначение здания
        :param storeys: Этажность здания
        :param area: Площадь здания
        :param price: Общая стоимость здания
        :param module_types: Количество типов модулей
        :param amount_modules: Общее количество модулей
        >>> building = Building (name="Название", functional="Функц.тип", storeys=2, area=1000.2, price=1000.2, module_types=2, amount_modules=30)
        """
        super().__init__(name, functional, storeys, area, price)
        self.module_types = module_types
        self.amount_modules = amount_modules

    def structural_analysis(self, region: int, step: float, length: float, width: float, height: float) -> dict:
        """
        Метод совершает конструктивный расчет здания и подбирает сечения элементов
        Метод базового класса перегружен, т.к. в него добавлены дополнительные конструктивные проверки (монтажные нагрузки)
        :param region: снеговой район
        :param step: шаг конструкций
        :param length: длина здания
        :param width: ширина здания
        :param height: высота здания
        :return: сечения элементов (ключ - элемент, значение - номер сечения)
        >>> building = Building (name="Название", functional="Функц тип", storeys=2, area=1000.2, price=1000.2, module_types=2, amount_modules=30)
        >>> building.structural_analysis(region=1, step=6, length=24, width=12, height=8)
        """
        ...  # добавление дополнительных конструкционных проверок

    def __str__(self):  # Строковое представление обьекта класса. Метод перегружен, т.к. добавлены новые параметры для модульного здания
        return f"Модульное здание {self.name} {self.functional}. Этажность: {self.storeys}. Стоимость 1 кв.м: {self.square_price()}. Типов модулей: {self.module_types}. Кол-во модулей: {self.amount_modules}"

    def __repr__(self):  # Формальное строковое представление объекта. Метод перегружен, т.к. добавлены атрибуты
        return f"{self.__class__.__name__}(name={self.name!r}, functional={self.functional!r}, storeys={self.storeys!r}, area={self.area!r}, price={self.price!r}, module_types={self.module_types!r}, amount_modules={self.amount_modules!r})"


# Проверка
burj_halifa = Building("Бурдж-Халифа", "Многофункциональное", 163, 344000, 1500000000)
print(burj_halifa.__str__())
print(burj_halifa.__repr__())
print(f"Стоимость кв.м {burj_halifa.name}", burj_halifa.square_price(), "долларов")

dean_street_461 = ModularBuilding("461 Dean Street", "Жилое", 32, 32516, 195096000, 225, 930)
print(dean_street_461.__str__())
print(dean_street_461.__repr__())
print(f"Стоимость кв.м. {dean_street_461.name}", dean_street_461.square_price(), "долларов")

print(f"Стоимость {burj_halifa.name} больше стоимости {dean_street_461.name}:", burj_halifa.price > dean_street_461.price, "Разница", burj_halifa.price-dean_street_461.price, "Долларов")

dean_street_461.storeys = 33
print(dean_street_461.__str__())

burj_halifa.name = "Эйфелева башня"
print(burj_halifa.name)  # вызов ошибки, атрибут нельзя изменять
