"""

Project:    snakflake
Author:     LanHao
Date:       2020/9/21
Python:     python3.6

计数器

"""
import time
from multiprocessing import Value, Lock


class TimestampCounter(object):
    """

    多进程共享的时间戳计数器,只保留当前时间戳的计数器

    """
    _last_timestamp: Value  # 计数的时间戳,以double 类型保存int 值,以确保数据长度
    _counter: Value  # 计数器,此处同样使用了double 类型保存int 值,实际情况可根据状态并发数修改,位数不够容易发生溢出
    _lock: Lock  # 锁,多进程间访问控制

    def __init__(self):

        self._last_timestamp: Value = Value("d", TimestampCounter.get_timestamp(), lock=False)
        self._counter: Value = Value("d", 0, lock=False)
        self._lock: Lock = Lock()

    @staticmethod
    def get_timestamp() -> int:
        """
        将当前时间戳转换成int 类型进行返回,10 位长度是秒级，13 位长度是毫秒级
        :return:
        """
        return int(time.time() * 1000)

    def get_index(self) -> int:
        """
        获取当前时间点中的序号
        :return: int
        """
        timestamp = TimestampCounter.get_timestamp()
        with self._lock:
            if timestamp == self._last_timestamp.value:
                self._counter.value += 1
            else:
                self._last_timestamp.value = timestamp
                self._counter.value = 0
        return int(self._counter.value)
