"""

Project:    snakflake
Author:     LanHao
Date:       2020/9/21
Python:     python3.6

"""
import time
import logging
from multiprocessing import Process

# from snakflake.Counter import TimestampCounter
from snakflake.cCounter import TimestampCounter
from snakflake.cSnakflake import Snow

logging.basicConfig(level=logging.DEBUG)


# print(get_timestamp())

# counter = TimestampCounter()
# #
# while True:
#     logging.debug(counter.get_index())
def test(counter: Snow):
    while True:
        # logging.debug(f"获取到的id 为:{counter.guid()}")
        print(counter.guid())

if __name__ == '__main__':
    snow = Snow(10, int(time.time() * 1000))

    tests = []
    for _ in range(1):
        p = Process(target=test, args=(snow,))
        tests.append(p)
    for process in tests:
        process.start()

    for process in tests:
        process.join()
