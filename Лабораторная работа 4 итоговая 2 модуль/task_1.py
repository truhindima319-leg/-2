class Arachnid:
    """
    Базовый класс для паукообразных.
    """
    def __init__(self, species: str, age: int, venomous: bool = False) -> None:
        """
        :param species: Вид паукообразного
        :param age: Возраст паукообразного
        :param venomous: наличие яда (ядовитый ли?)
        """
        self._species = species
        self._venomous = venomous
        self._age = max(0, age)  # Возраст не может быть отрицательным

    def danger_for_people(self) -> str:
        """
        Описывает, опасен ли этот вид для человека.

        :return: Строка с описанием опасности
        """
        if self._venomous:
            return "Опасен для человека, так как ядовит"
        return "Не опасен для человека"

    def __str__(self) -> str:
        """
        Строковое представление объекта.

        :return: Человекочитаемая строка
        """
        venom_status = "ядовит" if self._venomous else "не ядовит"
        return f"{self._species} (класс - Паукообразные): возраст {self._age} мес., {venom_status}"

    def __repr__(self) -> str:
        """
        Формальное представление объекта.

        :return: Строка для воссоздания объекта
        """
        return f"Arachnid(species='{self._species}', venomous={self._venomous}, age={self._age})"

    def hunt(self) -> str:
        """
        Метод охоты паукообразного
        :return: Строка с описанием процесса охоты
        """
        pass

class Spider(Arachnid):
    """
    Класс паука.
    """
    def __init__(self, web: bool, species: str, age: int, venomous: bool = False) -> None:
        """
        :param web: Использование паутины для охоты
        :param species: Вид паукообразного
        :param age: Возраст паукообразного
        :param venomous: Наличие яда (ядовитый ли?)
        """
        super().__init__(species, age, venomous)
        self._web = web

    def hunt(self) -> str:
        """
        Метод охоты для паука
        Не все пауки плетут паутину для того, чтобы охотиться
        :return: Строка с описанием процесса охоты паука
        """
        if self._web:
            return f"{self._species} плетет паутину и ждет добычу"
        else:
            return f"{self._species} не плетет паутину, а преследует добычу"

    def __str__(self) -> str:
        """
        Строковое представление паука.

        :return: Человекочитаемая строка
        """
        w_str = super().__str__()
        web_info = "плетет паутину" if self._web else "не плетет паутину"
        return f"{w_str}, {web_info}"

    def __repr__(self) -> str:
        """
        Формальное представление паука.

        :return: Строка для воссоздания объекта
        """
        return f"Spider(web='{self._web}', species='{self._species}', venomous={self._venomous}, age={self._age})"


if __name__ == "__main__":
    arachnid = Arachnid("Скорпион", 4, True)
    spider = Spider(False, "Паук-скакун", 4, False)

    print(arachnid)
    print(spider)

    print(arachnid.danger_for_people())
    print(spider.hunt())

    print([arachnid, spider])
