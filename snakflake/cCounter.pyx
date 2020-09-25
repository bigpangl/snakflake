#cython:language_level=3
import time
from multiprocessing import Value, Lock


class TimestampCounter(object):
    """

    多进程共享的时间戳计数器,只保留当前时间戳的计数器

    """

    def __init__(self):

        self._last_timestamp = Value("d", TimestampCounter.get_timestamp(), lock=False)
        self._counter = Value("d", 0, lock=False)
        self._lock = Lock()

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
