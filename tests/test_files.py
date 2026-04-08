import os

from src.airplane import Airplane
from src.files import AirplaneFileJson

TEST_FILE = "test_airplanes.json"


class TestAirplaneFileJson:
    def setup_method(self):
        """Создаём объект и чистим файл перед каждым тестом"""
        self.saver = AirplaneFileJson(TEST_FILE)
        if self.saver._filepath.exists():
            os.remove(self.saver._filepath)

    def teardown_method(self):
        """Удаляем тестовый файл после завершения теста"""
        if self.saver._filepath.exists():
            os.remove(self.saver._filepath)

    def test_save_and_get_all(self):
        planes = [Airplane("1", "RU", "Sushka", False, 200, 5000), Airplane("2", "US", "EAGLE", True, 0, 0)]
        self.saver.save_to_file(planes)
        saved = self.saver.get_data_from_file()
        assert saved is not None
        assert len(saved) == 2
        assert saved[0].call_sign == "Sushka"

    def test_delete_by_callsign(self):
        planes = [Airplane("1", "RU", "Sushka", False, 200, 5000), Airplane("2", "US", "EAGLE", True, 0, 0)]
        self.saver.save_to_file(planes)
        to_del = self.saver.get_data_from_file(call_sign="EAGLE")
        assert len(to_del) == 1

        self.saver.delete_data_from_file(to_del)
        data = self.saver.get_data_from_file()
        assert data is not None and len(data) == 1

    def test_delete_all(self):
        planes = [Airplane("1", "RU", "Sushka", False, 200, 5000), Airplane("2", "US", "EAGLE", True, 0, 0)]
        self.saver.save_to_file(planes)
        self.saver.delete_all_from_file()
        data = self.saver.get_data_from_file()
        assert data == []
