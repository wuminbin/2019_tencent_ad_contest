# coding: utf-8

import cPickle
import sqlite3
import sys

from constants import DATA_DIR

all_multi_value_cols = ['status', 'work', 'behavior', 'area']


def get_match_cnt(con, col):
    sql = '''SELECT value, count(1) FROM user WHERE col = "%s"
              GROUP BY value''' % (col, )
    return con.execute(sql).fetchall()


def main():
    fn_out = sys.argv[1]

    con = sqlite3.connect(DATA_DIR + 'user.db')
    with open(DATA_DIR + 'all_user.pkl', 'rb') as fr:
        all_user = cPickle.load(fr)  # set
        len_all_user = len(all_user)
        dem = float(len_all_user)
    fw = open(fn_out, 'a')
    for col in all_multi_value_cols:
        res = get_match_cnt(con, col)
        for value, cnt in res:
            fw.write('%s\t%s\t%s\n' % (col, value, cnt / dem))

if __name__ == '__main__':
    main()
