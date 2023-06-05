import pytest
import time
from datetime import datetime



@pytest.fixture()
def current_time():
    start_time = datetime.now().time()
    print(f'\nВремя начала выполнения теста: {start_time}')
    return start_time
    yield
    end_time = datetime.now().time()
    print(f'\nВремя окончания выполнения теста: {end_time}')
    return end_time

@pytest.fixture()
def sum_time(current_time):
    sum_time = end_time - start_time


