# coding=utf-8

from datetime import datetime, timedelta


def get_day_list(start_day, end_day, fmt=None):
    end_date = datetime.strptime(end_day, '%Y%m%d')
    start_date = datetime.strptime(start_day, '%Y%m%d')
    if fmt is None:
        res = [start_date]
    else:
        res = [start_date.strftime(fmt)]
    while start_date <= end_date:
        start_date += timedelta(days=1)
        if fmt is None:
            res.append(start_date)
        else:
            res.append(start_date.strftime(fmt))
    return res
