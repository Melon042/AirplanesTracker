from src.api import APIAdapter
from src.utils import parse_opensky_response
from src.airplane import Airplane



def user_interaction():
    """Функция для взаимодействия с пользователем через консоль"""

    country_for_search = input("Введите название страны, на территории которой нужно найти самолёты (латиницей): ")

    api_adapter = APIAdapter()
    response = api_adapter.get_airplanes(country_for_search)
    parsed_response = parse_opensky_response(response)
    planes = [Airplane.from_api_response_to_object(state) for state in parsed_response]

    to_sort_top_altitude = input("\nХотите отобразить топ самолётов по высоте полёта? (да/нет) ").lower() == "да"
    if to_sort_top_altitude:
        n_top_altitude = int(input("\nТоп сколько самолётов по высоте полёта отобразить? "))

    to_sort_country_of_reg = input("\nХотите отсортировать самолёты по стране регистрации? (да/нет) ").lower() == "да"
    if to_sort_country_of_reg:
        query_country_of_reg = input("\nПо какой стране регистрации отобразить самолёты? ")


    if to_sort_country_of_reg:
        planes = [p for p in planes if p.country_of_registration == query_country_of_reg]

    if to_sort_top_altitude:
        planes = sorted(planes, key=lambda p: p.altitude, reverse=True)[:n_top_altitude]


    if len(planes):
        print(f"По заданным параметрам найдено самолётов: {len(planes)}!")
        for counter, plane in enumerate(planes, 1):
            print(f"{counter}.\n{plane}\n\n")
    else:
        print("Самолётов по заданным параметрам не найдено.")












