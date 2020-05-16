# -*- coding: utf-8 -*-

import pandas as pd
# import numpy as np

from constants import HEADER_TOTAL_EXPOSURE, HEADER_AD_STATIC, HEADER_USER

_data_dir = 'data/testA/'

# totalExposureLog.out
# user_data
# ad_operation.dat
# test_sample.dat
# ad_static_feature.out
totalExposure = pd.DataFrame(
    columns=HEADER_TOTAL_EXPOSURE)

ad_static_feature = pd.DataFrame(
    columns=HEADER_AD_STATIC)

user = pd.DataFrame(
    columns=HEADER_USER)

ADExposure = pd.DataFrame(columns=['num'])


def preTotalExposure():
    with open(_data_dir + 'totalExposure', 'r', encoding='utf-8') as f:
        new = open(_data_dir + 'ad_static_feature.csv', 'w')
        i = 0
        for line in f:
            if i % 1000000 == 0:
                print(i, line)
            if i == 0:
                new.write(
                    'AD_id,time,AD_loc_id,user_id,expo_id,expo_size,expo_bid,expo_pctr,expo_quality_ecpm,'
                    'expo_total_ecpm\n')
                lineContent = line.split('m')
                print(lineContent[len(lineContent) - 1])
                new.write(lineContent[len(lineContent) - 1])
            else:
                new.write(line)
            i += 1


def preADStatic():
    with open(_data_dir + 'ad_static_feature.out', 'r', encoding='utf-8') as f:
        new = open(_data_dir + 'ad_static_feature.csv', 'w')
        new.write('AD_id,time,account_id,product_id,product_class,industry_id,size,is_multi_size\n')
        for line in f:
            line = line.replace('\n', '')
            lineContent = line.split('\t')
            if len(lineContent) == 7 and lineContent[6] == '':
                for i in range(3):
                    new.write(lineContent[i] + ',')
                new.write('0,')
                new.write(lineContent[3] + ',')
                new.write(lineContent[4] + ',')
                if ',' in lineContent[5]:
                    size = 0
                    size_tmp = lineContent[5].split(',')
                    for _ in size_tmp:
                        size += int(_)
                    size /= len(size_tmp)
                    new.write(str(size) + ',1\n')
                else:
                    new.write(lineContent[5] + ',0\n')
            elif len(lineContent) == 7:
                for i in range(6):
                    new.write(lineContent[i] + ',')
                if ',' in lineContent[6]:
                    size = 0
                    size_tmp = lineContent[6].split(',')
                    for _ in size_tmp:
                        size += int(_)
                    size /= len(size_tmp)
                    new.write(str(size) + ',1\n')
                else:
                    new.write(lineContent[6] + ',0\n')
            else:
                print('ERROR: ', line)


def preUser():
    with open(_data_dir + 'user_data', 'r', encoding='utf-8') as f:
        new = open(_data_dir + 'user_data.csv', 'w')
        i = 0
        for line in f:
            if i == 0:
                new.write(
                    'user_id,age,gender,area,status,education,consumption_ability,device,work,connect_type,behavior\n')
            line = line.replace('\t', ',')
            new.write(line)
            if i % 100000 == 0:
                print(i, line)
            i += 1


def countTotalExposure():
    with open(_data_dir + 'totalExposure.csv', 'r', encoding='utf-8') as f:
        i = 0
        for line in f:
            line_content = line.strip('\n').split('\t')
            if i % 100000 == 0:
                print(line_content[0])
            try:
                ADExposure.loc[line_content[0]] = ADExposure.loc[line_content[0]] + 1
            except:
                ADExposure.loc[line_content[0]] = 0
            i += 1


def clean_total_exposure_log():
    with open(_data_dir + 'totalExposureLog.out', 'r', encoding='utf-8') as f:
        new = open(_data_dir + 'totalExposure.csv', 'w')
        i = 0
        for line in f:
            if line.split('\t') != 10:
                print(line)
            line = line.replace('\t', ',')
            new.write(line)
            i += 1


def count_total_exposure():
    df = pd.read_csv(_data_dir + 'totalExposure.csv', header=None,
                     names=['ad_id', 'time', 'ad_loc_id', 'user_id', 'expo_id', 'expo_size', 'expo_bid', 'expo_pctr',
                            'expo_quality_ecpm',
                            'expo_total_ecpm'])
    print(len(df.groupby('ad_id')))
    print(len(df))

# clean_total_exposure_log()  # 无需清理
count_total_exposure()
print(ADExposure.index.is_unique)
