from src.airplane import Airplane
from src.api import APIAdapter
from src.files import AirplaneFileJson
from src.utils import parse_opensky_response


def user_interaction():
    """Функция для взаимодействия с пользователем через консоль"""

    json_saver = AirplaneFileJson()

    while True:
        print("\n1. Записать данные о самолетах в стране из API в файл")
        print("2. Показать все сохраненные самолеты")
        print("3. Найти самолеты по стране регистрации в сохраненных")
        print("4. Удалить самолет из сохраненных по позывному")
        print("5. Показать топ N самолётов по скорости из файла")
        print("6. Удалить все самолёты из файла")
        print("7. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            country = input("\nВведите страну (латиницей): ")

            api_adapter = APIAdapter()
            response = api_adapter.get_airplanes(country)
            parsed_response = parse_opensky_response(response)
            airplanes = [Airplane.from_api_response_to_object(state) for state in parsed_response]

            json_saver.save_to_file(airplanes)

            print(f"\nВ стране {country} найдено самолётов: {len(airplanes)}. " f"Данные добавлены/обновлены в файле.")

        elif choice == "2":
            airplanes = json_saver.get_data_from_file()

            if len(airplanes):
                print(f"\nСамолётов найдено: {len(airplanes)}!")
                for counter, plane in enumerate(airplanes, 1):
                    print(f"{counter}.\n{plane}\n\n")
            else:
                print("\nВ файле пока нет самолётов.")

        elif choice == "3":
            country = input("\nВведите страну регистрации (латиницей): ")
            airplanes = json_saver.get_data_from_file(country_of_registration=country)
            if len(airplanes):
                print(f"\nСамолётов найдено: {len(airplanes)}!")
                for counter, plane in enumerate(airplanes, 1):
                    print(f"{counter}.\n{plane}\n\n")
            else:
                print("\nВ файле нет самолётов с такой страной регистрации.")

        elif choice == "4":
            callsign = input("\nВведите позывной для удаления: ")

            airplane_to_delete = json_saver.get_data_from_file(call_sign=callsign)
            json_saver.delete_data_from_file(airplane_to_delete)

            print(f"\nСамолет с позывным {callsign} удален (если существовал).")

        elif choice == "5":
            n = int(input("\nТоп сколько самолётов показать?: "))

            airplanes = json_saver.get_data_from_file()
            airplanes = sorted(airplanes, key=lambda a: a.velocity, reverse=True)[:n]

            print(f"\nТоп {n} самолётов по скорости:\n")
            for counter, airplane in enumerate(airplanes, 1):
                print(f"{counter}.\n{airplane}\n\n")

        elif choice == "6":

            json_saver.delete_all_from_file()
            print("\nФайл очищен.")

        elif choice == "7":
            print("\nРабота программы завершена.")
            break
