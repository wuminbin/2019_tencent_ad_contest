# coding: utf-8

from collections import defaultdict
import sqlite3

import pandas as pd

from constants import DATA_DIR, HEADER_USER

user_multi_split = {'area': defaultdict(set), 'status': defaultdict(set), 'work': defaultdict(set), 'behavior': defaultdict(set)}

con = sqlite3.connect(DATA_DIR + 'user.db')

'''
在你的程序中有几个 pragma 可用于调整 sqlite3 的行为。特别地，其中一个可以改善性能的是synchronous：
connection.execute('PRAGMA synchronous = OFF')
你应该知道这可能是危险的。如果应用程序在事务中间意外崩溃，数据库可能会处于不一致的状态。所以请小心使用！ 但是如果你要更快地插入很多行，那么这可能是一个选择。
'''
con.execute('''CREATE TABLE user(
uid int,
col string,
value int
)''')

user = pd.read_csv(DATA_DIR + 'user_data', sep='\t', header=None, names=HEADER_USER,
                   index_col=False, dtype=str, quotechar='\t')

# multi_value_cols = list(user_multi_split.keys())
for col in user_multi_split:
    for tup in user[['uid', col]].itertuples(index=False):  # 默认index为True，作为tup[0]
        values = tup[1].strip(',').split(',')
        l = len(values)
        uids = [tup.uid] * l
        cols = [col] * l
        con.executemany('INSERT INTO user VALUES (?,?,?)', zip(uids, cols, values))
        con.commit()
