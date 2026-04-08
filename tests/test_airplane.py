from src.airplane import Airplane


class TestAirplane:
    def test_creation(self):
        p = Airplane("id1", "Spain", "AER123  ", False, 250.5, 10000)
        assert p.country_of_registration == "Spain"
        assert p.call_sign == "AER123"
        assert p.velocity == 250.5

    def test_to_dict(self):
        p = Airplane("id1", "US", "EAGLE", True, 0, 0)
        d = p.to_dict()
        assert isinstance(d, dict)
        assert d["airplane_id"] == "id1"
        assert d["on_ground"] is True

    def test_from_api_response_to_object(self):
        raw = ["abc123", " EAGLE ", "US", 0, 0, 0, 0, 5000.0, False, 150.0, 0, 0, None, 0, "0000", False, 0]
        p = Airplane.from_api_response_to_object(raw)
        assert p.airplane_id == "abc123"
        assert p.call_sign == "EAGLE"
        assert p.altitude == 5000.0
        assert p.velocity == 150.0

    def test_comparisons(self):
        p1 = Airplane("1", "Rus", "X", False, 200, 5000)
        p2 = Airplane("2", "Rus", "Y", False, 300, 4000)
        assert p2 > p1
        assert p1 < p2
        assert p1.is_higher(p2)
        assert p2.is_lower(p1)

    def test_str(self):
        p = Airplane("1", "Rus", "X", False, 200, 5000)
        s = str(p)
        assert "В полёте" in s
