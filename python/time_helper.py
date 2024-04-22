# -*- coding: utf-8 -*-
# @Time    : 2023/3/2 12:45
# @Author  : Hanxun Yu
# @Email   :
# @File    : time_helper.py
# @Software: PyCharm

# -*- coding: utf-8 -*-
# @Time    : 2021/3/19 10:36
# @Author  : Han-xun Yu
# @Email   : yuhanxun@126.com
# @File    : TimeHelper
# @Software: PyCharm

"""

"""
import time
import datetime as dt


class TimeConst:
    SECOND_PER_MINUTE = 60
    MINUTE_PER_HOUR = 60
    HOUR_PER_DAY = 24
    SECOND_PER_HOUR = MINUTE_PER_HOUR * SECOND_PER_MINUTE
    SECOND_PER_DAY = HOUR_PER_DAY * SECOND_PER_HOUR


class TimeHelper:

    @staticmethod
    def timestamp_ms():
        """
        当前时间戳 毫秒
        :return:
        """
        return int(time.time() * 1000)

    @staticmethod
    def timestamp_s() -> float:
        """
        当前时间戳 秒
        :return:
        """
        return int(time.time())

    @staticmethod
    def __ts_s_from_datetime(dtobj):
        """
        datetime对象 转 秒
        """
        return int(dtobj.timestamp())

    @staticmethod
    def __ts_ms_from_datetime(dtobj):
        return int(dtobj.timestamp() * 1000)

    @staticmethod
    def datetime_from_second(second):
        return dt.datetime.fromtimestamp(second)

    @staticmethod
    def second_of_daystart_from_second(second):
        """
        返回 当天开始时刻 秒
        """
        dtobj = TimeHelper.datetime_from_second(second)
        newdt = dt.datetime(dtobj.year, dtobj.month, dtobj.day, 0, 0, 0)
        return TimeHelper.__ts_s_from_datetime(newdt)

    @staticmethod
    def second_day_delta(day_second, day_delta):
        """
        比如
        day_second:2023-02-03 13:00:00
        day_delta: 2

        返回 2023-02-01 13:00:00
        :param day_second: 该天时间戳
        :param delta: 天数 偏移量
        :return:
        """
        day_datetime = TimeHelper.datetime_from_second(day_second)
        day_datetime += dt.timedelta(days=day_delta)

        return TimeHelper.__ts_s_from_datetime(day_datetime)

    @staticmethod
    def day_count(day1_second, day2_second) -> int:
        """
        返回从day1_second到day2_second 有多少天，闭区间
        :param day1_second:
        :param day2_second:
        :return:
        """
        day1_second = TimeHelper.second_of_daystart_from_second(day1_second)
        day2_second = TimeHelper.second_of_daystart_from_second(day2_second)

        return int(abs(day1_second - day2_second) / (24 * 60 * 60) + 1)

    def format_from_second(self, second):
        return self.format_from_datetime(dt.datetime.fromtimestamp(second))

    @staticmethod
    def format_to_YYYYmmdd_from_second(second):
        return dt.datetime.fromtimestamp(second).strftime('%Y%m%d')

    @staticmethod
    def format_to_HHMMSS_from_second(second):
        return dt.datetime.fromtimestamp(second).strftime('%H:%M:%S')

    @staticmethod
    def format_to_second_from_YYYYmmdd(str):
        dtobj = dt.datetime.now()
        dtobj = dtobj.strptime(str, '%Y%m%d')
        second = TimeHelper.__ts_s_from_datetime(dtobj)
        return TimeHelper.second_of_daystart_from_second(second)

    @staticmethod
    def format_to_YYYYmmdd_HHMMSS_from_second(second):
        """
        %d-以零填充的十进制数字表示的月份的第几天。
        %m-以零填充的十进制数表示的月份。
        %Y-以世纪为十进制数的年份
        %H-小时（24小时制）作为一个零填充的十进制数。
        %M-分钟，用零填充的十进制数。
        %S-秒，用零填充的十进制数。
        %f微秒为十进制数，左边补零
        """
        return dt.datetime.fromtimestamp(second).strftime('[%Y-%m-%d %H:%M:%S]')

    # def format_filename_from_second(self, second):
    #     return self.format_filename_from_datetime(dt.datetime.fromtimestamp(second))
    #
    # def format_filename_from_datetime(self, dtobj: dt.datetime):
    #     return dtobj.strftime('[%Y%m%d_%H%M%S]')


if __name__ == '__main__':
    second_now = TimeHelper.timestamp_s()
    print("cur_ts_s:{} format:{}".format(str(second_now), TimeHelper.format_to_YYYYmmdd_HHMMSS_from_second(second_now)))

    second_now_minus_24day = TimeHelper.second_day_delta(second_now, -24)
    print("second_now_minus_24day:{} format:{}".format(str(second_now_minus_24day),
                                                       TimeHelper.format_to_YYYYmmdd_HHMMSS_from_second(
                                                           second_now_minus_24day)))

    second_day_start = TimeHelper.second_of_daystart_from_second(second_now)
    print("second_day_start:{} format:{}".format(str(second_day_start),
                                                 TimeHelper.format_to_YYYYmmdd_HHMMSS_from_second(second_day_start)))

    second2 = TimeHelper.format_to_second_from_YYYYmmdd('20230225')
    print("format_to_second_from_YYYYmmdd:" + str(second2))
    print("format_to_YYYYmmdd_from_second:" + TimeHelper.format_to_YYYYmmdd_from_second(second2))
    print("format_to_HHMMSS_from_second:" + TimeHelper.format_to_HHMMSS_from_second(second_now))

    # -----------------------------------
    print("daycount:{}".format(TimeHelper.day_count(second_now, second_now_minus_24day)))
