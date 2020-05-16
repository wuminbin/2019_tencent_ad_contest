# 运行步骤
* ad_fea_clean得到clean_ad_static_feature（h5及csv）
> ad_static_feature 735911条去重得到509252条，去掉多值情况及创建时间小于等于0的得到497666条（ad_id已经唯一了）,ad_id去重后保存
> ad_operation 760866去重后760096条，当天去重后得到494044条（其中广告id有38843唯一值但37321条为新建记录且无status）！
> ad_daily_fea从ad_operation groupby ID及操作日，有321606条，去掉空值后有320084条，保存ad_fea_op_by_day（h5及csv）
> ad_sample = ad_fea_op_by_day.merge(ad_static_feature)得到258137条，去除日期不对的得到257169，构造每日ad状态值697997条，保存ad_date_valid（h5及csv）
> 下一天无操作的469610条，status为1的175680条，保存train_sample（h5及csv），TODO：确认当天之后是不是存在已曝光的广告，及自动生效的
* clean_total_exposure_n_label
* gen_dataset
* user_stat
* py2 user_match.py data/testA/Btest_sample_new.tsv data/testA/dataset_crow_single_match.out
* gen_libsvm

user_table.py
user_table_reset_index.py
py2 user_match.py data/testA/dataset.tsv data/testA/dataset_crow_match.out
* 之后跑模型即可