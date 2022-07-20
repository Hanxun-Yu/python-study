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
    def millisecond_cur(self):
        return int(time.time() * 1000)

    def second_cur(self) -> float:
        """
        当前时间戳 秒
        """
        return int(time.time())

    def second_from_datetime(self, dtobj):
        """
        datetime对象 转 秒
        """
        return int(dtobj.timestamp())

    def ms_from_datetime(self, dtobj):
        """
        datetime对象 转 毫秒
        """
        return int(dtobj.timestamp() * 1000)

    def second_daystart_from_datetime(self, dtobj):
        """
        datetime对象 当天开始时刻 秒
        """
        newdt = dt.datetime(dtobj.year, dtobj.month, dtobj.day, 0, 0, 0)
        return self.second_from_datetime(newdt)

    def datetime_cur(self):
        """
        返回datetime对象 当前时间
        """
        return dt.datetime.now()

    def datetime_sometime_from_second(self, second):
        return dt.datetime.fromtimestamp(second)

    def datetime_daydelta(self, dtobj: dt.datetime, delta):
        return dtobj + dt.timedelta(days=delta)

    def format_from_second(self, second):
        return self.format_from_datetime(dt.datetime.fromtimestamp(second))

    def format_from_ms(self, ms):
        return self.format_from_datetime(dt.datetime.fromtimestamp(ms / 1000))

    def format_from_datetime(self, dtobj: dt.datetime):
        """
        %d-以零填充的十进制数字表示的月份的第几天。
        %m-以零填充的十进制数表示的月份。
        %Y-以世纪为十进制数的年份
        %H-小时（24小时制）作为一个零填充的十进制数。
        %M-分钟，用零填充的十进制数。
        %S-秒，用零填充的十进制数。
        %f微秒为十进制数，左边补零
        """
        return dtobj.strftime('[%Y-%m-%d %H:%M:%S]')
    
    def format_filename_from_second(self, second):
        return self.format_filename_from_datetime(dt.datetime.fromtimestamp(second))
    
    def format_filename_from_datetime(self, dtobj: dt.datetime):
        return dtobj.strftime('[%Y%m%d_%H%M%S]')


if __name__ == '__main__':
    th = TimeHelper()
    
    print("cur_ts_ms:" + str(th.millisecond_cur()))

    print("cur_ts_s:" + str(th.second_cur()))

    cur_datetime = th.datetime_cur()
    print("cur_datetime:" + str(cur_datetime))
    cur_minus_24day_datetime = th.datetime_daydelta(cur_datetime, -24)
    print("cur_datetime -24:" + str(cur_minus_24day_datetime))
    day_start_s = th.second_daystart_from_datetime(cur_minus_24day_datetime)
    print("day_start_s:" + str(day_start_s))
    print("cur_minus_24day_datetime:" + str(cur_minus_24day_datetime))

    print("sometime_s_datetime:" + th.format_from_second(cur_datetime.timestamp()))
    print("sometime_s_datetime:" + th.format_from_ms(cur_datetime.timestamp() * 1000))
