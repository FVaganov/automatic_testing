import pytest


# Создаем функцию для запуска тестов
def run_tests():
    # Запускаем все тесты с подробным выводом
    result = pytest.main(["-v"])

    # Проверяем результат выполнения тестов
    if result == 0:
        print("Все тесты успешно пройдены.")
        return True
    else:
        print("Тесты не прошли. Пожалуйста, проверьте лог ошибок для подробной информации.")
        return False


if __name__ == "__main__":
    if run_tests():
        print("Тесты успешно выполнены: True")
    else:
        print("Произошла ошибка при выполнении тестов: False")
