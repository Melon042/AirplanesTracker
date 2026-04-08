from abc import ABC, abstractmethod
from typing import Optional

from requests import Response, get


class AbstractAPIAdapter(ABC):
    """Абстрактный класс для работы с API сервисов nominatim.openstreetmap.org и opensky - network.org"""

    @abstractmethod
    def __init__(self) -> None:
        """Инициализация объекта"""
        pass

    @abstractmethod
    def _connect_to_api(self, url: str, params: dict, headers: Optional[dict] = None) -> Optional[Response]:
        """Метод подключения к API"""
        pass

    @abstractmethod
    def get_airplanes(self, country: str) -> dict:
        """Получить информацию о самолётах в заданной стране"""
        pass


class APIAdapter(AbstractAPIAdapter):
    """Класс для работы с платформами nominatim.openstreetmap.org и opensky - network.org"""

    def __init__(self) -> None:
        """Инициализация объекта"""
        self.__openstreetmap_url = "https://nominatim.openstreetmap.org/search"
        self.__opensky_url = "https://opensky-network.org/api/states/all?"

    def _connect_to_api(self, url: str, params: dict, headers: Optional[dict] = None) -> Optional[Response]:
        """Метод подключения к API"""
        try:
            response = get(url=url, params=params, headers=headers)
            response.raise_for_status()
            return response
        except Exception:
            raise TypeError("Не удалось подключиться к API-сервису или сервис не отвечает")

    def get_airplanes(self, country: str) -> dict:
        """Получить информацию о самолётах в заданной стране"""

        # Headers с user-agent - обязательный параметр при запросе к nominatim.openstreetmap.
        headers_openstreetmap = {"User-Agent": "test-app"}

        params_openstreetmap = {"country": country, "format": "json", "limit": 1}

        response_openstreetmap = self._connect_to_api(
            url=self.__openstreetmap_url, params=params_openstreetmap, headers=headers_openstreetmap
        )

        data = response_openstreetmap.json()
        geo_coordinates = data[0].get("boundingbox")

        params_opensky = {
            "lamin": geo_coordinates[0],
            "lamax": geo_coordinates[1],
            "lomin": geo_coordinates[2],
            "lomax": geo_coordinates[3],
        }

        response_opensky = self._connect_to_api(url=self.__opensky_url, params=params_opensky)

        result = response_opensky.json()
        return result
