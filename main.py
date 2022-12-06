import csv
import pandas as pd
import sys
import itertools
import math

atraction_name = ["美女と野獣_魔法の物語", "スプラッシュマウンテン", "ベイマックスのハッピーランド",
                  "ビッグサンダーマウンテン", "ホーンテッドマンション"]

df = pd.read_csv('time.csv')
df_map = pd.read_csv("map.csv", index_col = 0)
print("現在の時刻を入力してね")
hour = input("何時? ")
minute = input("何分? ")
print("乗りたいアトラクションを3つ選んでね")
print("美女と野獣_魔法の物語  1")
print("スプラッシュマウンテン　2")
print("ベイマックスのハッピーランド　3")
print("ビッグサンダーマウンテン  4")
print("ホーンテッドマンション　5")

atraction_1 = atraction_name[int(input()) - 1]
atraction_2 = atraction_name[int(input()) - 1]
atraction_3 = atraction_name[int(input()) - 1]

df_atraction = df.loc[:, ["time", atraction_1, atraction_2, atraction_3]]
go_atraction = [atraction_1, atraction_2, atraction_3]
df_atraction_permutation = list(itertools.permutations(go_atraction, 3))

current_time = int(hour) + float(minute) / 60.0

min_wait = 10000
best_atraction = 0

time_index = df_atraction.index[(df_atraction["time"] - current_time).abs().argsort()][0].tolist()

for i in df_atraction_permutation:
    store_wait = 0.0
    current_time = int(hour) + float(minute) / 60.0

    for j in i:
        current_time += store_wait / 60.0
        time_index = df_atraction.index[(df_atraction["time"] - current_time).abs().argsort()][0].tolist()
        store_wait += df_atraction.loc[time_index][j]

    if(store_wait < min_wait):
        min_wait = store_wait
        best_atraction = i

current_time = int(hour) + float(minute) / 60.0
print("現在時刻 " + str(int(current_time)) + ":" + str(int(((current_time - int(current_time)) * 60))))
print("回る順番")
number = 1
for i in best_atraction:
    time_index = df_atraction.index[(df_atraction["time"] - current_time).abs().argsort()][0].tolist()
    print(str(number) + "番目 " + str(i), end = " ")
    print("待ち時間" +  str(int(df_atraction.loc[time_index][i])) + "分", end = " ")
    print("アトラクション終了時刻" +str(int(current_time + df_atraction.loc[time_index][i] / 60.0)) + ":" + str(int((current_time + df_atraction.loc[time_index][i] / 60.0 - int(current_time + df_atraction.loc[time_index][i] / 60.0)) * 60)))
    current_time += df_atraction.loc[time_index][i] / 60.0
    number += 1

