import doctest

class Flat:
    def __init__(self, room_number: int, area: float):
        """
        Создание и подготовка к работе объекта "Стул"

        :param room_number: количество комнат в квартире
        :param area: площадь квартиры

        """
        if not isinstance(room_number, (int)):
            raise TypeError("Количество комнат в квартире должно быть типа int")
        if room_number <= 0:
            raise ValueError("Количество комнат в квартире не может быть меньше 0")
        self.room_number = room_number

        if not isinstance(area, (int, float)):
            raise TypeError("Площадь квартиры должно быть int или float")
        if area < 0:
            raise ValueError("Площадь квартиры не может быть отрицательным числом")
        self.area = area

    def is_empty_flat(self) -> bool:
        """
        Функция которая проверяет есть ли люди в квартире

        :return: Является ли квартира пустой

         Пример:
        >>> flat = Flat(3, 74.5)
        >>> flat.is_empty_flat()

        """
        ...

    def add_human_to_flat(self, human: int) -> None:
        """
        Добавление человека в квартиру.
        :param human: Количество добавляемых людей

        :raise ValueError: Если количество добавляемых людей превышает свободное место в квартире, то вызываем ошибку

        """
        if not isinstance(human, (int)):
            raise TypeError("Добавляемые люди должны быть типа int")
        if human < 0:
            raise ValueError("Добавляемые люди должны быть положительным числом")
        ...

class Magazine:
    def __init__(self, page_count: int, title_name: str):
        """
        Создание и подготовка к работе объекта "Журнал"

        :param page_count: количество страниц в журнале
        :param area: название журнала

        """
        if not isinstance(page_count, (int)):
            raise TypeError("Количество страниц журнала должно быть типа int")
        if page_count <= 0:
            raise ValueError("Количество страниц журнала не может быть меньше 0")
        self.page_count = page_count

        if not isinstance(title_name, (str)):
            raise TypeError("Название журнала должно быть str")
        if len(title_name) == 0:
            raise ValueError("Название журнала не может быть пустым")
        self.title_name = title_name

    def is_big_magazine(self) -> bool:
        """
        Функция которая проверяет толстый ли журнал

        :return: Является ли журнал толстым в плане страниц

         Пример:
        >>> magazine = Magazine(100, "Факты и правда")
        >>> magazine.is_big_magazine()
        """
        ...

    def age_of_magazine(self, age: int) -> int:
        """
        Рассчитывает сколько лет данному выпуску журнала
        :param current_year: Текущий год
        :return возраст выпуска в годах

        """

class Chair:
    def __init__(self, material: str, chair_back: bool, chair_legs: int):
        """
        Создание и подготовка к работе объекта "Стул"

        :param material: материал стула
        :param chair_back: есть ли спинка у стула
        :param chair_legs: количество ножек стула

        """
        if not isinstance(material, (str)):
            raise TypeError("Материал стула должеж быть типа str")
        if len(material) == 0:
            raise ValueError("Материал стула не может быть пустым")
        materials = ["дерево", "пластик", "металл"]
        if material not in materials:
            print(f"'{material}' - необычный материал для стула")
        self.material = material

        if not isinstance(chair_back, (bool)):
            raise TypeError("Наличие спинки у стула должно быть bool")
        self.chair_back = chair_back

        if not isinstance(chair_legs, (int)):
            raise TypeError("Количество ножек у стула должно быть int")
        if chair_legs <= 2:
            raise ValueError("Количество ножек у стула не может быть меньше 3")
        self.chair_legs = chair_legs

    def is_chair_is_for_school(self) -> bool:
        """
        Функция которая проверяет подходит ли стул для школы

        :return: Является ли стул подходящим для школы

         Пример:
        >>> chair = Chair("металл", False, 4)
        >>> chair.is_chair_is_for_school()

        """
        ...

    def type_of_chair(self) -> str:

        """
        Определение типа стула по параметрам
        :return тип стула в зависимости от характеристик
        Пример:
        >>> chair_1 = Chair("металл", True, 4)
        >>> chair_1.type_of_chair()

        """

if __name__ == "__main__":
    doctest.testmod(verbose=True)  # тестирование примеров, которые находятся в документации
