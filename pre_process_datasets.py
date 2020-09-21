#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from time import *

pd.options.mode.chained_assignment = None

# read_file_num = "main"
# read_file_num = "5"
# read_file_num = "11"
read_file_num = "12"
start_time = time()
# 读取文件
beer = pd.read_csv('E:\\Download\\DM pdfs\\DM projects1\\data\\dataset_'+read_file_num+".csv", sep=',')
beer['Label'] = len(beer)*[0]
# 将Power < 0的数据标记为异常数据
beer.loc[(beer["Power"] <= 0),("Label")] = 1
# RotorSpeed过小的数据标记为异常数据，不同的风机要设定不同的上限
beer.loc[beer["RotorSpeed"] < 5, "Label"] = 1
beer0 = beer[beer['Label'] == 0]
beer1 = beer[beer['Label'] == 1]
# 绘图
plt.scatter(beer0['WindSpeed'], beer0["Power"], c="green", s=5)
plt.scatter(beer1['WindSpeed'], beer1["Power"], c="red", s=5)
plt.xlabel('WindSpeed', fontsize=12)
plt.ylabel('Power', fontsize=12)

np.savetxt("E:\\Download\\DM pdfs\\DM projects1\\data\\just_tmp_data.csv", beer,header='WindNumber,Time,WindSpeed,Power,RotorSpeed,Index,label', delimiter=',',fmt='%s')
np.savetxt("E:\\Download\\DM pdfs\\DM projects1\\data\\tmpdata_"+read_file_num+".csv", beer[["WindNumber","Time","Label"]], delimiter=',',fmt='%s')

end_time = time()
print("耗时:"+str(end_time-start_time)+"s")
# 显示图片
plt.show()