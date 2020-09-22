"""

Project:    snakflake
Author:     LanHao
Date:       2020/9/21
Python:     python3.6

"""
import time

from .Counter import TimestampCounter


class Snow(object):
    _start_times_map: int  # 时间戳开始时间
    _counter: TimestampCounter  # 多进程安全的时间戳计数器
    _machine_id: int  # 服务器所在ID
    _machine_id_move: int  # 服务器ID 位移位数
    _times_map_move: int  # 时间戳位移位数
    _index_move: int  # 序列号位移个数

    def __init__(self, machine_id: int, start_times_map: int, times_map_move: int = 41, machine_id_move: int = 10,
                 index_move: int = 12):
        """
        machine_id 最多支持多大？

        :param machine_id:

        """
        self._start_times_map = start_times_map
        self._counter = TimestampCounter()
        self._machine_id = machine_id
        self._machine_id_move = machine_id_move
        self._times_map_move = times_map_move
        self._index_move = index_move

        assert self._machine_id < -1 ^ (-1 << self._machine_id_move), Exception("设备ID 超过位数上限")

    def get_increment_times_map(self) -> int:
        """
        增量时间戳
        :return:
        """
        times_map = int(time.time() * 1000) - self._start_times_map
        assert times_map < -1 ^ (-1 << self._times_map_move), Exception("时间戳超过了位数上限")
        return times_map

    def guid(self) -> int:
        """
        计算分布式自增 ID
        :return:
        """
        times_map = self.get_increment_times_map()
        index: int = self._counter.get_index()
        assert index < -1 ^ (-1 << self._index_move), Exception(f"序号超出位数上限")
        up_id = times_map << (self._machine_id_move + self._index_move) | self._machine_id << self._index_move | index
        return up_id
