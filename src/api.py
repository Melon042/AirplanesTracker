from requests import get, Response
from abc import ABC, abstractmethod
from typing import Optional


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
    def _get_airplanes(self, country: str) -> None:
        """Получить информацию о самолётах в заданной стране"""
        pass


class APIAdapter(AbstractAPIAdapter):
    """Класс для работы с платформами nominatim.openstreetmap.org и opensky - network.org"""

    def __init__(self) -> None:
        """Инициализация объекта"""
        self._openstreetmap_url = 'https://nominatim.openstreetmap.org/search'
        self._opensky_url = 'https://opensky-network.org/api/states/all?'
        self._airplanes = None


    def _connect_to_api(self, url: str, params: dict, headers: Optional[dict] = None) -> Optional[Response]:
        """Метод подключения к API"""
        try:
            response = get(url=url, params=params, headers=headers)
            response.raise_for_status()
            return response
        except Exception:
            raise TypeError(f"Не удалось подключиться к API-сервису или сервис не отвечает")


    def _get_airplanes(self, country: str) -> None:
        """Получить информацию о самолётах в заданной стране"""

        # Headers с user-agent - обязательный параметр при запросе к nominatim.openstreetmap.
        headers_openstreetmap = {
            'User-Agent': 'test-app'}

        params_openstreetmap = {
            'country': country,
            'format': 'json',
            'limit': 1}

        response_openstreetmap = self._connect_to_api(
            url=self._openstreetmap_url,
            params=params_openstreetmap,
            headers=headers_openstreetmap)

        data = response_openstreetmap.json()
        geo_coordinates = data[0].get('boundingbox')

        params_opensky = {
            'lamin': geo_coordinates[0],
            'lamax': geo_coordinates[1],
            'lomin': geo_coordinates[2],
            'lomax': geo_coordinates[3]}

        response_opensky = self._connect_to_api(url=self._opensky_url, params=params_opensky)

        self._airplanes = response_opensky.json()
