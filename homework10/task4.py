# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import pytest


def all_division(*arg1):  # Функция для нахождения частного
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.usefixtures('current_time')  # Марка для применения к классу фикстуры 'current_time'
class Test:

    def test1(self, work_time):  # для теста используется фикстура 'work_time'
        assert all_division(100, 2) == 50

    def test2(self):
        with pytest.raises(ZeroDivisionError):
            all_division(100, 0)

