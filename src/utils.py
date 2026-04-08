def parse_opensky_response(response: dict) -> list[list]:
    """Преобразует полный ответ OpenSky API в список списков с данными самолётов"""
    states = response.get("states", [])
    return states
