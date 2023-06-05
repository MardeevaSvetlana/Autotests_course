# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(a, b):  # Функция, которая принимает два аргумента и возвращает частое
    return a/b


@pytest.mark.parametrize('a, b, result',  # Задаем параметры
[pytest.param(2, 2, 1, marks=pytest.mark.skip('bad test')),   # Один тест скипаем
pytest.param(-50, -5, 10, marks=pytest.mark.smoke('smoke')),  # Один тест маркируем smoke
(-1, 1, -1),
(555, 5, 111),
(2, 1, 2)])

def test_division_res(a, b, result):
    assert all_division(a, b) == result


