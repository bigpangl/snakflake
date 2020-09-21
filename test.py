"""

Project:    snakflake
Author:     LanHao
Date:       2020/9/21
Python:     python3.6

"""
import time
import logging
from multiprocessing import Process

from snakflake.Counter import TimestampCounter
from snakflake.Snakflake import Snow

logging.basicConfig(level=logging.DEBUG)


def test(counter: Snow):
    while True:
        logging.debug(counter.guid())


if __name__ == '__main__':
    snow = Snow(10,int(time.time() * 1000))

    tests = []
    for _ in range(10):
        p = Process(target=test, args=(snow,))
        tests.append(p)
    for process in tests:
        process.start()

    for process in tests:
        process.join()
