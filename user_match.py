# coding: utf-8

import cPickle
import sys

import pandas as pd

from constants import DATA_DIR


def main():
    fn_in = sys.argv[1]
    fn_out = sys.argv[2]

    with open(DATA_DIR + 'all_user.pkl', 'rb') as fr:
        all_user = cPickle.load(fr)  # set
        len_all_user = len(all_user)
    with open(DATA_DIR + 'user_single_split.pkl', 'rb') as fr:
        user_single_fea = cPickle.load(fr)
        user_single_cols = set(user_single_fea.keys())
    crow_set = set(pd.read_csv(fn_in, sep='\t', usecols=['crow'])['crow'].tolist())
    fw = open(fn_out, 'a')
    for crow in crow_set:
        if crow == 'all':
            uid_num = len_all_user
            fw.write('%s\t%s\n' % (crow, uid_num))
            continue
        uid_set = None
        for kv in crow.split('|'):
            col, values = kv.split(':')
            if col in user_single_cols:
                match_uids = set()
                to_match_dict = user_single_fea[col]
                for v in values.split(','):
                    match_uids |= to_match_dict.get(v, set())
                if not match_uids:  # 提前终止
                    uid_set = match_uids
                    break
                if uid_set is None:
                    uid_set = match_uids
                else:
                    uid_set &= match_uids

        if uid_set is None:
            uid_num = len_all_user  # 没有筛选用户单值特征
        else:
            uid_num = len(uid_set)

        fw.write('%s\t%s\n' % (crow, uid_num))

if __name__ == '__main__':
    main()
