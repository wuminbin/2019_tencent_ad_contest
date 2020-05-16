# -*- coding: utf-8 -*-

HEADER_TOTAL_EXPOSURE = ['req_id', 'req_ts', 'ad_loc_id', 'uid', 'ad_id', 'expo_size', 'bid', 'pctr',
                         'quality_ecpm', 'total_ecpm']
HEADER_AD_STATIC = ['ad_id', 'create_ts', 'account_id', 'product_id', 'product_class', 'industry_id', 'sizes']
# device与crow不符
HEADER_USER = ['uid', 'age', 'gender', 'area', 'status', 'education', 'consuptionAbility', 'os',
               'work', 'connectionType', 'behavior']
HEADER_AD_OPERATION = ['ad_id', 'op_time', 'op_type', 'op_col', 'finished_kvs']

HEADER_TEST_SAMPLE = ['id', 'ad_id', 'create_ts', 'sizes', 'industry_id', 'product_class', 'product_id', 'account_id',
                      'exposure_time', 'crow', 'bid']
DATA_DIR = 'data/testA/'
