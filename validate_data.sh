#!/usr/bin/env bash
# 曝光日志都是10列
cat data/testA/totalExposureLog.out | awk -F "\t" '{print NF}' | grep -vE "^10$"  # $? == 1
# 没有20190230（无效日期）修改后值为非零的记录
cat ad_operation.dat | grep 20190230 | grep -vE '\t0$'  # $? == 1
# 测试集很标准
cat test_sample.dat |awk -F "\t" '{print NF}' | grep -vE "^11$"  # $? == 1

# 划分测试验证集

