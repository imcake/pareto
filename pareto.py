#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-01
# @Author  : imcake (likaike@gmail.com)
# @Link    : https://github.com/imcake

##############################################
# 计算累积频率分段值（帕累托图）
# 输入带有需要累积的值的csv文件和该值的字段名
# 输出百分之10-90对应的最相近数值
# 输出结果为字典，10:xxx, 20:xxx, ..., 90:xxx
#############################################
import pandas as pd


def get_pareto_penct(csv_name, value_column):
    data_df = pd.read_csv(csv_name, header=0)
    pencentList = []
    pencentage = 0
    for i in range(len(data_df)):
        rawList = data_df[value_column].tolist() # change colume to list
        rawList.sort(reverse=True)
        pencent = float(rawList[i]) / sum(rawList) * 100
        pencentage = pencentage + pencent # calculate the accumulated pencentage
        pencentList.append(pencentage)
    # add pencentage and raw date to a dict
    dictionary = dict(zip(pencentList, rawList))
    init_penct = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    value = []
    for j in init_penct:
        # get the closest raw date of certain pencentage
        dict_key = min(pencentList, key=lambda x: abs(x - j))
        value.append(dictionary.get(dict_key))
    result_dict = dict(zip(init_penct, value))
    return result_dict


if __name__ == '__main__':
    csv_name = 'pareto.csv' # csv文件名
    value_column = 'TOTAL' # 需要累积的字段名
    print get_pareto_penct(csv_name, value_column)
