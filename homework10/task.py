# class MyRange:
#     def __init__(self, start, end= None):
#         if end is None:
#             start, end = 0, end
#         self._start = start
#         self._end = end
#
#     def __iter__(self):
#         return self
#     def __next__(self):
#         current = self._start
#         if self._start == self._end:
#             raise StopIteration('end')
#         self._start +=1
#         return current
# r = MyRange(1,3)
# print(next(r))
# print(next(r))
# print(next(r))
import os
import tempfile
from typing import Optional

import pytest


#
# # def my_range(start, end=None):
# #     if end is None:
# #         start, end = 0, start
# #     while start < end:
# #         yield start
# #         start += 1
# # r = my_range(1,3)
# # for i in r:
# file_name: Optional[str] = None
# def setup_function():
#     global  file_name
#     with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.txt', delete=False, dir= os.getcwd()) as tmp:
#         tmp.write(('test data'))
#         file_name =  tmp.name
#
# def teadown_function():
#     if os.path.isfile(file_name):
#         os.remove(file_name)
#
# def test_read():
#     with open(file_name, 'r') as file:
#         assert 'test data' == file.read()
# def test_update():
#     with open(file_name, 'a') as file:
#         file.write('test2')
#         with open(file_name, 'r') as file:
#             assert ' test2' in file.read()
# def test_delete():
#     os.remove(file_name)
# #     assert not os.path.isfile(file_name)
# from datetime import datetime
# import time
# class Test:
#
#     @classmethod
#     def setup_class(cls):
#         start_time = datetime.now().time()
#         print(f'\nВремя начала выполнения класса: {start_time}')
#         time.sleep(1)
#
#     @classmethod
#     def teardown_class(cls):
#         end_time = datetime.now().time()
#         print(f'\nВремя окончания выполнения класса: {end_time}')
#
#     def setup_method(test1):
#         start_time = datetime.now().time()
#         print(f'\nВремя начала выполнения теста test1: {start_time}')
#         return start_time
#
#     def teardown_method(test1):
#         end_time = datetime.now().time()
#
#         print(f'\nВремя окончания выполнения теста test1: {end_time}')
#
#
#
#     def test1(self):
#         assert (2 + 4) == 6
#         time.sleep(2)
#
#     def test2(self):
#         assert (800/1) == 800
#         time.sleep(2)
import os
import tempfile
import pytest


@pytest.fixture(scope='function')
def create_file():
    print('BEFORE TEST')
    with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', suffix='.txt', delete=False, dir=os.getcwd()) as tmp:
        tmp.write('test data')
    yield tmp.name
    print('AFTER TEST')
    if os.path.exists(tmp.name):
        os.remove(tmp.name)


def test_read(create_file):
    with open(create_file, 'r') as file:
        assert 'test data' == file.read()
    print('test read')


def test_update(create_file):
    with open(create_file, 'a') as file:
        file.write('test2')
    with open(create_file, 'r') as file:
        assert 'test2' in file.read()
    print('test update')


def test_delete(create_file):
    os.remove(create_file)
    assert not os.path.exists(create_file)
    print('test delete')



