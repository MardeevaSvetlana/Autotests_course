# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

from datetime import datetime
import time

import pytest
import time
from datetime import datetime




class Test():

    def test1(current_time):
        assert (2 + 4) == 6



    def test2(self):
        assert (800/1) == 800
