"""

Project:    snakflake
Author:     LanHao
Date:       2020/9/21
Python:     python3.6

"""
import logging
from multiprocessing import Process

from snakflake.Counter import TimestampCounter

logging.basicConfig(level=logging.DEBUG)


def test(counter: TimestampCounter):
    for i in range(1000):
        counter.get_index()



if __name__ == '__main__':
    counter = TimestampCounter()
    tests = []
    for _ in range(5):
        p = Process(target=test,args=(counter,))
        tests.append(p)
    for process in tests:
        process.start()

    for process in tests:
        process.join()
