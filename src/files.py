from abc import ABC, abstractmethod
from typing import Optional
from xml.dom import NotFoundErr

from pandas.io.common import file_path_to_url

from airplanes import (Airplane)
import os
import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).parent.parent


class AbstractAirplaneFile(ABC):
    """Абстрактный класс для работы с информацией о самолётах в файле"""

    @abstractmethod
    def __init__(self, filename: Optional[str]) -> None: #В дочерних классах необходимо указать filename по умолчанию.
        """Инициализация объекта"""
        self._filename = filename
        pass

    @abstractmethod
    def save_to_file(self, airplanes: list[Airplane]) -> None:
        """Метод для сохранения информации о самолётах в файл"""
        pass

    @abstractmethod
    def delete_data_from_file(self, airplanes: list[Airplane]) -> None:
        """Метод для удаления информации о самолётах из файла"""
        pass

    @abstractmethod
    def get_data_from_file(self, airplane_id: Optional[str] = None, country_of_registration: Optional[str] = None,
                           call_sign: Optional[str] = None, on_ground: Optional[bool] = None) -> list[dict] | None:
        """Метод для получения данных о самолётах из файла по указанным критериям"""
        pass


class AirplaneFileJson(AbstractAirplaneFile):
    """Класс для сохранения информации о самолётах в Json-файл."""

    def __init__(self, filename: str = "airplanes.json") -> None:
        """Инициализация объекта"""

        self._filename = filename
        self._filedir = os.path.join(PROJECT_ROOT, "data")
        self._filepath = os.path.join(self._filedir, filename)

        os.makedirs(self._filedir, exist_ok=True)


    def save_to_file(self, airplanes: list[Airplane]) -> None:
        """Метод для сохранения информации о самолётах в Json-файл"""

        if os.path.exists(self._filepath):
            with open(self._filepath, "r", encoding="utf-8") as f:
                old_data = json.load(f)
        else:
            old_data = []

        new_data = [airplane.to_dict() for airplane in airplanes]

        data_map = {airplane.get("_airplane_id"): airplane for airplane in old_data}

        for airplane in new_data:
            data_map[airplane.get("_airplane_id")] = airplane

        with open(self._filepath, "w", encoding="utf-8") as file:
            json.dump(list(data_map.values()), file, ensure_ascii=False, indent=4)


    def delete_data_from_file(self, airplanes: list[Airplane]) -> None:
        """Метод для удаления информации о самолётах из файла"""


        if not os.path.exists(self._filepath):
            print(f"Не удалось выполнить удаление. Файла {self._filename} не существует.")
            return None
        else:
            with open(self._filepath, "r", encoding="utf-8") as file:
                data = json.load(file)

        airplanes = [airplane.to_dict() for airplane in airplanes]

        keys_to_delete = [airplane["_airplane_id"] for airplane in airplanes]

        new_data = [airplane for airplane in data if airplane.get("_airplane_id") not in keys_to_delete]

        with open(self._filepath, "w", encoding="utf-8") as file:
            json.dump(new_data, file, ensure_ascii=False, indent=4)


    def get_data_from_file(self, airplane_id: Optional[str] = None, country_of_registration: Optional[str] = None,
                           call_sign: Optional[str] = None, on_ground: Optional[bool] = None) -> list[dict] | None:
        """Метод для получения данных о самолётах из файла по указанным критериям.
        Без указания критериев возвращает все данные из файла"""

        if not os.path.exists(self._filepath):
            print(f"Не удалось получить данные. Файла {self._filename} не существует.")
            return None

        with open(self._filepath, "r", encoding="utf-8") as file:
            data = json.load(file)

        filters = {
        "_airplane_id": airplane_id,
        "_country_of_registration": country_of_registration,
        "_call_sign": call_sign,
        "_on_ground": on_ground}

        filters = {key: value for key, value in filters.items() if value is not None}

        if not filters:
            return data

        result = [airplane for airplane in data
            if all(airplane.get(key) == value for key, value in filters.items())]
