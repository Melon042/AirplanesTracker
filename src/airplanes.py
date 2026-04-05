from typing import Self


class Airplane:
    """Класс для работы с информацией о самолётах"""

    __slots__ = ('_airplane_id', '_country_of_registration', '_call_sign', '_on_ground', '_velocity', '_altitude')

    _airplane_id: str
    _country_of_registration: str
    _call_sign: str
    _on_ground: bool
    _velocity: float | int
    _altitude: float | int


    def __init__(self, airplane_id: str, country_of_registration: str, call_sign: str, on_ground: bool,
                 velocity: float | int, altitude: float | int) -> None:
        """Инициализация объекта"""

        self._airplane_id = self._validate_airplane_id(airplane_id)
        self._country_of_registration = self._validate_country_of_registration(country_of_registration)
        self._call_sign = self._validate_call_sign(call_sign)
        self._on_ground = self._validate_on_ground(on_ground)
        self._velocity = self._validate_velocity(velocity)
        self._altitude = self._validate_altitude(altitude)


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
        return self._velocity > other._velocity


    def __lt__(self, other: Self) -> bool:
        """Сравнивает скорость (меньше)"""
        return self._velocity < other._velocity


    def is_higher(self, other: Self) -> bool:
        """Сравнивает высоту (больше)"""
        return self._altitude > other._altitude


    def is_lower(self, other: Self) -> bool:
        """Сравнивает высоту (меньше)"""
        return self._altitude < other._altitude

    def to_dict(self) -> dict:
        """Преобразует объект в словарь"""
        return {
            "airplane_id": self._airplane_id,
            "country_of_registration": self._country_of_registration,
            "call_sign": self._call_sign,
            "on_ground": self._on_ground,
            "velocity": self._velocity,
            "altitude": self._altitude}
