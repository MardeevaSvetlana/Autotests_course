import pytest
import time
from datetime import datetime


@pytest.fixture(scope='class')  # Фикстура, которая выводит время начала и окончания выполнения класса
def current_time():
    print(f'\nВремя начала выполнения класса: {datetime.now().time()}')
    yield
    print(f'\nВремя окончания выполнения класса: {datetime.now().time()}')


@pytest.fixture  # Фикстура, которая выводит время выполнения теста
def work_time():
    start_time = time.time()
    yield
    end_time = time.time()
    print('\nПродолжительность теста: {:0.4} секунд\n'.format(end_time - start_time))
