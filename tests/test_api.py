from src.api import APIAdapter


class TestAPIAdapter:
    def test_real_api_call(self):
        """Реальный запрос к API Nominatim и OpenSky"""
        adapter = APIAdapter()
        result = adapter.get_airplanes("Spain")
        assert isinstance(result, dict)
        assert "states" in result
        assert isinstance(result["states"], list)
