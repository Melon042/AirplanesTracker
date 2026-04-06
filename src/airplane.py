from typing import Self


class Airplane:
    """Класс для работы с информацией о самолётах"""

    __slots__ = ('airplane_id', 'country_of_registration', 'call_sign', 'on_ground', 'velocity', 'altitude')

    airplane_id: str
    country_of_registration: str
    call_sign: str
    on_ground: bool
    velocity: float | int
    altitude: float | int


    def __init__(self, airplane_id: str, country_of_registration: str, call_sign: str, on_ground: bool,
                 velocity: float | int, altitude: float | int) -> None:
        """Инициализация объекта"""

        self.airplane_id = self._validate_airplane_id(airplane_id)
        self.country_of_registration = self._validate_country_of_registration(country_of_registration)
        self.call_sign = self._validate_call_sign(call_sign)
        self.on_ground = self._validate_on_ground(on_ground)
        self.velocity = self._validate_velocity(velocity)
        self.altitude = self._validate_altitude(altitude)

    @classmethod
    def from_api_response_to_object(cls, data: list) -> Self:
        """Создаёт экземпляр класса из ответа API OpenSky (из элемента списка "states")"""

        return cls(
            airplane_id=data[0],
            country_of_registration = data[2],
            call_sign = data[1],
            on_ground = data[8],
            velocity = data[9] if data[9] is not None else 0,
            altitude = data[7] if data[7] is not None else 0)

    def __str__(self) -> str:
        """Человекочитаемое представление"""
        on_ground = "На земле" if self.on_ground else "В полёте"
        return (f"Позывной: {self.call_sign}\nID: {self.airplane_id}\n"
                f"Страна регистрации: {self.country_of_registration}\nСтатус: {on_ground}\n"
                f"Высота: {self.altitude}\nСкорость: {self.velocity}")



    @staticmethod
    def _validate_airplane_id(value: str) -> str:
        """Валидация airplane_id по типу данных"""
        if not isinstance(value, str):
            raise TypeError(f"airplane_id должен быть строкой, получено: {type(value)}")
        return value

    @staticmethod
    def _validate_country_of_registration(value: str) -> str:
        """Валидация country_of_registration по типу данных"""
        if not isinstance(value, str):
            raise TypeError(f"country_of_registration должен быть строкой, получено: {type(value)}")
        return value

    @staticmethod
    def _validate_call_sign(value: str) -> str:
        """Валидация call_sign по типу данных"""
        if not isinstance(value, str):
            raise TypeError(f"call_sign должен быть строкой, получено: {type(value)}")
        return value

    @staticmethod
    def _validate_on_ground(value: bool) -> bool:
        """Валидация on_ground по типу данных"""
        if not isinstance(value, bool):
            raise TypeError(f"on_ground должен быть булевым значением, получено: {type(value)}")
        return value

    @staticmethod
    def _validate_velocity(value: float | int) -> float | int:
        """Валидация velocity по типу данных"""
        if not isinstance(value, float | int):
            raise TypeError(f"velocity должен быть числом, получено: {type(value)}")
        return value

    @staticmethod
    def _validate_altitude(value: float | int) -> float | int:
        """Валидация altitude по типу данных"""
        if not isinstance(value, float | int):
            raise TypeError(f"altitude должен быть числом, получено: {type(value)}")
        return value


    def __gt__(self, other: Self) -> bool:
        """Сравнивает скорость (больше)"""
        return self.velocity > other.velocity


    def __lt__(self, other: Self) -> bool:
        """Сравнивает скорость (меньше)"""
        return self.velocity < other.velocity


    def is_higher(self, other: Self) -> bool:
        """Сравнивает высоту (больше)"""
        return self.altitude > other.altitude


    def is_lower(self, other: Self) -> bool:
        """Сравнивает высоту (меньше)"""
        return self.altitude < other.altitude

    def to_dict(self) -> dict:
        """Преобразует объект в словарь"""
        return {
            "airplane_id": self.airplane_id,
            "country_of_registration": self.country_of_registration,
            "call_sign": self.call_sign,
            "on_ground": self.on_ground,
            "velocity": self.velocity,
            "altitude": self.altitude}
