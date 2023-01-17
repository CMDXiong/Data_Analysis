# -*- coding:utf-8 -*-
__author__ = 'px'

import pandas as pd
import scipy.stats as ss


df = pd.read_csv("./data/HR.csv")
# print(df)

qt_25 = df.quantile(q=0.25)
print(qt_25)

mode = df.mode()
print(mode)

std = df['satisfaction_level'].std()
print("std:", std)

var = df.var()
print("var:", var)

skew = df.skew()
print("skew: ", skew)

kurt = df.kurt()
print("kurt: ", kurt)


print(ss.norm.stats(moments="mvsk"))

# 正态分布0点的值
print(ss.norm.pdf(0.0))

# 累积概率对应的x位置
print(ss.norm.ppf(0.95))

# 累积到2所对应的概率
print(ss.norm.cdf(2))

# 卡方分布
# ss.chi2

# t分布
# ss.t

# F分布
# ss.f

# 抽样
df.sample(n=10)
df.sample(frac=0.001)

