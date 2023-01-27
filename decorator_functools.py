import time
from functools import wraps


class MyTestCase():
    pass


def wrong_timelogger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        finish = time.time()
        print(f'{func.__name__}: {finish - start}')
        return result
    return wrapper

@wrong_timelogger
def longloop(num):
    '''
    longloop function
    :param num
    result

    '''
    while num > 0:
        num -= 1



if __name__ == '__main__':
    longloop(10000000)
    longloop.__wrapped__(10000000)


