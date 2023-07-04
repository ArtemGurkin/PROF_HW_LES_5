import os
import time
import datetime

def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            t1 = time.time()
            date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            res = old_function(*args, **kwargs)
            t2 = time.time()
            with open(path, 'a') as log_file:
                log_file.write(f'name_function - {old_function.__name__}\n'
                               f'datetime: {date}\n'
                               f'time: {t2 - t1}\n'
                               f'args = {args}\n'
                               f'kwargs = {kwargs}\n'
                               f'result: {res}\n\n')
            return res
        return new_function

    return __logger

def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger(path)
        def hello_world():
            return 'Hello World'

        @logger(path)
        def summator(a, b=0):
            return a + b

        @logger(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), 'Функция возвращает "Hello World"'
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert  result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:
        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_2()