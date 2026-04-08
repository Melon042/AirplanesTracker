from src.utils import parse_opensky_response


class TestUtils:
    def test_parse_valid(self):
        data = {"time": 123, "states": [["id1", "CS1", "RU"], ["id2", "CS2", "US"]]}
        result = parse_opensky_response(data)
        assert len(result) == 2
        assert result[0][0] == "id1"

    def test_parse_empty_or_missing(self):
        assert parse_opensky_response({}) == []
        assert parse_opensky_response({"time": 0}) == []
