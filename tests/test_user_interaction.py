from src.user_interaction import user_interaction


def test_user_interaction_core_branches(monkeypatch, capsys):
    """Покрывает ветки меню 2, 4, 6, 7"""

    # Заглушка
    class FakeSaver:
        def get_data_from_file(self, **kwargs):
            return []

        def delete_data_from_file(self, _):
            pass

        def delete_all_from_file(self):
            pass

    # Подменяем класс на заглушку
    monkeypatch.setattr("src.user_interaction.AirplaneFileJson", lambda: FakeSaver())

    mock_inputs = iter(["2", "4", "EAGLE", "6", "7"])
    monkeypatch.setattr("builtins.input", lambda test: next(mock_inputs))

    user_interaction()

    out = capsys.readouterr().out

    assert "В файле пока нет самолётов." in out
    assert "удален" in out
    assert "Файл очищен." in out
    assert "Работа программы завершена." in out
