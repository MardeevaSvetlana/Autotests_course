import pytest
import time
from datetime import datetime



@pytest.fixture(scope='class')
def current_time():
    start_time = datetime.now().time()
    print(f'\nВремя начала выполнения класса: {start_time}')
    yield
    end_time = datetime.now().time()
    print(f'\nВремя окончания выполнения класса: {end_time}')
    return start_time, end_time

@pytest.fixture
def work_time(current_time):
    global start_time, end_time
    time_work = end_time - start_time
    print(f'Время выполнения: {time_work}')



